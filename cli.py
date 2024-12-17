import sys
from app.server import start_server
from app.parser import show_markdown_help, create_markdown, delete_markdown, list_markdown_files, edit_markdown, rename_markdown, export_markdown_to_html,show_help,show_help
from app.server import start_server

def main():
    """CLI pour gérer les commandes Markdown."""
    if len(sys.argv) < 2:
        print("Usage :")
        print("  python cli.py create <nom-du-fichier>")
        print("  python cli.py delete <nom-du-fichier>")
        print("  python cli.py list")
        print("  python cli.py syntaxe")
        print("  python cli.py rename <ancien-nom> <nouveau-nom>")
        print("  python cli.py edit <nom-du-fichier>")
        print("  python cli.py export <nom-du-fichier>")
        print("  python cli.py preview <nom-du-fichier>")
        return

    command = sys.argv[1]


    
    if command == "create":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nom de fichier.")
        else:
            create_markdown(sys.argv[2])
    elif command == "syntaxe":
        show_markdown_help()
    elif command == "help":
        show_help()
    elif command == "rename":
        if len(sys.argv) < 4:
            print("Usage : python cli.py rename <ancien-nom> <nouveau-nom>")
        else:
            rename_markdown(sys.argv[2], sys.argv[3])
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nom de fichier.")
        else:
            delete_markdown(sys.argv[2])
    elif command == "edit":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nom de fichier.")
        else:
            edit_markdown(sys.argv[2])
    elif command == "export":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nom de fichier.")
        else:
            export_markdown_to_html(sys.argv[2])
    elif command == "list":
        list_markdown_files()
    elif command == "preview":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nom de fichier.")
        else:
            start_server(sys.argv[2])
    else:
        print(f"Commande inconnue : '{command}'.")

if __name__ == "__main__":
    main()
