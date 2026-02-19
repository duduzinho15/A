
import json
import os

def add_nodes_to_workflow(main_workflow_path, new_nodes_path, output_workflow_path):
    """
    Adds nodes and connections from a new file to a main workflow file.

    Args:
        main_workflow_path (str): Path to the main n8n workflow JSON file.
        new_nodes_path (str): Path to the JSON file containing new nodes and connections.
        output_workflow_path (str): Path to save the updated workflow.
    """
    try:
        with open(main_workflow_path, 'r', encoding='utf-8') as f:
            main_workflow = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading main workflow file '{main_workflow_path}': {e}")
        return

    try:
        with open(new_nodes_path, 'r', encoding='utf-8') as f:
            new_content = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading new nodes file '{new_nodes_path}': {e}")
        return

    if 'nodes' not in main_workflow:
        main_workflow['nodes'] = []
    if 'connections' not in main_workflow:
        main_workflow['connections'] = {}

    new_nodes = new_content.get('nodes', [])
    new_connections = new_content.get('connections', {})

    existing_node_ids = {node['id'] for node in main_workflow['nodes']}
    nodes_to_add = [node for node in new_nodes if node['id'] not in existing_node_ids]

    main_workflow['nodes'].extend(nodes_to_add)
    main_workflow['connections'].update(new_connections)

    try:
        with open(output_workflow_path, 'w', encoding='utf-8') as f:
            json.dump(main_workflow, f, indent=2, ensure_ascii=False)
        print(f"Successfully added {len(nodes_to_add)} new nodes and updated connections in '{output_workflow_path}'")
    except IOError as e:
        print(f"Error writing updated workflow file: {e}")

if __name__ == '__main__':
    # Using relative paths for better portability
    main_workflow_file = 'workflow_producao_v9.json'
    new_nodes_file = 'disconnected_nodes.json'
    
    # Overwriting the original file
    add_nodes_to_workflow(main_workflow_file, new_nodes_file, main_workflow_file)
