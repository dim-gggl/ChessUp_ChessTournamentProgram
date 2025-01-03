import os


class HTMLExporter:
    EXPORT_DIR = "data/reports/"

    @staticmethod
    def export_to_html(filename, title, content):
        """
        Génère un fichier HTML basique dans le répertoire EXPORT_DIR.
        """
        if not os.path.exists(HTMLExporter.EXPORT_DIR):
            os.makedirs(HTMLExporter.EXPORT_DIR)

        filepath = os.path.join(HTMLExporter.EXPORT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"<html><head><title>{title}</title></head><body>")
            f.write(f"<h1>{title}</h1>")
            f.write(content)
            f.write("</body></html>")

        print(f"[SUCCÈS] Rapport exporté dans {filepath}.")
