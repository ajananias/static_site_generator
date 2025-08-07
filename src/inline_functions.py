import re
from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        section_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown Syntax")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                section_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                section_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(section_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        section_nodes = []
        images = extract_markdown_images(old_node.text)
        node_text = old_node.text
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown Syntax")
            if sections[0] != "":    
                section_nodes.append(TextNode(sections[0], TextType.TEXT))
            section_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = sections[1]
        if node_text != "":
            section_nodes.append(TextNode(node_text, TextType.TEXT))
        new_nodes.extend(section_nodes)
    return new_nodes
def split_nodes_link(old_nodes):
    new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        section_nodes = []
        links = extract_markdown_links(old_node.text)
        node_text = old_node.text
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown Syntax")
            if sections[0] != "":
                section_nodes.append(TextNode(sections[0], TextType.TEXT))
            section_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = sections[1]
        if node_text != "":
            section_nodes.append(TextNode(node_text, TextType.TEXT))
        new_nodes.extend(section_nodes)
    return new_nodes
            
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes