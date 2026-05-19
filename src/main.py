import sys
from textnode import TextType, TextNode
from copystatic import copy_source_to_destination, generate_pages_recursive
from generate_page import generate_page

def junk():
    node = TextNode("insert text", TextType.TEXT,"https://www.boot.dev")
    print(node)

def main():
    basepath = "/"
    if len(sys.argv) >1:
        basepath = sys.argv[1]
    copy_source_to_destination("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()
