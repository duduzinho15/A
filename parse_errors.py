import json
import re

def parse_n8n_errors(file_path):
    print(f"Parsing {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    for line in lines:
        if '|' not in line or 'executionId' in line or '----' in line:
            continue
        
        parts = line.split('|')
        if len(parts) < 2:
            continue
            
        exec_id = parts[0].strip()
        data_str = parts[1].strip()
        
        if not exec_id or not data_str:
            continue
            
        print(f"\n--- Execution ID: {exec_id} ---")
        try:
            # Clean up potential truncated JSON
            if data_str.endswith('...'):
                data_str = data_str[:-3]
            
            # If it's still not valid JSON, we might need more effort, but let's try
            data_json = json.loads(data_str)
            
            errors = []
            def find_errors(obj, path=""):
                if isinstance(obj, dict):
                    if 'error' in obj:
                        errors.append(f"{path} -> {obj['error']}")
                    if 'message' in obj and 'stack' in obj:
                         errors.append(f"{path} -> {obj['message']}")
                    for k, v in obj.items():
                        find_errors(v, f"{path}.{k}")
                elif isinstance(obj, list):
                    for i, item in enumerate(obj):
                        find_errors(item, f"{path}[{i}]")
            
            find_errors(data_json)
            if errors:
                for err in errors:
                    print(f"  [ERROR] {err}")
            else:
                print("  No specific error found in this JSON segment.")
                
        except json.JSONDecodeError:
            print(f"  [!] Invalid or truncated JSON. Raw excerpt: {data_str[:200]}...")
        except Exception as e:
            print(f"  [!] Error parsing row: {e}")

if __name__ == "__main__":
    parse_n8n_errors('n8n_errors.txt')
