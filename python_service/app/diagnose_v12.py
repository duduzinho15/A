import psycopg2
from psycopg2.extras import RealDictCursor
import json
import os
from datetime import datetime

def check_v12_state():
    # Credenciais corretas conforme docker-compose.yml
    db_url = "postgresql://n8n:n8npassword@postgres:5432/n8n"
    
    try:
        conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
        with conn.cursor() as cur:
            # 1. Verifica Leads
            cur.execute("SELECT status, count(*) FROM news_leads GROUP BY status")
            leads = cur.fetchall()
            print("\n📊 ESTATÍSTICAS DE LEADS (Buffer):")
            if not leads:
                print("   Nenhum lead encontrado no buffer.")
            for l in leads:
                print(f"   - {l['status']}: {l['count']} itens")

            # 2. Mostra os últimos 3 leads pendentes
            cur.execute("SELECT title, created_at FROM news_leads WHERE status = 'pending' ORDER BY created_at DESC LIMIT 3")
            pending = cur.fetchall()
            if pending:
                print("\n🔔 ÚLTIMOS LEADS PENDENTES:")
                for p in pending:
                    print(f"   [ {p['created_at'].strftime('%H:%M:%S')} ] {p['title'][:50]}...")

            # 3. Verifica Jobs
            cur.execute("SELECT status, count(*) FROM video_jobs GROUP BY status")
            jobs = cur.fetchall()
            print("\n🎬 ESTATÍSTICAS DE JOBS (Produção):")
            if not jobs:
                print("   Nenhum job de vídeo encontrado.")
            for j in jobs:
                print(f"   - {j['status']}: {j['count']} vídeos")

        conn.close()
    except Exception as e:
        print(f"Erro ao conectar no banco interno: {e}")

if __name__ == "__main__":
    check_v12_state()
