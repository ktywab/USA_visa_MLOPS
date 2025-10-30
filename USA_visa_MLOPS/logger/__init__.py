import logging               # Module standard pour la journalisation (logs)
import os                    # Outils pour manipuler le système de fichiers (chemins, dossiers)

from from_root import from_root   # Fonction tierce : renvoie le chemin "racine" du projet
from datetime import datetime     # Pour dater/horodater le fichier de log

# Nom du fichier de log avec horodatage à la seconde (ex: 10_30_2025_14_22_05.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Nom du dossier qui contiendra les fichiers de log
log_dir = 'logs'

# Chemin ABSOLU du fichier de log : <racine_projet>/logs/<fichier_log>
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Crée un dossier "logs" dans le répertoire COURANT si absent
# ⚠️ Attention : ce n'est pas forcément le même "logs" que celui de logs_path
os.makedirs(log_dir, exist_ok=True)

# Configuration globale du logging :
# - filename=logs_path : écrit les logs dans le fichier défini ci-dessus
# - format=... : format des lignes de log (date, logger, niveau, message)
# - level=logging.DEBUG : inclut tous les messages de DEBUG à CRITICAL
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
