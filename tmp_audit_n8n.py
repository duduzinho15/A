import psycopg2
import json

def audit_n8n():
    try:
        # Connect to the n8n database in the postgres container
        # Since I'm running from the host, but the db is in docker, 
        # I should check if I can connect via localhost:5432 (mapped)
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="n8n",
            user="n8n",
            password="n8npassword"
        )
        cur = conn.cursor()
        
        print("--- ÚLTIMAS 10 FALHAS DE EXECUÇÃO ---")
        cur.execute("""
            SELECT 
                e.id, 
                w.name, 
                e.status, 
                e."startedAt", 
                e."stoppedAt"
            FROM execution_entity e
            JOIN workflow_entity w ON e."workflowId" = w.id
            WHERE e.status IN ('error', 'failed')
            ORDER BY e."startedAt" DESC
            LIMIT 10;
        """)
        
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]} | Workflow: {row[1]} | Status: {row[2]} | Início: {row[3]}")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"ERRO DE CONEXÃO/AUDITORIA: {e}")

if __name__ == "__main__":
    audit_n8n()
