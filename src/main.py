import sys
from copystatic import clear_directory, copy_contents
from generate_page import generate_pages_recursive
def main():
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    
    clear_directory("./docs")
    log = copy_contents("./static", "./docs")
    for entry in log:
        print(entry)
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()
