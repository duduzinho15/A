
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
        
        # 1. Find and update stuck jobs (Processing or Pending > 1 hour)
        query_update = """
            UPDATE video_jobs 
            SET status = 'error', 
                error_message = 'Job marked as stuck (stalled in processing/pending for > 1h)', 
                updated_at = NOW()
            WHERE status IN ('processing', 'pending') 
            AND (
                (updated_at IS NOT NULL AND updated_at < NOW() - INTERVAL '1 hour')
                OR 
                (updated_at IS NULL AND created_at < NOW() - INTERVAL '1 hour')
            )
            RETURNING id
        """
        cur.execute(query_update)
        rows = cur.fetchall()
        
        print(f"Updated {len(rows)} stuck jobs to 'error' status.")
        for row in rows:
            print(f" - Job {row['id']} marked as error.")
            
        conn.commit()
        print("Cleanup complete.")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error resetting jobs: {e}")

if __name__ == "__main__":
    reset_stuck_jobs()
