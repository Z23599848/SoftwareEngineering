import re
import os

def sync_diagrams():
    readme_path = 'report/README.md'
    diagrams_dir = 'design/diagrams'
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Mapping of tags to source files
    mappings = {
        'CLASS_DIAGRAM': 'classDiagram.md',
        'SEQUENCE_DIAGRAM': 'sequenceDiagram.md',
        'ER_DIAGRAM': 'edr_diagram.md'
    }
    
    for tag, filename in mappings.items():
        source_path = os.path.join(diagrams_dir, filename)
        if not os.path.exists(source_path):
            print(f"Warning: {source_path} not found.")
            continue
            
        with open(source_path, 'r') as f:
            source_content = f.read()
            
        # Extract the mermaid block from source
        mermaid_match = re.search(r'```mermaid.*?```', source_content, re.DOTALL)
        if mermaid_match:
            new_mermaid = mermaid_match.group(0)
            
            # Replace in README
            pattern = re.compile(f'<!-- START_{tag} -->.*?<!-- END_{tag} -->', re.DOTALL)
            content = pattern.sub(f'<!-- START_{tag} -->\n{new_mermaid}\n<!-- END_{tag} -->', content)
            print(f"Synced {tag} from {filename}")
        else:
            print(f"Warning: No mermaid block found in {filename}")

    with open(readme_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    sync_diagrams()
