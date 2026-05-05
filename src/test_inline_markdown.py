import unittest
from inline_markdown import( split_nodes_delimiter, extract_markdown_links, 
                            extract_markdown_images, text_to_textnodes,
                            split_nodes_image, split_nodes_link,)
from textnode import TextNode, TextType

class TestInline(unittest.TestCase):
    def test_single_old_node(self):
        old1 = TextNode("text", TextType.CODE)
        self.assertEqual(split_nodes_delimiter([old1], '`', TextType.BOLD), [old1])
    def test_bold_delimiter(self):
        node = TextNode("These are **bold** letters",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("These are ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" letters", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    def test_code_delimiter(self):
        node = TextNode("These are text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("These are text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    def test_unclosed_delimiter_raises(self):
        node = TextNode("This is `unclosed code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
    def test_markdown_images(self):
        text = "I am sleepy ![sleepy cat](https://example.com/cat.jpg)"
        result = extract_markdown_images(text)
        self.assertListEqual(result, [("sleepy cat", "https://example.com/cat.jpg")])
    def test_markdown_links(self):
        text = "I need to study [boot dev](https://www.boot.dev)"
        result = extract_markdown_links(text)
        self.assertListEqual(result, [("boot dev", "https://www.boot.dev")])
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_images2(self):
        node = TextNode(
            "I don't want to write ![image](https://i.imgur.com/zjjcJKZ.png) a bunch of tests", TextType.TEXT,
        ) 
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("I don't want to write ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" a bunch of tests", TextType.TEXT),
            ],
            new_nodes
        )
    def test_split_images3(self):
        node = TextNode("Just plain text, nothing fancy", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Just plain text, nothing fancy", TextType.TEXT),
            ],
            new_nodes
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links2(self):
        node = TextNode(
            "I don't want to write [image](https://i.imgur.com/zjjcJKZ.png) a bunch of tests", TextType.TEXT,
        ) 
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("I don't want to write ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" a bunch of tests", TextType.TEXT),
            ],
            new_nodes
        )
    def test_split_link3(self):
        node = TextNode("Just plain text, nothing fancy", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Just plain text, nothing fancy", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_text_textnode(self):
        text = "I'm **really** am _struggling_ with this `lesson` [study](https://www.boot.dev) **please** _help_ ![lain](https://www.lain.png)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("I'm ", TextType.TEXT),
                TextNode("really", TextType.BOLD),
                TextNode(" am ", TextType.TEXT),
                TextNode("struggling", TextType.ITALIC),
                TextNode(" with this ", TextType.TEXT),
                TextNode("lesson", TextType.CODE),
                TextNode(" ", TextType.TEXT),      
                TextNode("study", TextType.LINK, "https://www.boot.dev"),
                TextNode(" ", TextType.TEXT),      
                TextNode("please", TextType.BOLD),
                TextNode(" ", TextType.TEXT),      
                TextNode("help", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),      
                TextNode("lain", TextType.IMAGE, "https://www.lain.png"),
            ],
            new_nodes
        )
        