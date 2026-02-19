import json

with open('workflow_producao_v9.json', 'r', encoding='utf-8') as f:
    wf = json.load(f)

connections = wf['connections']

print("=== LOOKING FOR POTENTIAL LOOPS ===")
print()

# Build adjacency list
graph = {}
for src, conns in connections.items():
    targets = []
    for output_list in conns.get('main', []):
        for c in output_list:
            targets.append(c['node'])
    graph[src] = targets

# Check the job polling cycle
print("=== JOB POLLING CYCLE ===")
print(f"Wait for Job -> {graph.get('Wait for Job', [])}")
print(f"Check Job Status -> {graph.get('Check Job Status', [])}")
print(f"Increment Attempts -> {graph.get('Increment Attempts', [])}")
print(f"Job Finished? -> {graph.get('Job Finished?', [])}")
print(f"Is Timeout? -> {graph.get('Is Timeout?', [])}")
print(f"Job Succeeded? -> {graph.get('Job Succeeded?', [])}")
print()

# Check if there's a back-edge creating a loop
print("=== CHECKING FOR BACK-EDGES ===")
# Wait for Job should go to Check Job Status
# Check Job Status should go to Increment Attempts
# Increment Attempts should go to Job Finished?
# Job Finished? has two outputs: true (continue) and false (loop back)
# The false branch (not finished) should go back to Wait for Job

jf_outputs = graph.get('Job Finished?', [])
print(f"Job Finished? outputs: {jf_outputs}")

# Let's trace the full loop path
print()
print("=== TRACING FULL PATH FROM Gera Vídeo Híbrido ===")
visited = set()
path = ['Gera Vídeo Híbrido']

def trace(node, depth=0):
    if depth > 20:
        return
    if node in visited:
        print(f"{'  '*depth}[LOOP DETECTED] -> {node}")
        return
    visited.add(node)
    targets = graph.get(node, [])
    for t in targets:
        print(f"{'  '*depth}{node} -> {t}")
        trace(t, depth + 1)

trace('Gera Vídeo Híbrido')