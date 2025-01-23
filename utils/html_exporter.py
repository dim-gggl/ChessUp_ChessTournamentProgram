import os
from datetime import datetime


class HTMLExporter:
    EXPORT_DIR = "data/reports/"

    @staticmethod
    def export_to_html(filename, title, content):
        """
        Generates an HTML file in the EXPORT_DIR directory.
        """
        if not os.path.exists(HTMLExporter.EXPORT_DIR):
            os.makedirs(HTMLExporter.EXPORT_DIR)

        export_time = datetime.now().strftime("%x ~~ %X")
        exported_at = f"Ce rapport a été généré automatiquement par le programme 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ à la date: {export_time}."

        filepath = os.path.join(HTMLExporter.EXPORT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(
                f"<!DOCTYPE html>\n<html>\n<head>\n<link href='style.css' "
                f"rel='stylesheet'>\n "
                f"<link rel='preconnect href='https://fonts.googleapis.com'>\n"
                f"<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
                f"<link href='https://fonts.googleapis.com/css2?family=Special+Elite&display=swap' "
                f"rel='stylesheet'>\n<title>\n{title}\n</title>\n</head>\n<body>\n"

            )
            f.write(f"\n<header class='header-banner''>\n<h1>{title}</h1>\n</header>\n <main class='main-content'>\n")
            f.write(content)
            f.write("\n</main>\n<footer class='footer-brand'>\n𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎\n</footer>\n</body>\n</html>")
        print("\n" * 50)
        print(f"\t\t[SUCCÈS] Rapport exporté dans {filepath}.\n\n\n\n\n")
        input("\tAppuyez sur ENTRÉE pour continuer")
