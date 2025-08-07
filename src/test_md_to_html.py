import unittest
from md_to_html_functions import *

class TestFunctions(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

#     def test_codeblock_with_empty_start_and_end(self):
#         md = """
# ```

# some code
# more code

# ```
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><pre><code>\nsome code\nmore code\n</code></pre></div>"
#         )

    def test_quote_with_nested_newlines(self):
        md = """
> This is a quote
>
> with an empty line in the middle
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><blockquote>This is a quote\n\nwith an empty line in the middle</blockquote></div>"
        )
    def test_ordered_list_with_extra_spaces(self):
        md = """
1.   First item
2.      Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
        )
    def test_heading_with_extra_spaces(self):
        md = """
##               Several spaces in heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Several spaces in heading</h2></div>"
        )


if __name__ == "__main__":
    unittest.main()