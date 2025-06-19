import os

def print_file_structure(start_path="."):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = '    ' * level
        print(f"{indent}📁 {os.path.basename(root)}/")
        for file in files:
            print(f"{indent}    📄 {file}")

def main():
    print("📦 Project File Structure:\n")
    # Go one level up from utils (project root)
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print_file_structure(root_path)

if __name__ == "__main__":
    main()
