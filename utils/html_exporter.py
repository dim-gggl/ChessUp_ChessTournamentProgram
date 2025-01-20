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
        exported_at = f"Ce rapport a été généré automatiquement par le programme logiciel 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ à la date suivante : {export_time}."

        filepath = os.path.join(HTMLExporter.EXPORT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(
                f"<html>\n<head>\n<link href='style.css' "
                f"rel='stylesheet'>\n<link rel='preconnect' "
                f"href='https://fonts.googleapis.com'>\n<link rel='preconnect' "
                f"href='https://fonts.gstatic.com' crossorigin>\n<link "
                f"href='https://fonts.googleapis.com/css2?family=Manuale:ital,wght@0,300..800;1,300..800&family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap' "
                f"rel='stylesheet'>\n<title>{title}</title>\n</head>\n<body>\n"
            )
            f.write(f"\n<header>\n<h1>{title}</h1>\n</header>\n<section>\n")
            f.write(content)
            f.write("</section>\n</body>\n</html>")
        print("\n" * 50)
        print(f"[SUCCÈS] Rapport exporté dans {filepath}.\n\n\n\n\n")
        input("Appuyez sur ENTRÉE pour continuer")
