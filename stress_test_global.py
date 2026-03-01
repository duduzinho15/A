import requests
import json
import time
import concurrent.futures

BASE_URL = "http://localhost:8000"

def log_test(name, response):
    status = response.status_code
    try:
        data = response.json()
    except:
        data = "No JSON response"
    print(f"[TEST: {name}] Status: {status} | Data: {data}")

def test_maintenance():
    # Idea #1 & #8 & #10 (Heal/Cleanup)
    print("Triggering Maintenance/Heal...")
    r = requests.post(f"{BASE_URL}/maintenance/heal")
    log_test("Maintenance Heal", r)

def test_ai_seo():
    # Idea #7 (SEO Optimization)
    print("Triggering SEO Metadata Stress...")
    payload = {
        "text": "Top soccer trends and betting strategies for 2026",
        "style": "viral",
        "social_context": True
    }
    r = requests.post(f"{BASE_URL}/ai/metadata", json=payload)
    log_test("SEO AI Metadata", r)

def test_openhands_tasks():
    # Idea #4, #5, #2, #3, #6, #8, #10
    tasks = [
        {"endpoint": "/openhands/auto-docs", "payload": {}},
        {"endpoint": "/openhands/security-scan", "payload": {}},
        {"endpoint": "/openhands/generate-scraper", "payload": {"url": "https://news.google.com", "target_fields": ["title", "link"]}},
        {"endpoint": "/openhands/infra-task", "payload": {"action_description": "Verify docker-compose health check configurations", "target_files": ["docker-compose.yml"]}},
    ]
    
    for task in tasks:
        print(f"Triggering {task['endpoint']}...")
        r = requests.post(f"{BASE_URL}{task['endpoint']}", json=task['payload'])
        log_test(task['endpoint'], r)

def test_datasets():
    # Idea #9 (Dataset Manager)
    print("Triggering Dataset Export...")
    r = requests.get(f"{BASE_URL}/datasets/export?min_ctr=0.1")
    log_test("Dataset Export", r)

def run_stress_test():
    print("--- STARTING GLOBAL STRESS TEST (10 IDEAS) ---")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(test_maintenance),
            executor.submit(test_ai_seo),
            executor.submit(test_openhands_tasks),
            executor.submit(test_datasets),
        ]
        concurrent.futures.wait(futures)

    print("--- STRESS TEST DISPATCHED ---")
    print("Check logs: docker logs -f python_service")
    print("Check health: curl http://localhost:8000/maintenance/health")

if __name__ == "__main__":
    run_stress_test()
