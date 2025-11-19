#!/usr/bin/env python3
import hashlib
import re
import sys

def detect_hash_type(hash_string):
    hash_string = hash_string.strip().lower()
    if not re.fullmatch(r"[a-f0-9]+", hash_string):
        return "❌ Invalid input: Hash must contain only hexadecimal characters."
    length = len(hash_string)
    if length == 32:
        return "✅ Detected Hash Type: MD5"
    elif length == 40:
        return "✅ Detected Hash Type: SHA1"
    elif length == 64:
        return "✅ Detected Hash Type: SHA256"
    elif length == 96:
        return "✅ Detected Hash Type: SHA384"
    elif length == 128:
        return "✅ Detected Hash Type: SHA512"
    else:
        return f"❓ Unknown hash type (length: {length})"

def generate_md5(plaintext):
    return hashlib.md5(plaintext.encode("utf-8")).hexdigest()

def banner():
    print("\033[1;36m")
    print("╔═══════════════════════════════════════╗")
    print("║     🔐 Hash Detector & MD5 Generator   ║")
    print("╠═══════════════════════════════════════╣")
    print("║      by YourName | v1.0 | 2025         ║")
    print("╚═══════════════════════════════════════╝")
    print("\033[0m")

def menu():
    banner()
    print("1️⃣  Detect hash type")
    print("2️⃣  Generate MD5 from plaintext")
    print("3️⃣  Exit")
    choice = input("\nEnter choice (1-3): ").strip()
    if choice == "1":
        h = input("Enter hash string: ")
        print(detect_hash_type(h))
    elif choice == "2":
        text = input("Enter plaintext: ")
        print("MD5:", generate_md5(text))
    elif choice == "3":
        print("👋 Goodbye!")
        exit()
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(detect_hash_type(sys.argv[1]))
    else:
        while True:
            menu()
