import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

print("Searching for '...' in all node expressions...")
print()

for node in wf['nodes']:
    node_str = json.dumps(node, ensure_ascii=False)
    if '...' in node_str:
        print(f"=== Found '...' in node: {node['name']} ===")
        # Find context around the ...
        idx = node_str.find('...')
        while idx != -1:
            print(f"Context: ...{repr(node_str[max(0,idx-50):idx+50])}...")
            idx = node_str.find('...', idx + 1)
        print()