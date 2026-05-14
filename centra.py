import os
import re

# A simple script to scan files for potential security issues (Secrets, Hardcoded passwords)

# Patterns to look for
PATTERNS = {
    "Password/Secret": r'(?i)(password|secret|api_key|token|auth)\s*=\s*["\'][^"\']+["\']',
    "IP Address": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
}

def scan_file(file_path):
    issues_found = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for label, pattern in PATTERNS.items():
                    if re.search(pattern, line):
                        issues_found.append(f"[{label}] Line {line_num}: {line.strip()}")
    except Exception as e:
        return [f"Error reading file: {e}"]
    return issues_found

def main():
    print("--- Centra: Basic Security Scanner ---")
    print("Scanning current directory for hardcoded secrets and IPs...\n")
    
    current_dir = os.getcwd()
    
    for root, dirs, files in os.walk(current_dir):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            # Only scan text-based files
            if file.endswith(('.py', '.js', '.txt', '.env', '.yml', '.yaml', '.json')):
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, current_dir)
                
                results = scan_file(path)
                if results:
                    print(f"[!] Issues in {relative_path}:")
                    for r in results:
                        print(f"    {r}")
                    print()

    print("Scan complete!")

if __name__ == "__main__":
    main()
