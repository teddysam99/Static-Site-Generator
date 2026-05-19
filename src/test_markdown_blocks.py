import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node, extract_title

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "After a long day of work, I come back home just to code."
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(["After a long day of work, I come back home just to code.",], blocks)
    def test_markdown_to_blocks2(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual([], blocks)
    def test_markdown_to_blocks3(self):
        markdown = """
    After a long day of work,

    I come back home just to code.
    """
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(["After a long day of work,",
                            "I come back home just to code.",
                              ],
                                blocks)
    def test_markdown_to_blocks4(self):
        markdown = """
    I **really** just want to play video games right now,

    I don't want to be productive after work.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(["I **really** just want to play video games right now,",
                              "I don't want to be productive after work.",
                              ], blocks)
    def test_markdown_to_blocks3(self):
        markdown = """
After a long day of work,

I come back home just to code.
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(["After a long day of work,",
                            "I come back home just to code.",
                              ],
                                blocks)
    
    def test_block_type_heading(self):
        block = "#### I am so tired"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.HEADING)
    
    def test_block_type_code(self):
        block = """```
CODE
```"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.CODE)
    def test_block_type_quote(self):
        block = ">"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.QUOTE )
    
    def test_block_type_unordered_list(self):
        block = """- GAMING
- ANIME"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.UNORDERED_LIST)
    
    def test_block_type_ordered_list(self):
        block = """1. work
2. taxes
3. chores"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.ORDERED_LIST)
    
    def test_block_type_paragraph(self):
        block = "I'M DONE"
        bt = block_to_block_type(block)
        self.assertEqual(bt,BlockType.PARAGRAPH)

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
    
    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")
    def test_extract_title2(self):
        md = "## Not H1\n# Hi"
        title = extract_title(md)
        self.assertEqual(title, "Hi")
    def test_extract_title3(self):
        md = "no title here"
        with self.assertRaises(Exception):
            extract_title(md)
   