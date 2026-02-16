
import sys
import os
from datetime import datetime, timedelta, timezone

# Add /app to python path to find 'app' package
sys.path.append("/app")

try:
    from app.config import settings
    import psycopg2
    from psycopg2.extras import RealDictCursor
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def reset_stuck_jobs():
    print(f"Connecting to DB: {settings.DATABASE_URL}")
    try:
        conn = psycopg2.connect(settings.DATABASE_URL, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        
        # 1. Find stuck jobs (Pending > 1 hour)
        # Using raw SQL with interval. Assuming postgres timezone handling matches.
        query_find = """
            SELECT id, created_at FROM video_jobs 
            WHERE status = 'pending' 
            AND created_at < NOW() - INTERVAL '1 hour'
        """
        cur.execute(query_find)
        rows = cur.fetchall()
        
        print(f"Found {len(rows)} stuck jobs.")
        
        for row in rows:
            job_id = row['id']
            print(f"Deleting stuck job: {job_id} (Created: {row['created_at']})")
            
            # 2. Delete the job
            cur.execute("DELETE FROM video_jobs WHERE id = %s", (job_id,))
            
        conn.commit()
        print("Cleanup complete.")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error resetting jobs: {e}")

if __name__ == "__main__":
    reset_stuck_jobs()
