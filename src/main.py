from textnode import TextNode, TextType

def main():
    node = TextNode("Dummy Text", TextType.PLAIN.value, "https://www.boot.dev")
    print(node)

main()
