# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: IdeaSprint
import argparse

def main():
    parser = argparse.ArgumentParser(description="IdeaSprint CLI")
    parser.add_argument("command", choices=["add", "list", "show", "remove"], help="Command to run")
    parser.add_argument("--file", "-f", default="ideas.txt", help="Data file path")
    args = parser.parse_args()
    if args.command == "add":
        print("Add a new idea (interactive mode)")
    elif args.command == "list":
        print("List all ideas")
    elif args.command == "show":
        print("Show details of a specific idea")
    elif args.command == "remove":
        print("Remove an idea by ID")
    print(f"Command: {args.command}, File: {args.file}")
