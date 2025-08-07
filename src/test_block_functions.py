import unittest

from inline_functions import *
from block_functions import *

class TestFunctions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks_multiple_newlines(self):
        md = """
This is **bolded** paragraph 




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line 




- This is a list
- with items 
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks_extra_spaces(self):
        md = """
This is **bolded** paragraph      




    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line    




- This is a list
- with items    
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type_ordered_list(self):
        md = """
1. This is an
2. ordered list
3. of three items
"""
        block = markdown_to_blocks(md)
        self.assertEqual(block_to_block_type(block[0]), BlockType.ORDERED_LIST)
    def test_block_to_block_type_unordered_list(self):
        md = """
- This is an 
- unordered list
- of three items
"""
        block = markdown_to_blocks(md)
        self.assertEqual(block_to_block_type(block[0]), BlockType.UNORDERED_LIST)
    def test_block_to_block_type_heading(self):
        md = """
# This is a heading

## This is also a header

### This is also a header

#### This is also a header

##### This is also a header

###### This is also a header

####### This is not a header
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            if block == blocks[-1]:

                self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
            else:
                self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_block_to_block_type_quote(self):
        md = """
>This is the first part of a quote
>This is the second part of a quote
>This is the third part of a quote

>This is the first part of a second quote
>This is the second part of a second quote
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_block_to_block_type_code(self):
        md = """
```This is a code text block```

```
this is another code text block but with a newline at the start and the end
```
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_block_to_block_type_all(self):
        md = """
This is a regular markdown paragraph block.

### This is a header block.

``` This is a code text block ```

>This is a quote text block
>more text on the same quote block

- This
- is
- an
- unordered
- list

1. This is
2. an
3. ordered
4. list
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[1]), BlockType.HEADING)
        self.assertEqual(block_to_block_type(blocks[2]), BlockType.CODE)
        self.assertEqual(block_to_block_type(blocks[3]), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(blocks[4]), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(blocks[5]), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()