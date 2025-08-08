import os
from pathlib import Path
from md_to_html_functions import *

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown_content = f.read()
    with open(template_path, 'r') as g:
        template_content = g.read()    
    html_node = markdown_to_html_node(markdown_content)
    html = html_node.to_html()
    title = extract_title(markdown_content)

    html_page = template_content.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html)
    html_page = html_page.replace('href="/', f'href="{basepath}')
    html_page = html_page.replace('src="/', f'src="{basepath}')
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as h:
        h.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(item_path, template_path, dest_path, basepath)
        elif os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, dest_path, basepath)
