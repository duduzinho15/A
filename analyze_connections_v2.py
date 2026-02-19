
import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

nodes_by_id = {node['id']: node['name'] for node in wf['nodes']}

print("--- Connections in workflow_producao_v9.json ---")
for src_name, connections in wf['connections'].items():
    for type_name, branches in connections.items():
        for i, branch in enumerate(branches):
            for target in branch:
                print(f"[{src_name}] Branch {i} -> [{target['node']}]")

print("\n--- Searching for 'Wait for Job' incoming connections ---")
for src_name, connections in wf['connections'].items():
    for type_name, branches in connections.items():
        for i, branch in enumerate(branches):
            for target in branch:
                if target['node'] == 'Wait for Job':
                    print(f"target 'Wait for Job' from '{src_name}' (Branch {i})")

print("\n--- 'Mark Job Failed' details ---")
if 'Mark Job Failed' in wf['connections']:
    print(json.dumps(wf['connections']['Mark Job Failed'], indent=2))
else:
    print("'Mark Job Failed' has NO outgoing connections.")

print("\n--- Check Job Status Node Details ---")
for node in wf['nodes']:
    if node['name'] == 'Check Job Status':
        print(json.dumps(node.get('parameters', {}).get('options', {}), indent=2))
