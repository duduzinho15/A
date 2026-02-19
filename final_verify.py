import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

# Check IA Roteiro Master
for node in wf['nodes']:
    if node['name'] == 'IA Roteiro Master':
        body = node['parameters']['jsonBody']
        if 'ximos Jogos' in body or 'Próximos Jogos' in body:
            print('ERROR: Próximos Jogos still present')
        else:
            print('OK: IA Roteiro Master is clean')
        break

# Validate JSON structure
num_nodes = len(wf['nodes'])
num_conns = len(wf['connections'])
print(f'Valid JSON: {num_nodes} nodes, {num_conns} connection sources')

# Check for any remaining broken node references
nodes_set = set(n['name'] for n in wf['nodes'])
broken = []
for src, conns in wf['connections'].items():
    for output_list in conns.get('main', []):
        for c in output_list:
            if c['node'] not in nodes_set:
                broken.append(f'{src} -> {c["node"]}')
if broken:
    print('Broken references:', broken)
else:
    print('No broken node references')

# Search all nodes for any remaining references to 'Próximos Jogos'
print()
print('Searching all nodes for Próximos Jogos references...')
found_any = False
for node in wf['nodes']:
    node_str = json.dumps(node, ensure_ascii=False)
    if 'ximos Jogos' in node_str or 'Próximos Jogos' in node_str:
        print(f'  Found in node: {node["name"]}')
        found_any = True
if not found_any:
    print('  None found! Workflow is clean.')