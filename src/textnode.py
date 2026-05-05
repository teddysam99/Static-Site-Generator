from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"
    CODE = "code"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self,node):
        result = True
        if self.text != node.text:
            result = False
        if self.text_type != node.text_type:
            result = False
        if self.url != node.url:
            result = False
        return result
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
    