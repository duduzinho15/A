
import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

print("--- All connection source nodes ---")
keys = list(wf['connections'].keys())
keys.sort()
for k in keys:
    print(k)
