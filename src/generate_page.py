import os
from markdown_blocks import markdown_to_html_node, extract_title
def generate_page(from_path, template_path, dest_path):
    print(f"Using {template_path}, generating a page from {from_path} to {dest_path}")

    with open(from_path, 'r') as f:
        source_content = f.read()
    with open(template_path, 'r') as f:
        template_content = f.read()

    source_html = markdown_to_html_node(source_content).to_html()

    source_title = extract_title(source_content)
    template_content = template_content.replace("{{ Title }}", source_title)
    template_content = template_content.replace("{{ Content }}",  source_html)


    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(template_content)


    