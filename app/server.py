from flask import render_template
from app import app, socketio
from app.markdowns import parse_custom_markdown
import os
import threading
import subprocess

MARKDOWN_DIRECTORY = "markdowns"
markdown_file = ""  # Nom du fichier Markdown à afficher

@app.route("/")
def home():
    """Afficher le fichier Markdown converti."""
    file_path = os.path.join(MARKDOWN_DIRECTORY, markdown_file)
    if not os.path.exists(file_path):
        return f"<h1>Erreur : le fichier '{markdown_file}' n'existe pas.</h1>"
    
    # Lire et parser le contenu Markdown
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    html_content = parse_custom_markdown(markdown_content)

    # Rendre le template avec le contenu HTML généré
    return render_template("preview.html", content=html_content, file_name=markdown_file)

def start_server(file_name):
    """Démarrer le serveur Flask et surveiller les modifications."""
    global markdown_file
    markdown_file = file_name

    # Ouvrir le fichier dans l'éditeur de code
    file_path = os.path.join(MARKDOWN_DIRECTORY, file_name)
    try:
        # Ouvrir avec VS Code si disponible, sinon ouvrir avec l'éditeur par défaut
        if os.name == "nt":  # Pour Windows
            subprocess.run(["code", file_path], check=True)  # VS Code
        else:  # Pour Linux/Mac
            subprocess.run(["code", file_path], check=True)  # VS Code
    except FileNotFoundError:
        print("VS Code n'est pas installé. Ouverture avec l'éditeur par défaut.")
        os.startfile(file_path) if os.name == "nt" else subprocess.run(["xdg-open", file_path])

    # Surveiller les modifications dans un thread séparé
    threading.Thread(target=watch_file, args=(file_name,), daemon=True).start()

    # Lancer le serveur SocketIO
    socketio.run(app, debug=True)

def watch_file(file_name):
    """Surveiller les modifications du fichier Markdown."""
    file_path = os.path.join(MARKDOWN_DIRECTORY, file_name)
    if not os.path.exists(file_path):
        print(f"Erreur : le fichier '{file_name}' n'existe pas.")
        return

    last_modified = os.path.getmtime(file_path)
    while True:
        try:
            current_modified = os.path.getmtime(file_path)
            if current_modified != last_modified:
                last_modified = current_modified
                socketio.emit("update")  # Notifier le client en temps réel
        except FileNotFoundError:
            print(f"Erreur : le fichier '{file_name}' a été supprimé.")
            break
