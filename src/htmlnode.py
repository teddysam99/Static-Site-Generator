from textnode import TextType, TextNode
class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag              # tag name (e.g."p","a","h1",etc.)
        self.value = value          # value of Htmlnode's tag
        self.children = children    # list of Htmlnode objects
        self.props = props          # dictionary of attributes for Htmlnode tag
    def to_html(self):
        raise NotImplementedError("Override this method")
    def props_to_html(self):
        result = ''
        if not self.props:
            return result
        for key,value in self.props.items():
            result += f' {key}="{value}"'
        return result
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
    def __eq__(self,node):
        result = True
        if self.tag != node.tag:
            result = False
        if self.value != node.value:
            result = False
        if self.children != node.children:
            result = False
        if self.props != node.props:
            result = False
        return result
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
       super().__init__(tag,value,None,props)
    def to_html(self):
        if self.value is None:
            raise ValueError("Value must be included, not optional")
        if self.tag is None:
            return self.value
        props = self.props_to_html()
        render_tag = f'<{self.tag}{props}>{self.value}</{self.tag}>'
        return render_tag
    
    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        result = ""
        if self.tag is None:
            raise ValueError("Tag must be included, not optional")
        if self.children is None:
            raise ValueError("Children --> list must be included, not optional")
        for child in self.children:
            result += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a",text_node.text, {"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src":text_node.url ,"alt":text_node.text})
    raise Exception("Unsupported type, cannot convert to html")
