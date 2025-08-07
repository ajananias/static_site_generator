import os
from md_to_html_functions import *

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown_content = f.read()
    with open(template_path, 'r') as g:
        template_content = g.read()
    
    html_string = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    html_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    with open(dest_path, 'w') as h:
        h.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    directories = os.listdir(dir_path_content)
    for item in directories:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, os.path.join(dest_dir_path, item))
        elif item.endswith(".md"):
            dest_path = os.path.join(dest_dir_path, item[:-3] + ".html")
            generate_page(item_path, template_path, dest_path)
