from htmlnode import *
from textnode import *
from inline_functions import *
from block_functions import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            html_blocks.append(paragraph_to_html_node(block))
        elif block_type == BlockType.HEADING:
            html_blocks.append(heading_to_html_node(block))
        elif block_type == BlockType.CODE:
            html_blocks.append(code_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            html_blocks.append(quote_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            html_blocks.append(unordered_list_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            html_blocks.append(ordered_list_to_html_node(block))
    return ParentNode("div", children=html_blocks)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def paragraph_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children=children)
def heading_to_html_node(block):
    space_index = block.find(" ")
    level = block[:space_index].count("#")
    text = block[space_index+1:].strip()
    tag = f"h{level}"
    children = text_to_children(text)
    return ParentNode(tag, children=children)
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block format")
    lines = block.split("\n")
    code_lines = lines[1:-1]
    code_text = "\n".join(code_lines) + "\n"
    code_text_node = TextNode(code_text, TextType.TEXT)
    code_node = text_node_to_html_node(code_text_node)
    code = ParentNode("code", children=[code_node])
    return ParentNode("pre", children=[code])
def quote_to_html_node(block):
    lines = block.split("\n")
    formatted_lines = []
    for line in lines:
        if line.startswith("> "):
            line = line[2:]
            formatted_lines.append(line)
        elif line.startswith(">"):
            formatted_lines.append("")
    text = "\n".join(formatted_lines)
    quote_nodes = text_to_children(text)
    return ParentNode("blockquote", children=quote_nodes)
def unordered_list_to_html_node(block):
    items = block.split("\n")
    for item in items:
        if item.startswith("- "):
            item = item[2:]
    children_item_nodes = [text_to_children(item) for item in items]
    item_nodes = [ParentNode("li", children=children_item_node) for children_item_node in children_item_nodes]
    return ParentNode("ul", children=item_nodes)
def ordered_list_to_html_node(block):
    items = block.split("\n")
    i = 1
    stripped_items = []
    for item in items:
        prefix = f"{i}. "
        if item.startswith(prefix):
            item = item[len(prefix):].strip()
            stripped_items.append(item)
        i += 1
    children_item_nodes = [text_to_children(item) for item in stripped_items]
    item_nodes = [ParentNode("li", children=children_item_node) for children_item_node in children_item_nodes]
    return ParentNode("ol", children=item_nodes)
