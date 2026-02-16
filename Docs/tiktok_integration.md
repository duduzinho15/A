# 🎵 Integração TikTok Uploader (TiktokAutoUploader)

Start Date: 2026-02-14  
Status: **Integrated (with caveats)**  
Library: [TiktokAutoUploader](https://github.com/makiisthenes/TiktokAutoUploader) (Cloned)

## 📋 Visão Geral

A integração de upload para TikTok foi implementada utilizando uma versão clonada e *patchada* da biblioteca `TiktokAutoUploader`. Devido a instabilidades na estrutura do repositório original e incompatibilidades com o `cli.py` fornecido, um script customizado foi desenvolvido para interagir diretamente com a função de upload.

## 🛠️ Componentes

### 1. Script Customizado: `tiktok_custom_uploader.py`

Localizado em: `python_service/app/tiktok_custom_uploader.py`
Função:

- Substitui o `cli.py` original (que estava quebrado/desatualizado).
- Importa diretamente `upload_video` de `tiktok_uploader.tiktok`.
- Gerencia argumentos e chama a função de upload nativa da biblioteca.
- Invocado via `subprocess` pelo endpoint `/publish/tiktok` (em `publish.py`).

### 2. Patch na Biblioteca: `tiktok.py`

Arquivo: `/app/tiktok_uploader/tiktok_uploader/tiktok.py` (no container)
Modificações aplicadas:

- **User-Agent Fixo**: A biblioteca original usava `UserAgent().random`, o que gerava incompatibilidade com cookies exportados de navegadores reais (Chrome Windows). Foi fixado um User-Agent de Chrome on Windows.
- **Correção de Identação**: O arquivo original usa Tabs, patches devem respeitar isso.

### 3. Cookies e Sessão

- **Origem**: `/data_midia/cookies_tiktok.txt` (exportados via extensão Netscape).
- **Processamento**: `publish.py` converte para formato `pickle` (.cookie) esperado pela biblioteca.
- **Armazenamento**: `/app/tiktok_uploader/CookiesDir/tiktok_session-auto.cookie`.

## ⚠️ Problemas Conhecidos (Caveats)

### Erro "Code 8" (Project Create Failed)

Apesar da autenticação e carregamento de cookies funcionarem (login validado com sucesso), a API do TikTok pode rejeitar a criação do projeto de upload (`project/create`) com o seguinte comportamento:

- **Status HTTP**: 200 OK
- **Status Code JSON**: `8` (Erro genérico de sessão/permissão)
- **Sintoma**: O script falha com `KeyError: 'project'` pois a chave não existe na resposta.

**Causa Provável**:

- Detecção de automação/bot pelo TikTok (mesmo com cookies reais).
- Restrição da conta ou do IP do datacenter (Docker IP).
- Falta de assinatura (`_signature`/`X-Bogus`) na etapa `project/create` (a biblioteca só assina o POST subsequente).

**Solução de Contorno**:

- A aplicação detecta este erro e retorna uma mensagem clara: *"TikTok recusou a criacao do projeto de upload..."*.
- Recomendado tentar re-exportar cookies frescos ou rotacionar IP.

## 🚀 Como Testar Manualmente

Dentro do container `python_service`:

```bash
# Navegar para o diretório da biblioteca (Importante para carregar cookies relativos!)
cd /app/tiktok_uploader

# Executar script
export PYTHONPATH=/app/tiktok_uploader
python /app/app/tiktok_custom_uploader.py --video /data_midia/videos/teste.mp4 --title "Teste" --user auto
```
