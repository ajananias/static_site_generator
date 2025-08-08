import sys
from copystatic import clear_directory, copy_contents
from generate_page import generate_pages_recursive
def main():
    basepath = sys.argv[0]
    clear_directory("public")
    log = copy_contents("./static", "./public")
    for entry in log:
        print(entry)
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()
