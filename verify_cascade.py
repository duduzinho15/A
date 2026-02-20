
import json

WF_PATH = 'workflow_producao_v9.json'

with open(WF_PATH, 'r', encoding='utf-8') as f:
    wf = json.load(f)

def verify_cascade(name, nodes):
    print(f"--- Verifying {name} Cascade ---")
    errors = []
    for i in range(len(nodes) - 1):
        src = nodes[i]
        target = nodes[i+1]
        
        if src not in wf['connections']:
            errors.append(f"Source node '{src}' has NO connections.")
            continue
            
        conns = wf['connections'][src]['main'][0]
        found = False
        for c in conns:
            if c['node'] == target:
                found = True
                break
        
        if not found:
            errors.append(f"Connection from '{src}' to '{target}' NOT found.")
            
        # For sequential, most should have only 1 target except special cases
        if src != "Gaveta VIP (Embeds)" and len(conns) > 1:
            errors.append(f"Node '{src}' has multiple connections (Fan-out) in a pure sequential cascade: {[c['node'] for c in conns]}")
            
    if errors:
        for e in errors: print(f"ERROR: {e}")
        return False
    print(f"SUCCESS: {name} cascade is correct.")
    return True

enrich_cascade = ["Merge Suggest", "ScoreBat (Python)", "TheSportsDB", "Social Scraper (Python)", "Transfermarkt (Python)", "Merge Contexto Roteiro"]
asset_cascade = [
    "Broadcast Hub", "Serper Search", "Brave Images", "Brave Web", "Brave News", 
    "Brave Videos", "Serper.dev (Images)", "Gaveta VIP (Embeds)", "Serper News", 
    "Serper Videos", "Tavily AI", "Pexels API", "Pixabay API", "SearXNG", 
    "IA Metadata", "Merge Assets"
]

v1 = verify_cascade("Enrichment", enrich_cascade)
v2 = verify_cascade("Asset", asset_cascade)

# Check Gaveta VIP secondary connection
gaveta_conns = [c['node'] for c in wf['connections']['Gaveta VIP (Embeds)']['main'][0]]
if "Filtra Ligas (Telegram)" in gaveta_conns:
    print("SUCCESS: Gaveta VIP still points to Telegram.")
else:
    print("ERROR: Gaveta VIP lost connection to Telegram.")

# Check Agrupador Code
agrupador = next(n for n in wf['nodes'] if n['name'] == "Agrupador Master Assets")
if ".first()" in agrupador['parameters']['jsCode']:
    print("SUCCESS: Agrupador Master Assets uses $().first() logic.")
else:
    print("ERROR: Agrupador Master Assets uses old logic.")

if v1 and v2:
    exit(0)
else:
    exit(1)
