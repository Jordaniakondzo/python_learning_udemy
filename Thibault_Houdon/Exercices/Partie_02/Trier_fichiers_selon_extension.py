# Trier les fichiers selon leur extension dans le dossier Downloads avec la bibliothèque pathlib.
from pathlib import Path
import shutil

# Obtenir le chemin du dossier Downloads de l'utilisateur.
tri_dossier = Path.home() / "Downloads"

# Créer un dictionnaire pour stocker les dossiers selon les extensions des fichiers.
extension_folders = {"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
                     "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
                     "Musiques": [".mp3", ".wav", ".aac", ".flac"],
                     "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
                     "Codes": [".py", ".ipynb", ".js", ".html", ".css", ".java", ".c", ".cpp", ".rb", ".php"],
                     "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
                     "Logiciels": []}

# Obtenir le chemin du dossier Telegram Desktop dans Downloads
telegram_dossier = tri_dossier / "Telegram Desktop"
# Créer un dictionnaire pour stocker les dossiers selon les extensions des fichiers du dossier Telegram Desktop.
telegram_extensions = {
    "Telegram_Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Telegram_Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Telegram_Musiques": [".mp3", ".wav", ".aac", ".flac"],
    "Telegram_Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Telegram_Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Telegram_Codes": [".py", ".ipynb", ".js", ".html", ".css", ".java", ".c", ".cpp", ".rb", ".php"],
    "Telegram_Autres": []
}

# Parcourir tous les fichiers dans le dossier Telegram Desktop s'il existe et s'il est un dossier.
if telegram_dossier.exists() and telegram_dossier.is_dir():
    # Parcourir tous les fichiers dans le dossier Telegram Desktop et les trier selon leur extension.
    for fichier in telegram_dossier.iterdir():
        # Vérifier si c'est un fichier et non un dossier.
        if fichier.is_file():
            deplace = False # Indicateur pour savoir si le fichier a été déplacé ou non.
            # Vérifier l'extension du fichier et le déplacer dans le dossier approprié.
            for dossier, extensions in telegram_extensions.items():
                # Vérifier si l'extension du fichier est dans la liste des extensions du dossier de Telegram.
                if fichier.suffix.lower() in extensions:
                    # Créer le dossier si il n'existe pas.
                    cible_dossier = telegram_dossier / dossier
                    cible_dossier.mkdir(parents=True, exist_ok=True)
                    # Déplacer le fichier dans le dossier approprié
                    shutil.move(str(fichier), str(cible_dossier / fichier.name))
                    deplace = True
                    break
            # Si l'extension ne correspond à aucun dossier, le déplacer dans le dossier "Telegram_Autres".    
            if not deplace:
                cible_dossier = telegram_dossier / "Telegram_Autres"
                cible_dossier.mkdir(parents=True, exist_ok=True)
                shutil.move(str(fichier), str(cible_dossier / fichier.name))
                deplace = True

# Parcourir tous les fichiers dans le dossier Downloads
for fichier in tri_dossier.iterdir():
    # Vérifier si c'est un fichier et non un dossier.
    if fichier.is_file():
        deplace = False
        # Vérifier l'extension du fichier et le déplacer dans le dossier approprié
        for dossier, extensions in extension_folders.items():
            # Vérifier si l'extension du fichier est dans la liste des extensions du dossier
            if fichier.suffix.lower() in extensions:
                # Créer le dossier si il n'existe pas
                cible_dossier = tri_dossier / dossier
                cible_dossier.mkdir(exist_ok=True)
                # Déplacer le fichier dans le dossier approprié
                shutil.move(str(fichier), str(cible_dossier / fichier.name))
                deplace = True
                break
        # Si l'extension ne correspond à aucun dossier, le déplacer dans le dossier "Logiciels".    
        if not deplace:
            cible_dossier = tri_dossier / "Logiciels"
            cible_dossier.mkdir(exist_ok=True)
            shutil.move(str(fichier), str(cible_dossier / fichier.name))
            deplace = True