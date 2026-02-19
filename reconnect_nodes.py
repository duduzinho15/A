import json
import shutil

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

connections = wf['connections']

print("=== RECONNECTING DISCONNECTED NODES ===")
print()

# -------------------------------------------------------
# FIX 1: Definir Prioridade -> Descobre Link Real (instead of directly to Leitor Trafilatura)
# The correct chain is: Definir Prioridade -> Descobre Link Real -> Extrai Link Real do Google -> Leitor Trafilatura
# -------------------------------------------------------
print("[FIX 1] Definir Prioridade -> Descobre Link Real")
connections['Definir Prioridade'] = {
    "main": [
        [
            {
                "node": "Descobre Link Real",
                "type": "main",
                "index": 0
            }
        ]
    ]
}
print("  -> Done")

# -------------------------------------------------------
# FIX 2: Descobre Link Real -> Extrai Link Real do Google
# -------------------------------------------------------
print("[FIX 2] Descobre Link Real -> Extrai Link Real do Google")
connections['Descobre Link Real'] = {
    "main": [
        [
            {
                "node": "Extrai Link Real do Google",
                "type": "main",
                "index": 0
            }
        ]
    ]
}
print("  -> Done")

# -------------------------------------------------------
# FIX 3: Job Succeeded? output[0] (TRUE branch) -> Publica Multi
# Currently: output[0] = [] (empty), output[1] -> Mark Job Failed
# Should be: output[0] -> Publica Multi, output[1] -> Mark Job Failed
# -------------------------------------------------------
print("[FIX 3] Job Succeeded? (true branch) -> Publica Multi")
connections['Job Succeeded?'] = {
    "main": [
        [
            {
                "node": "Publica Multi",
                "type": "main",
                "index": 0
            }
        ],
        [
            {
                "node": "Mark Job Failed",
                "type": "main",
                "index": 0
            }
        ]
    ]
}
print("  -> Done")

# -------------------------------------------------------
# FIX 4: Mark Timeout -> Filtra Ligas (Telegram)
# After a timeout, we still want to notify via Telegram
# -------------------------------------------------------
print("[FIX 4] Mark Timeout -> Filtra Ligas (Telegram)")
connections['Mark Timeout'] = {
    "main": [
        [
            {
                "node": "Filtra Ligas (Telegram)",
                "type": "main",
                "index": 0
            }
        ]
    ]
}
print("  -> Done")

# -------------------------------------------------------
# FIX 5: Remove the broken reference to 'Próximos Jogos (Free)' from Merge Suggest
# This node doesn't exist in the workflow
# -------------------------------------------------------
print("[FIX 5] Remove broken reference to 'Próximos Jogos (Free)' from Merge Suggest")
if 'Merge Suggest' in connections:
    for output_list in connections['Merge Suggest'].get('main', []):
        to_remove = [c for c in output_list if c['node'] == 'Próximos Jogos (Free)']
        for c in to_remove:
            output_list.remove(c)
            print(f"  -> Removed reference to 'Próximos Jogos (Free)'")
print("  -> Done")

# Save backup and write fixed workflow
shutil.copy('workflow_producao_v9.json', 'workflow_producao_v9.bak2.json')
with open('workflow_producao_v9.json', 'w', encoding='utf-8') as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print()
print("=== VERIFICATION ===")
with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf2 = json.load(f)

connections2 = wf2['connections']
nodes2 = {n['name']: n for n in wf2['nodes']}

targets2 = set()
for src, outputs in connections2.items():
    for output_list in outputs.get('main', []):
        for conn in output_list:
            targets2.add(conn['node'])

sources2 = set(connections2.keys())
all_node_names2 = set(nodes2.keys())

print()
print("Nodes with no incoming (should only be entry points like Cron):")
no_incoming2 = all_node_names2 - targets2
for n in sorted(no_incoming2):
    has_outgoing = n in sources2
    print(f"  {'[HAS OUTGOING - OK entry point]' if has_outgoing else '[ISOLATED - PROBLEM]'} {n}")

print()
print("Broken references (target not in nodes):")
found_broken = False
for src, outputs in connections2.items():
    for output_list in outputs.get('main', []):
        for conn in output_list:
            if conn['node'] not in nodes2:
                print(f"  {src} -> {conn['node']} (MISSING NODE)")
                found_broken = True
if not found_broken:
    print("  None! All connections reference valid nodes.")

print()
print("Status of previously disconnected nodes:")
disconnected_mentioned = [
    'Publica Multi', 'If TikTok Error', 'Notifica Telegram Manual Post', 
    'Update DB Final', 'Descobre Link Real', 'Filtra Ligas (Telegram)', 
    'Envio Telegram Gols', 'Log Execution'
]
for n in disconnected_mentioned:
    has_in = n in targets2
    has_out = n in sources2
    status = "OK" if (has_in or n == 'Cron (10min)') else "STILL DISCONNECTED"
    print(f"  [{status}] {n}: has_incoming={has_in}, has_outgoing={has_out}")

print()
print("Workflow saved to workflow_producao_v9.json (backup: workflow_producao_v9.bak2.json)")
