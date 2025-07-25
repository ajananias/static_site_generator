from textnode import TextNode, TextType

def main():
    node = TextNode("Dummy Text", TextType.TEXT.value, "https://www.boot.dev")
    print(node)

main()
