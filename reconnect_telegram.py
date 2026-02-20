
import json

WF_PATH = 'workflow_producao_v9.json'

with open(WF_PATH, 'r', encoding='utf-8') as f:
    wf = json.load(f)

node_name = "Gaveta VIP (Embeds)"
target_node = "Filtra Ligas (Telegram)"

if node_name in wf['connections']:
    # Add new target to Branch 0 of main output
    wf['connections'][node_name]['main'][0].append({
        "node": target_node,
        "type": "main",
        "index": 0
    })
    print(f"Added connection from '{node_name}' to '{target_node}'")
else:
    print(f"Node '{node_name}' not found in connections.")

with open(WF_PATH, 'w', encoding='utf-8') as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print(json.dumps(wf['connections'][node_name], indent=2))
