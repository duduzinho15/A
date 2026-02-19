
import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

print("--- Analyzing connections pointing to 'Wait for Job' ---")
for node_name, conn in wf['connections'].items():
    for branch in conn['main']:
        for target in branch:
            if target['node'] == 'Wait for Job':
                print(f"Node '{node_name}' points to 'Wait for Job'")

print("\n--- Analyzing outgoing connections from 'Mark Job Failed' ---")
if 'Mark Job Failed' in wf['connections']:
    print(wf['connections']['Mark Job Failed'])
else:
    print("'Mark Job Failed' has NO outgoing connections in this JSON.")

print("\n--- Analyzing 'Job Succeeded?' branches ---")
if 'Job Succeeded?' in wf['connections']:
    print(json.dumps(wf['connections']['Job Succeeded?'], indent=2))
