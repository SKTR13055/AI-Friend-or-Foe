# obfuscation.py (fixed)
import re
import random
import string
import sys
import os

def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def obfuscate_file(input_path, output_path):
    with open(input_path, "r") as f:
        code = f.read()

    # find variable-like words
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
    mapping = {}

    for token in tokens:
        if token not in mapping and token not in ["import", "def", "return", "print", "if", "else", "for", "while"]:
            mapping[token] = generate_random_name()

    # replace tokens
    for old, new in mapping.items():
        code = code.replace(old, new)

    # optional: add dummy comments
    code = "# Obfuscated Code\n" + code

    with open(output_path, "w") as f:
        f.write(code)

    print(f"[Obfuscation] Saved: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python obfuscation.py input_file.py output_file.py")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        sys.exit(1)
    
    obfuscate_file(input_file, output_file)