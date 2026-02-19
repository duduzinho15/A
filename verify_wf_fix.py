
import json

WF_PATH = 'workflow_producao_v9.json'

with open(WF_PATH, 'r', encoding='utf-8') as f:
    wf = json.load(f)

def check_connections():
    errors = []
    
    # Check Job Finished?
    conn = wf['connections'].get('Job Finished?', {})
    main = conn.get('main', [])
    if len(main) < 2:
        errors.append(f"'Job Finished?' should have 2 outputs, found {len(main)}")
    else:
        if main[0][0]['node'] != 'Is Timeout?':
            errors.append(f"'Job Finished?' Output 0 should be 'Is Timeout?', found {main[0][0]['node']}")
        if main[1][0]['node'] != 'Wait for Job':
            errors.append(f"'Job Finished?' Output 1 should be 'Wait for Job', found {main[1][0]['node']}")

    # Check Is Timeout?
    conn_timeout = wf['connections'].get('Is Timeout?', {})
    main_timeout = conn_timeout.get('main', [])
    if len(main_timeout) < 2:
        errors.append(f"'Is Timeout?' should have 2 outputs, found {len(main_timeout)}")
    else:
        if main_timeout[0][0]['node'] != 'Mark Timeout':
            errors.append(f"'Is Timeout?' Output 0 should be 'Mark Timeout', found {main_timeout[0][0]['node']}")
        if main_timeout[1][0]['node'] != 'Job Succeeded?':
            errors.append(f"'Is Timeout?' Output 1 should be 'Job Succeeded?', found {main_timeout[1][0]['node']}")

    for node in wf['nodes']:
        if node['name'] == 'Job Finished?':
            if node['parameters'].get('combinator') != 'any':
                errors.append(f"'Job Finished?' combinator should be 'any', found {node['parameters'].get('combinator')}")

    if errors:
        for err in errors: print(f"ERROR: {err}")
        return False
    
    print("VERIFICATION SUCCESS: Workflow connections and logic are correct.")
    return True

if __name__ == "__main__":
    if check_connections():
        exit(0)
    else:
        exit(1)
