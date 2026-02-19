import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

connections = wf['connections']
nodes = {n['name']: n for n in wf['nodes']}

# Check critical connections
print("=== VERIFYING CONNECTIONS ===")
print()

# 1. Definir Prioridade -> Descobre Link Real
if 'Definir Prioridade' in connections:
    targets = [c['node'] for output in connections['Definir Prioridade'].get('main', []) for c in output]
    print(f"Definir Prioridade -> {targets}")
    if 'Descobre Link Real' in targets:
        print("  OK: Connects to Descobre Link Real")
    else:
        print("  MISSING: Should connect to Descobre Link Real!")
else:
    print("ERROR: Definir Prioridade has no connections!")

# 2. Descobre Link Real -> Extrai Link Real do Google
if 'Descobre Link Real' in connections:
    targets = [c['node'] for output in connections['Descobre Link Real'].get('main', []) for c in output]
    print(f"Descobre Link Real -> {targets}")
    if 'Extrai Link Real do Google' in targets:
        print("  OK: Connects to Extrai Link Real do Google")
    else:
        print("  MISSING: Should connect to Extrai Link Real do Google!")
else:
    print("ERROR: Descobre Link Real has no connections!")

# 3. Job Succeeded? -> Publica Multi (true branch)
if 'Job Succeeded?' in connections:
    outputs = connections['Job Succeeded?'].get('main', [[], []])
    true_targets = [c['node'] for c in outputs[0]] if len(outputs) > 0 else []
    false_targets = [c['node'] for c in outputs[1]] if len(outputs) > 1 else []
    print(f"Job Succeeded? (true) -> {true_targets}")
    print(f"Job Succeeded? (false) -> {false_targets}")
    if 'Publica Multi' in true_targets:
        print("  OK: True branch connects to Publica Multi")
    else:
        print("  MISSING: True branch should connect to Publica Multi!")
else:
    print("ERROR: Job Succeeded? has no connections!")

# 4. Mark Timeout -> Filtra Ligas (Telegram)
if 'Mark Timeout' in connections:
    targets = [c['node'] for output in connections['Mark Timeout'].get('main', []) for c in output]
    print(f"Mark Timeout -> {targets}")
    if 'Filtra Ligas (Telegram)' in targets:
        print("  OK: Connects to Filtra Ligas (Telegram)")
    else:
        print("  MISSING: Should connect to Filtra Ligas (Telegram)!")
else:
    print("ERROR: Mark Timeout has no connections!")

print()
print("=== CHECKING FOR DISCONNECTED NODES ===")
targets = set()
for src, conns in connections.items():
    for output_list in conns.get('main', []):
        for c in output_list:
            targets.add(c['node'])

sources = set(connections.keys())
all_nodes = set(nodes.keys())
no_incoming = all_nodes - targets

for n in sorted(no_incoming):
    if n == 'Cron (10min)':
        print(f"  {n} - OK (entry point)")
    else:
        print(f"  {n} - DISCONNECTED (no incoming)")