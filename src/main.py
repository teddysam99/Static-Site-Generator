from textnode import TextType, TextNode
from copystatic import copy_source_to_destination, generate_pages_recursive
from generate_page import generate_page


def junk():
    node = TextNode("insert text", TextType.TEXT,"https://www.boot.dev")
    print(node)

def main():
    copy_source_to_destination("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public/")

main()
