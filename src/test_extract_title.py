import unittest
from generate_page import extract_title
class TestTitleExtraction(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# My Title\n\nTest"
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")
    def test_no_title(self):
        md = "No title in this markdown"
        self.assertRaises(Exception, extract_title, md)
    def test_empty_markdown(self):
        md = ""
        self.assertRaises(Exception, extract_title, md)
    def test_multiple_titles(self):
        md = "# First Title\n# Second Title\nContent"
        title = extract_title(md)
        self.assertEqual(title, "First Title")
    def test_title_with_spaces_in_the_end(self):
        md = "# Title with spaces   \nContent"
        title = extract_title(md)
        self.assertEqual(title, "Title with spaces")