import os


class HTMLExporter:
    EXPORT_DIR = "data/reports/"

    @staticmethod
    def export_to_html(filename, title, content):
        """
        Génère un fichier HTML dans le répertoire EXPORT_DIR.
        """
        if not os.path.exists(HTMLExporter.EXPORT_DIR):
            os.makedirs(HTMLExporter.EXPORT_DIR)

        filepath = os.path.join(HTMLExporter.EXPORT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(
                f"<html><head><link href='style.css' "
                f"rel='stylesheet'><link rel='preconnect' "
                f"href='https://fonts.googleapis.com'><link rel='preconnect' "
                f"href='https://fonts.gstatic.com' crossorigin><link "
                f"href='https://fonts.googleapis.com/css2?family=Manuale:ital,wght@0,300..800;1,300..800&family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap' "
                f"rel='stylesheet'><title>{title}</title></head><body>"
            )
            f.write(f"<section><header><h1>{title}</h1></header>")
            f.write(content)
            f.write("</section></body></html>")

        print(f"[SUCCÈS] Rapport exporté dans {filepath}.")
