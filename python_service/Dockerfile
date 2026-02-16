# =============================================================================
# Dockerfile — Python Service (FastAPI + Trafilatura + MoviePy)
# =============================================================================
# Multi-stage build para imagem menor no final.
# ffmpeg é obrigatório para moviepy e edge-tts.
# =============================================================================

# ---------------------------------------------------------------------------
# Stage 1: instalar dependências
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Stage 1: instalar dependências (Builder)
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Stage 1: instalar dependências (Builder)
# ---------------------------------------------------------------------------
FROM python:3.10-slim AS builder

# Reset entrypoint
ENTRYPOINT []

WORKDIR /build

ENV DEBIAN_FRONTEND=noninteractive

# Install build deps (gcc, python, git, etc)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala no venv
COPY requirements.txt .
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# --- Clone & Install TiktokAutoUploader Deps (Builder Stage) ---
RUN git clone https://github.com/makiisthenes/TiktokAutoUploader.git /build/tiktok_uploader

# ---------------------------------------------------------------------------
# Stage 2: imagem final com suporte a GPU e Playwright
# ---------------------------------------------------------------------------
FROM nvidia/cuda:12.6.3-runtime-ubuntu22.04 AS runtime

# Reset entrypoint
ENTRYPOINT []

# Install Python and dependencies
ENV DEBIAN_FRONTEND=noninteractive

# Install base packages + ffmpeg + python
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    python3 \
    python3-pip \
    python3-venv \
    ffmpeg \
    git \
    imagemagick \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (needed by TikTok signature generator).
# Ubuntu 22.04 repos ship an outdated Node; use NodeSource for a modern runtime.
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Compatibility symlinks: builder venv scripts use /usr/local/bin/python* shebangs.
RUN mkdir -p /usr/local/bin \
    && ln -sf /usr/bin/python3 /usr/local/bin/python3 \
    && ln -sf /usr/bin/python3 /usr/local/bin/python \
    && if [ -x /usr/bin/python3.10 ]; then ln -sf /usr/bin/python3.10 /usr/local/bin/python3.10; fi

# Configuração de segurança do ImageMagick para permitir leitura/escrita de PDFs e outros (necessário para MoviePy)
# Adjust policy path (ImageMagick 6 or 7)
RUN if [ -f /etc/ImageMagick-6/policy.xml ]; then \
    sed -i 's/pixel" value="none"/pixel" value="1GiB"/' /etc/ImageMagick-6/policy.xml \
    && sed -i 's/disk" value="none"/disk" value="1GiB"/' /etc/ImageMagick-6/policy.xml \
    && sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/' /etc/ImageMagick-6/policy.xml; \
    elif [ -f /etc/ImageMagick-7/policy.xml ]; then \
    sed -i 's/pixel" value="none"/pixel" value="1GiB"/' /etc/ImageMagick-7/policy.xml \
    && sed -i 's/disk" value="none"/disk" value="1GiB"/' /etc/ImageMagick-7/policy.xml \
    && sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/' /etc/ImageMagick-7/policy.xml; \
    fi

# Copia apenas o venv compilado do stage anterior
COPY --from=builder /opt/venv /opt/venv

# Configura PATH para usar o venv
ENV PATH="/opt/venv/bin:${PATH}"
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Cria usuário não-root (segurança)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Diretório de trabalho
WORKDIR /app

# Copia o código da aplicação
COPY app/ ./app/
COPY test_tiktok_auth.py ./test_tiktok_auth.py
COPY test_youtube_auth.py ./test_youtube_auth.py
COPY auth_youtube.py ./auth_youtube.py

# Permissões para o usuário appuser
RUN chown -R appuser:appuser /app

# Diretório para arquivos de mídia (será montado como volume)
RUN mkdir -p /data_midia && chown appuser:appuser /data_midia

# --- TikTok Auto Uploader (User Request) ---
# Copia o repo já preparado do builder
COPY --from=builder /build/tiktok_uploader /app/tiktok_uploader

RUN /opt/venv/bin/pip install --no-cache-dir \
    fake-useragent==1.4.0 \
    requests-auth-aws-sigv4==0.7 \
    undetected-chromedriver \
    pytube

# Install Node deps for the signature generator (avoid downloading browsers here;
# Python Playwright step below installs Chromium into PLAYWRIGHT_BROWSERS_PATH).
RUN cd /app/tiktok_uploader/tiktok_uploader/tiktok-signature \
    && PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm ci --omit=dev

# Hotfixes for the vendored TikTok uploader (signature/cookies handling).
COPY overrides/tiktok_uploader/tiktok.py /app/tiktok_uploader/tiktok_uploader/tiktok.py

# Instala dependências de SO e Browsers do Playwright
# --with-deps instala libs do linux necessárias (requer apt-get update antes)
# chromium apenas para economizar espaço
RUN mkdir -p /ms-playwright \
    && apt-get update \
    && /opt/venv/bin/playwright install --with-deps chromium \
    && rm -rf /var/lib/apt/lists/*

# Permissões extras para o usuário appuser no diretório do uploader
RUN chown -R appuser:appuser /app/tiktok_uploader /ms-playwright

USER appuser

# Porta que o FastAPI vai escutar
EXPOSE 8000

# Comando de início — uvicorn com reload desabilitado (produção)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
