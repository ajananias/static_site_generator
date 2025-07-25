import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "Hello, world!", ["Nala", "Suki"], {"class": "my-class"})
        expected_repr = "tag: h1, value: Hello, world!, children: ['Nala', 'Suki'], props: {'class': 'my-class'}"
        self.assertEqual(repr(node), expected_repr)

    def test_empty(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_only_tag(self):
        node = HTMLNode("div")
        self.assertEqual(node.tag, "div")
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
    
    def test_only_value(self):
        node = HTMLNode(value="Some text")
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, "Some text")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_only_children(self):
        node = HTMLNode(children=["Child1", "Child2"])
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, ["Child1", "Child2"])
        self.assertIsNone(node.props)
    
    def test_only_props(self):
        node = HTMLNode(props={"id": "main", "class": "container"})
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"id": "main", "class": "container"})

    def test_eq(self):
        node1 = HTMLNode("a", "Text", ["Child"], {"class": "text"})
        node2 = HTMLNode("a", "Text", ["Child"], {"class": "text"})
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode("a", "Text", ["Child"], {"class": "text"})
        node2 = HTMLNode("a", "Text", ["Child2"], {"class": "text"})
        node3 = HTMLNode("p", "Text", ["Child"], {"type": "text"})
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node2, node3)

    def test_props_to_html(self):
        node = HTMLNode(props={"id": "main", "class": "container"})
        expected_html = ' id="main" class="container"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_leaf_repr_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_q(self):
        node = LeafNode("q", "Hello, world!")
        self.assertEqual(node.to_html(), "<q>Hello, world!</q>")

    def test_leaf_to_html_without_tag(self):
        node = LeafNode(None, "!@#$Just text$#@!")
        self.assertEqual(node.to_html(), "!@#$Just text$#@!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_from_grandparent_to_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"class": "parent"})
        grandparent_node = ParentNode("section", [parent_node])
        self.assertEqual(
            grandparent_node.to_html(),
            '<section><div class="parent"><span><b>grandchild</b></span></div></section>',
        )

    
if __name__ == "__main__":
    unittest.main()