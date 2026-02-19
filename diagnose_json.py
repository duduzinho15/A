import json

# disconnected_nodes.json - look at raw bytes around the error
with open('disconnected_nodes.json', 'rb') as f:
    raw = f.read()
print('Raw bytes around char 60-110:')
print(repr(raw[60:110]))
print()

# workflow_apostas_v1.json - try different encodings
for enc in ['latin-1', 'cp1252', 'utf-8-sig']:
    try:
        with open('workflow_apostas_v1.json', 'r', encoding=enc) as f:
            content = f.read()
        json.loads(content)
        print(f'workflow_apostas_v1.json: VALID with {enc}')
        break
    except json.JSONDecodeError as e:
        print(f'workflow_apostas_v1.json {enc} JSON ERROR: {e}')
    except Exception as e:
        print(f'workflow_apostas_v1.json {enc} ERROR: {e}')

# Show the area around the error in workflow_apostas_v1.json
with open('workflow_apostas_v1.json', 'rb') as f:
    raw2 = f.read()
print()
print('workflow_apostas_v1.json bytes around 8380-8395:')
print(repr(raw2[8375:8400]))
