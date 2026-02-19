import json
import shutil

# Step 1: Get the complete jsCode from bak.json
with open('workflow_producao_v9.bak.json', 'r', encoding='utf-8') as f:
    bak_wf = json.load(f)

complete_jsCode = None
for node in bak_wf['nodes']:
    if node['name'] == 'Agrupador Master Assets':
        complete_jsCode = node['parameters'].get('jsCode')
        print(f"Found complete jsCode in bak.json (len={len(complete_jsCode)})")
        break

if not complete_jsCode:
    print("ERROR: Could not find complete jsCode!")
    exit(1)

# Step 2: Read current workflow
with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

# Step 3: Replace the truncated jsCode
for node in wf['nodes']:
    if node['name'] == 'Agrupador Master Assets':
        old_len = len(node['parameters'].get('jsCode', ''))
        node['parameters']['jsCode'] = complete_jsCode
        print(f"Replaced jsCode: {old_len} -> {len(complete_jsCode)} chars")
        break

# Step 4: Fix the IA Roteiro Master expression (remove Próximos Jogos reference)
for node in wf['nodes']:
    if node['name'] == 'IA Roteiro Master':
        body = node['parameters']['jsonBody']
        if 'ximos Jogos' in body:
            # Find and remove the block
            idx = body.find('ximos Jogos (Free)").isExecuted')
            if idx != -1:
                start = body.rfind(' + ($(', 0, idx)
                end_marker = ": '')"
                end = body.find(end_marker, idx)
                if end != -1:
                    end += len(end_marker)
                    new_body = body[:start] + body[end:]
                    node['parameters']['jsonBody'] = new_body
                    print(f"Fixed IA Roteiro Master: removed Próximos Jogos reference")
        break

# Step 5: Save
shutil.copy('workflow_producao_v9.json', 'workflow_producao_v9.bak5.json')
with open('workflow_producao_v9.json', 'w', encoding='utf-8') as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Saved workflow_producao_v9.json")

# Step 6: Verify
with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf2 = json.load(f)

for node in wf2['nodes']:
    if node['name'] == 'Agrupador Master Assets':
        code = node['parameters'].get('jsCode', '')
        if '[truncated]' in code:
            print("ERROR: Agrupador Master Assets still truncated!")
        else:
            print(f"OK: Agrupador Master Assets complete (len={len(code)})")
    if node['name'] == 'IA Roteiro Master':
        body = node['parameters']['jsonBody']
        if 'ximos Jogos' in body:
            print("ERROR: IA Roteiro Master still has Próximos Jogos!")
        else:
            print("OK: IA Roteiro Master clean")