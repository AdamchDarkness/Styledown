import os
import sys
import subprocess
from app.markdowns import parse_custom_markdown

# Répertoires
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKDOWN_DIRECTORY = os.path.join(BASE_DIR, "markdowns")
EXPORTS_DIRECTORY = os.path.join(BASE_DIR, "exports")  # Répertoire exports en dehors de `app`

# Assurer que les répertoires existent
os.makedirs(MARKDOWN_DIRECTORY, exist_ok=True)
os.makedirs(EXPORTS_DIRECTORY, exist_ok=True)

def export_markdown_to_html(file_name):
    """Exporter un fichier Markdown en fichier HTML avec une prévisualisation complète."""
    file_path = os.path.join(MARKDOWN_DIRECTORY, file_name)
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier '{file_name}' n'existe pas.")
        return

    # Lire le contenu du fichier Markdown
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Convertir le Markdown en HTML
    html_content = parse_custom_markdown(markdown_content)

    # Construire un fichier HTML complet
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{file_name}</title>
        <link href="https://cdn.tailwindcss.com" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9fafb;
                color: #374151;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {html_content}
        </div>
    </body>
    </html>
    """

    # Créer le fichier HTML dans le dossier `exports`
    html_file_name = file_name.replace(".md", ".html")
    output_path = os.path.join(EXPORTS_DIRECTORY, html_file_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Fichier exporté avec prévisualisation : {output_path}")


def create_markdown(file_name):
    """Créer un nouveau fichier Markdown."""
    if not file_name.endswith(".md"):
        file_name += ".md"
    file_path = os.path.join(MARKDOWN_DIRECTORY, file_name)
    if os.path.exists(file_path):
        print(f"Le fichier '{file_name}' existe déjà.")
        return
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# Nouveau fichier Markdown\n\nCommencez à écrire ici...\n")
    print(f"Fichier '{file_name}' créé avec succès.")

def edit_markdown(file_name):
    """Ouvrir un fichier Markdown dans l'éditeur par défaut."""
    file_path = os.path.join(MARKDOWN_DIRECTORY, file_name)
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier '{file_name}' n'existe pas.")
        return
    try:
        if sys.platform == "win32":
            os.startfile(file_path)
        elif sys.platform == "darwin":
            subprocess.call(["open", file_path])
        else:
            subprocess.call(["xdg-open", file_path])
    except Exception as e:
        print(f"Impossible d'ouvrir le fichier : {e}")

def rename_markdown(old_name, new_name):
    """Renommer un fichier Markdown."""
    if not new_name.endswith(".md"):
        new_name += ".md"

    old_path = os.path.join(MARKDOWN_DIRECTORY, old_name)
    new_path = os.path.join(MARKDOWN_DIRECTORY, new_name)

    if not os.path.exists(old_path):
        print(f"Erreur : Le fichier '{old_name}' n'existe pas.")
        return
    if os.path.exists(new_path):
        print(f"Erreur : Un fichier portant le nom '{new_name}' existe déjà.")
        return

    os.rename(old_path, new_path)
    print(f"Fichier '{old_name}' renommé en '{new_name}'.")

def delete_markdown(file_name):
    """Supprimer un fichier Markdown."""
    file_path = os.path.join(MARKDOWN_DIRECTORY, file_name)
    if not os.path.exists(file_path):
        print(f"Le fichier '{file_name}' n'existe pas.")
        return
    try:
        os.remove(file_path)
        print(f"Fichier '{file_name}' supprimé avec succès.")
    except PermissionError:
        print(f"Permission refusée pour supprimer le fichier '{file_name}'.")

def list_markdown_files():
    """Lister les fichiers Markdown."""
    files = [f for f in os.listdir(MARKDOWN_DIRECTORY) if f.endswith(".md")]
    if not files:
        print("Aucun fichier Markdown trouvé.")
    else:
        print("Fichiers Markdown disponibles :")
        for file in files:
            print(f"- {file}")

def show_help():
    """Afficher l'aide complète avec toutes les commandes disponibles."""
    print("""
    Usage :
      python cli.py <commande> [arguments]

    Commandes disponibles :
      create <nom-du-fichier>          Créer un nouveau fichier Markdown.
      delete <nom-du-fichier>          Supprimer un fichier Markdown existant.
      list                             Lister tous les fichiers Markdown disponibles.
      rename <ancien-nom> <nouveau-nom> Renommer un fichier Markdown.
      edit <nom-du-fichier>            Ouvrir un fichier Markdown dans l'éditeur par défaut.
      export <nom-du-fichier>          Exporter un fichier Markdown en fichier HTML.
      preview <nom-du-fichier>         Prévisualiser un fichier Markdown dans le navigateur.
      syntaxe                          Syntaxe pour un fihcier markedown.
      help                             Afficher cette aide.

    Exemples :
      Créer un fichier :    python cli.py create example.md
      Supprimer un fichier : python cli.py delete example.md
      Renommer un fichier : python cli.py rename old.md new.md
      Exporter en HTML :    python cli.py export example.md
      Lister les fichiers : python cli.py list
      Prévisualiser :       python cli.py preview example.md
      Générer un guide :    python cli.py generate-help
    """)

def show_markdown_help():
    """Affiche le guide des commandes Markdown dans le terminal."""
    help_content = r"""
# Guide des commandes Markdown personnalisées

Ce document liste toutes les commandes Markdown supportées par l'application, leur syntaxe, et leur effet.

---

## Titre

# Titre h1
## Titre h2
### Titre h3
#### Titre h4
##### Titre h5
###### Titre h6

---

## Block de code
### Syntaxte
```<language de programation>

```

---

## Video
### Syntaxe
?(<url>)

---

## Liste
### Syntaxe
- texte
- texte

1. texte
2. texte

---

## Texte
### Syntaxte

* Texte * : Italic
** Texte ** : Bold
*** Texte *** : Bold Italic
~~ Texte ~~ : Texte Barre

---

## Retour a la ligne
\

---

## Badge
### Syntaxe
[badge color=<couleur> size=taille en px]

### Description
Affiche un badge

---

---

## Progress Bar
### Syntaxe
[progress value=<pourcentage> color="<couleur>"]

### Description
Affiche une barre de progression.

### Exemple
[progress value=70 color="blue"]

---

## Block Alerts
### Syntaxe
[!] Texte pour une alerte warning.
[i] Texte pour une alerte info.
[x] Texte pour une alerte d'erreur.
[✓] Texte pour une alerte de succès.

### Description
Affiche une alerte stylisée.

### Exemple
[!] Attention, une erreur pourrait survenir.
[i] Ceci est une information importante.
[x] Une erreur critique a été détectée.
[✓] Tout fonctionne correctement !

---

## Galerie d'images
### Syntaxe
[gallery]
![Texte alternatif](lien-image-1)
![Texte alternatif](lien-image-2)

### Description
Affiche une galerie d'images disposées en grille.

---

## Cartes
### Syntaxe
[card title="<titre>" image="<url-image-optionnel>"]
Contenu de la carte.

### Description
Crée une carte avec un titre, un contenu, et une image optionnelle.

---

## Colonnes et rangées
### Syntaxe
[row]
[col width=<nombre>]
Contenu de la colonne.
[/col]
[/row]

---

## Boutton
### Syntaxe
[button type=<type-of-button>]

### Description
Affiche un bouton stylisée.

### Types
default
alternative
dark
green
red
yellow
purple

---

## Lignes de séparation
### Syntaxe
---


    """
    print(help_content)


