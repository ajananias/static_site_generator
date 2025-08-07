from copystatic import clear_directory, copy_contents
from generate_page import generate_page
def main():
    clear_directory("public")
    log = copy_contents("static", "public")
    for entry in log:
        print(entry)
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
