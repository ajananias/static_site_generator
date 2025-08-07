from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    block_list = [block.strip() for block in block_list]
    for block in block_list:
        if not block:
            block_list.remove(block)
    return block_list

def block_to_block_type(block):
    split_block_lines = block.split("\n")
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if len(split_block_lines) > 0 and split_block_lines[0].startswith("```") and split_block_lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in split_block_lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in split_block_lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in split_block_lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    