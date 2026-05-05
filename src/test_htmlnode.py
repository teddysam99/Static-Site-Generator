import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_equal(self):
        node  = HTMLNode("h1","testing string") 
        node2 = HTMLNode("h1","testing string") 
        self.assertEqual(node,node2)
    def test_not_equal(self):
        node  = HTMLNode("h1","testing string") 
        node2 = HTMLNode("a","testing string")
        self.assertNotEqual(node,node2)
    def test_children(self):
        child  = HTMLNode("h1","testing string") 
        child2 = HTMLNode("a","testing string") 
        child3 = HTMLNode("p","testing string")
        node = HTMLNode("h3","testing children",[child,child2,child3])
        node2= HTMLNode("h3","testing children",[child2,child3,child])
        self.assertNotEqual(node,node2)
    def test_props_to_html(self):
        node  = HTMLNode("a","testing string",None, {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')
    def test_props_to_html2(self):
        node = HTMLNode("h1","testing string")
        self.assertEqual(node.props_to_html(), '')
    def test_props_to_html3(self):
        node = HTMLNode("h3", "Youtube addiction", None, {"id": "1234"})
        self.assertEqual(node.props_to_html(), ' id="1234"')
    def test_props_to_html4(self):
        node = HTMLNode("h3", "Youtube addiction", None, {"notexist": "none"})
        self.assertEqual(node.props_to_html(), ' notexist="none"')
    def test_props_to_html5(self):
        node = HTMLNode("h3", "Youtube addiction", None, {})
        self.assertEqual(node.props_to_html(), '')
    def test_props_to_html6(self):
        node = HTMLNode("h1", "", None, {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6'})
        self.assertEqual(node.props_to_html(), ' a="1" b="2" c="3" d="4" e="5" f="6"')
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_props(self):
        node = LeafNode("p","Hello world!", {"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f",})
        self.assertEqual(node.to_html(),'<p 1="a" 2="b" 3="c" 4="d" 5="e" 6="f">Hello world!</p>')
    def test_leaf_to_html_tags(self):
        node = LeafNode("@@@", "Hello, world!")
        self.assertEqual(node.to_html(), "<@@@>Hello, world!</@@@>")
    def test_to_html_with_children(self):
        child_node = LeafNode("p", "Hello world")
        parent_node = ParentNode("h1",[child_node])
        self.assertEqual(parent_node.to_html(), "<h1><p>Hello world</p></h1>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("3", "Goodbye world")
        child_node = ParentNode("2", [grandchild_node])
        parent_node = ParentNode("1", [child_node])
        self.assertEqual(parent_node.to_html(),"<1><2><3>Goodbye world</3></2></1>")
    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("p", "Hello world", {"1":"a","2":"b"})
        parent_node = ParentNode("h1",[child_node])
        self.assertEqual(parent_node.to_html(), '<h1><p 1="a" 2="b">Hello world</p></h1>')
    def test_text(self):
        node = TextNode("text",TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "text")
    def test_text_link(self):
        node = TextNode("text", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "text")
        self.assertEqual(html_node.props, {"href":node.url})
    def test_text_link2(self):
        node = TextNode("text", TextType.LINK,"https://www.boot.dev/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "text")
        self.assertEqual(html_node.props, {"href":node.url})
    def test_text_image(self):
        node = TextNode("text", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":node.url, "alt": node.text})
    def test_text_image2(self):
        node = TextNode("", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":node.url, "alt": node.text})
    def test_text_image3(self):
        node = TextNode("text", TextType.IMAGE, "https://media.istockphoto.com/id/1418379255/photo/net-zero-2050-carbon-neutral-and-net-zero-concept-natural-environment-a-climate-neutral-long.jpg?s=612x612&w=is&k=20&c=QXJOqA7TSIiVMrSpakdbD7Hm8k3GZnrqQMJHSUFrM5M=")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":node.url, "alt": node.text})
    def test_text_bold(self):
        node = TextNode("text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value, "text")
    def test_text_italic(self):
        node = TextNode("text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value, "text")
    def test_text_code(self):
        node = TextNode("text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value, "text")
    def test_text_unsupported(self):
        node = TextNode("text", "Manga")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        

