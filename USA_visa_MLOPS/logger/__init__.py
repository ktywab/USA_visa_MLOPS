import logging
import os

from from_root import from_root
from datetime import datetime
from pathlib import Path


# Calcule la racine du projet (On remonte à la racine du projet niveau -2)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Crée un dossier logs/ à la racine du projet s'il n'existe pas déjà il est créer
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Génère un nom de fichier de log horodaté
LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Configure logging with both file and stdout handlers (Avec un niveau DEBUG c'est à dire tout type d'erreur sera loggé)
logging.basicConfig(
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,  # journalise tout, de DEBUG à CRITICAL
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
