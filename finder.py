import os

def finder(repo_path, fully_qualified_method):
    paths = []
    
    for root, _, files in os.walk(repo_path):
        for f in files:
            if f.endswith(('.java', '.kt')):
                paths.append(os.path.join(root, f))
    
    if not paths:
        print(f"No Java or Kotlin files found in the repository.")
        return

    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            method_found = False
            code = []
            for line in lines:
                if fully_qualified_method in line:
                    method_found = True
                if method_found:
                    code.append(line.strip())
                    if '}' in line:
                        break

            if code:
                print(f"File: {path}")
                print('\n'.join(code))
                print("\n-----------------------------------\n")

if __name__ == "__main__":
    repo_path = "generic-expression-parser-main"
    fully_qualified_method = "MainChecker"
    finder(repo_path, fully_qualified_method)
