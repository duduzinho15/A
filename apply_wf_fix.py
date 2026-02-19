
import json

WF_PATH = 'workflow_producao_v9.json'

with open(WF_PATH, 'r', encoding='utf-8') as f:
    wf = json.load(f)

# 1. Fix "Job Finished?" Node Parameters
for node in wf['nodes']:
    if node['name'] == 'Job Finished?':
        if 'parameters' not in node: node['parameters'] = {}
        # Ensure OR logic
        node['parameters']['combinator'] = 'any'
        # Fix condition logic if needed (it had status != processing AND attempts >= 20)
        # We want (status != processing) OR (attempts >= 20)
        print("Updated 'Job Finished?' parameters.")
        break

# 2. Fix Connections
# "Job Finished?" (Index 0 is True, Index 1 is False)
# Output 0 (True) -> Is Timeout?
# Output 1 (False) -> Wait for Job

if 'Job Finished?' in wf['connections']:
    wf['connections']['Job Finished?']['main'] = [
        [ # Output 0: True
            {
                "node": "Is Timeout?",
                "type": "main",
                "index": 0
            }
        ],
        [ # Output 1: False
            {
                "node": "Wait for Job",
                "type": "main",
                "index": 0
            }
        ]
    ]
    print("Fixed 'Job Finished?' connections.")

# "Is Timeout?" (Index 0 is True, Index 1 is False)
# Output 0 (True) -> Mark Timeout
# Output 1 (False) -> Job Succeeded?

if 'Is Timeout?' in wf['connections']:
    wf['connections']['Is Timeout?']['main'] = [
        [ # Output 0: True
            {
                "node": "Mark Timeout",
                "type": "main",
                "index": 0
            }
        ],
        [ # Output 1: False
            {
                "node": "Job Succeeded?",
                "type": "main",
                "index": 0
            }
        ]
    ]
    print("Fixed 'Is Timeout?' connections.")

# Save
with open(WF_PATH, 'w', encoding='utf-8') as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Workflow v9 fixed successfully.")
