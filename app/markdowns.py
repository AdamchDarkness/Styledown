import re
import os

def parse_custom_markdown(markdown_text):
    """Convertir le Markdown personnalisé en HTML stylisé avec gestion d'état pour les balises ouvertes."""

    lines = markdown_text.split("\n")
    html_output = []
    in_gallery = False
    in_card = False
    in_row = False
    in_banner = False
    in_code_block = False
    code_language = "plaintext" 
    current_style = {"font": "", "color": ""}

    for line in lines:

        # Ajouter le style aux lignes de texte
        if current_style["font"] or current_style["color"]:
            style = ""
            if current_style["font"]:
                style += f"font-family: {current_style['font']}; "
            if current_style["color"]:
                style += f"color: {current_style['color']}; "

            html_output.append(f'<p style="{style}">{line}</p>')
            continue

        #progress bar
        if line.startswith("[progress"):
            match = re.match(r'\[progress value=(\d+) color="(.+?)"\]', line.strip())
            if match:
                value, color = match.groups()
                html_output.append(f"""
                <div class="w-full bg-gray-200 rounded-full h-4 dark:bg-gray-700">
                    <div class="bg-{color}-600 dark:bg-{color}-500 h-4 rounded-full" style="width: {value}%"></div>
                </div>
                """)
            continue



        #block
        if re.match(r"^\[(\!|i|x|✓)\]", line.strip()):
            match = re.match(r"^\[(\!|i|x|✓)\]\s*(.+)", line.strip())
            if match:
                block_type, content = match.groups()
                classes = {
                    "!": "bg-yellow-100 text-yellow-800 dark:bg-yellow-800 dark:text-yellow-100",
                    "i": "bg-blue-100 text-blue-800 dark:bg-blue-800 dark:text-blue-100",
                    "x": "bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100",
                    "✓": "bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100",
                }
                icons = {
                    "!": "⚠️",
                    "i": "ℹ️",
                    "x": "❌",
                    "✓": "✅",
                }
                html_output.append(f"""
                <div class="p-4 mb-4 rounded-lg {classes.get(block_type, 'bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-100')}">
                    <span class="font-bold">{icons.get(block_type, '')}</span> {content}
                </div>
                """)
            continue




        # === GALERIE D'IMAGES ===
        if line.startswith("[gallery]"):
            in_gallery = True
            html_output.append('<div class="grid grid-cols-2 gap-4">')
            continue
        elif in_gallery and not line.strip():  # Fin de la galerie sur une ligne vide
            in_gallery = False
            html_output.append("</div>")
            continue
        elif in_gallery:
            match = re.match(r"!\[(.*?)\]\((.*?)\)", line.strip())
            if match:
                alt, src = match.groups()
                html_output.append(f'<img src="{src}" alt="{alt}" class="w-full h-auto rounded-lg shadow" />')
            continue

        # === CARTES ===
        if line.startswith("[card"):
            match = re.match(r'\[card title="(.+?)"(?: image="(.+?)")?\]', line.strip())
            if match:
                in_card = True
                title, image = match.groups()
                # Début de la carte
                html_output.append("""
                <div class="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-4 my-4 transition duration-300">
                """)
                # Image en haut de la carte (optionnelle)
                if image:
                    html_output.append(f"""
                    <img src="{image}" alt="{title}" class="w-full h-auto mb-4 rounded-t-lg">
                    """)
                # Titre de la carte
                html_output.append(f"""
                <h3 class="text-lg font-bold mb-2 text-gray-800 dark:text-gray-100">{title}</h3>
                """)
            continue
        elif in_card and not line.strip():  # Fin de la carte sur une ligne vide
            in_card = False
            # Fermeture de la carte
            html_output.append("</div>")
            continue
        elif in_card:
            # Contenu à l'intérieur de la carte
            html_output.append(f"""
            <div class="text-gray-700 dark:text-gray-300">{line.strip()}</div>
            """)
            continue


        # === COLONNES ET RANGÉES ===
        if line.startswith("[row]"):
            in_row = True
            html_output.append('<div class="grid grid-cols-12 gap-4">')
            continue
        elif line.startswith("[col"):
            match = re.match(r"\[col width=(\d+)\](.+)", line.strip())
            if match:
                width, content = match.groups()
                html_output.append(f'<div class="col-span-{width}">{content}</div>')
            continue
        elif in_row and not line.strip():  # Fin de la rangée sur une ligne vide
            in_row = False
            html_output.append("</div>")
            continue

        # === LIENS HREF ===
        if line.startswith("[link"):
            match = re.match(r"\[link href=(.+?)\](.+)", line.strip())
            if match:
                href, content = match.groups()
                html_output.append(f'<a href="{href}" class="text-blue-500 underline hover:text-blue-700">{content}</a>')
            continue

        # === BADGES ===
        if line.startswith("[badge"):
            match = re.match(r"\[badge color=(\w+) size=(\w+)\](.+)", line.strip())
            if match:
                color, size, content = match.groups()
                size_class = "text-xs" if size == "small" else "text-sm"
                html_output.append(f"""
                <span class="bg-{color}-100 text-{color}-800 {size_class} font-medium px-2.5 py-0.5 rounded dark:bg-{color}-900 dark:text-{color}-300">
                    {content}
                </span>
                """)
            continue

        # === BOUTONS ===
        if line.startswith("[button"):
            match = re.match(r"\[button type=(\w+)\](.+)", line.strip())
            if match:
                button_type, content = match.groups()
                classes = {
                    "default": "text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300",
                    "alternative": "text-gray-900 bg-white border border-gray-200 hover:bg-gray-100 hover:text-blue-700",
                    "dark": "text-white bg-gray-800 hover:bg-gray-900 focus:ring-4 focus:ring-gray-300",
                    "green": "text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300",
                    "red": "text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300",
                    "yellow": "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300",
                    "purple": "text-white bg-purple-700 hover:bg-purple-800 focus:ring-4 focus:ring-purple-300",
                }
                html_output.append(f"""
                <button type="button" class="font-medium rounded-lg text-sm px-5 py-2.5 mb-2 {classes.get(button_type, '')}">
                    {content}
                </button>
                """)
            continue

        # === BANNIÈRES ===
        if line.startswith("[banner"):
            match = re.match(r'\[banner image="(.+?)"\](.+)', line.strip())
            if match:
                image, content = match.groups()
                html_output.append(f"""
                <div class="fixed top-0 start-0 z-50 flex justify-between w-full p-4 border-b border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
                    <div class="flex items-center">
                        <img src="{image}" alt="Banner" class="w-10 h-10 me-3 rounded-full">
                        <p class="text-sm font-normal text-gray-500 dark:text-gray-400">{content}</p>
                    </div>
                </div>
                """)
            continue

        # === LIGNE DE SÉPARATION ===
        if line.strip() in ("---", "***"):
            html_output.append('<hr class="my-4 border-gray-300 dark:border-gray-600" />')
            continue

        if line.strip().startswith("> "):
            quote_content = line.strip()[2:]
            html_output.append(f'<blockquote class="border-l-4 pl-4 italic text-gray-600 border-gray-300 dark:text-white">{quote_content}</blockquote>')
            continue

        # === BLOCS DE CODE ===
        if line.startswith("```"):
            if in_code_block:
                # Fin du bloc de code
                in_code_block = False
                html_output.append(f"""
                <pre class="rounded-lg bg-gray-50 dark:bg-gray-800 p-4 overflow-x-auto transition duration-300">
        <code class="language-{code_language}">
        {''.join(code_content).strip()}
        </code>
                </pre>
                """)
                # Réinitialisation
                code_content = []
                code_language = ""
            else:
                # Début d'un bloc de code
                in_code_block = True
                code_language = line[3:].strip() or "plaintext"  # Langage spécifié ou 'plaintext' par défaut
            continue
        elif in_code_block:
            # Ajouter chaque ligne du bloc de code avec son retour à la ligne
            code_content.append(line + "\n")
            continue

        #video
        if line.startswith("?("):
            match = re.match(r'\?\((.+?)\)', line.strip())
            if match:
                src = match.group(1)
                html_output.append(f"""
                <video class="w-full" controls>
                    <source src="{src}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                """)
            continue

        # === SYNTAXE CLASSIQUE ===
        line = re.sub(r"^###### (.+)$", r'<h6 class="text-xl font-semibold mt-4">\1</h6>', line)
        line = re.sub(r"^##### (.+)$", r'<h5 class="text-xl font-semibold mt-4">\1</h5>', line)
        line = re.sub(r"^#### (.+)$", r'<h4 class="text-xl font-semibold mt-4">\1</h4>', line)
        line = re.sub(r"^### (.+)$", r'<h3 class="text-xl font-semibold mt-4">\1</h3>', line)
        line = re.sub(r"^## (.+)$", r'<h2 class="text-2xl font-bold mt-6">\1</h2>', line)
        line = re.sub(r"^# (.+)$", r'<h1 class="text-3xl font-extrabold mt-8">\1</h1>', line)
        line = re.sub(r"^- (.+)$", r'<li>\1</li>', line)
        line = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", line)
        line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
        line = re.sub(r"\*(.+?)\*", r"<em>\1</em>", line)
        line = re.sub(r"~~(.+?)~~", r"<del>\1</del>", line)
        line = re.sub(r"\\", r"<br />", line)

        html_output.append(line)

    if in_gallery:
        html_output.append("</div>")
    if in_card:
        html_output.append("</div>")
    if in_row:
        html_output.append("</div>")
    if in_code_block:
        html_output.append(f"""
        <pre class="prism-light rounded-lg bg-gray-50 dark:bg-gray-800 p-4 overflow-x-auto">
<code class="language-{code_language}">
{''.join(code_content).strip()}
</code>
        </pre>
        """)

    return "\n".join(html_output)


def include_file_content(file_path):
    """Inclure le contenu d'un fichier Markdown."""
    if not os.path.exists(file_path):
        return f'<p class="text-red-500">Erreur : Le fichier "{file_path}" n\'existe pas.</p>'
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return parse_custom_markdown(content)
