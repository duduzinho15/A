import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

nodes = {n['name']: n for n in wf['nodes']}
connections = wf['connections']

# Find all nodes that are targets (have something connecting TO them)
targets = set()
for src, outputs in connections.items():
    for output_list in outputs.get('main', []):
        for conn in output_list:
            targets.add(conn['node'])

# Find all nodes that are sources (have something connecting FROM them)
sources = set(connections.keys())

all_node_names = set(nodes.keys())

print("=== NODES WITH NO INCOMING CONNECTION (potential entry points or disconnected) ===")
no_incoming = all_node_names - targets
for n in sorted(no_incoming):
    has_outgoing = n in sources
    print(f"  {'[HAS OUTGOING]' if has_outgoing else '[DEAD END - no outgoing either]'} {n}")

print()
print("=== NODES WITH NO OUTGOING CONNECTION (potential end points or disconnected) ===")
no_outgoing = all_node_names - sources
for n in sorted(no_outgoing):
    has_incoming = n in targets
    print(f"  {'[HAS INCOMING]' if has_incoming else '[ISOLATED - no incoming either]'} {n}")

print()
print("=== CONNECTIONS THAT REFERENCE NON-EXISTENT NODES ===")
for src, outputs in connections.items():
    if src not in nodes:
        print(f"  SOURCE not in nodes: {src}")
    for output_list in outputs.get('main', []):
        for conn in output_list:
            if conn['node'] not in nodes:
                print(f"  TARGET not in nodes: {conn['node']} (from {src})")

print()
print("=== SPECIFIC NODES MENTIONED AS DISCONNECTED ===")
disconnected_mentioned = [
    'Publica Multi', 'If TikTok Error', 'Notifica Telegram Manual Post', 
    'Update DB Final', 'Descobre Link Real', 'Filtra Ligas (Telegram)', 
    'Envio Telegram Gols', 'Log Execution'
]
for n in disconnected_mentioned:
    in_wf = n in nodes
    has_in = n in targets
    has_out = n in sources
    print(f"  {n}: in_workflow={in_wf}, has_incoming={has_in}, has_outgoing={has_out}")

print()
print("=== WHAT CONNECTS TO 'Descobre Link Real'? ===")
for src, outputs in connections.items():
    for output_list in outputs.get('main', []):
        for conn in output_list:
            if conn['node'] == 'Descobre Link Real':
                print(f"  {src} -> Descobre Link Real")

print()
print("=== WHAT CONNECTS TO 'Publica Multi'? ===")
for src, outputs in connections.items():
    for output_list in outputs.get('main', []):
        for conn in output_list:
            if conn['node'] == 'Publica Multi':
                print(f"  {src} -> Publica Multi")

print()
print("=== WHAT CONNECTS TO 'Filtra Ligas (Telegram)'? ===")
for src, outputs in connections.items():
    for output_list in outputs.get('main', []):
        for conn in output_list:
            if conn['node'] == 'Filtra Ligas (Telegram)':
                print(f"  {src} -> Filtra Ligas (Telegram)")

print()
print("=== Job Succeeded? connections ===")
if 'Job Succeeded?' in connections:
    print(json.dumps(connections['Job Succeeded?'], indent=2))

print()
print("=== Mark Timeout connections ===")
if 'Mark Timeout' in connections:
    print(json.dumps(connections['Mark Timeout'], indent=2))

print()
print("=== Definir Prioridade connections ===")
if 'Definir Prioridade' in connections:
    print(json.dumps(connections['Definir Prioridade'], indent=2))
