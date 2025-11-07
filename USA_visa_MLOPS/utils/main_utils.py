import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Lit un fichier YAML et retourne son contenu sous forme de dict.
    - file_path: chemin du fichier YAML.
    - Retour: dict ou liste (selon le YAML) ; ici typé dict par convention.
    - Exceptions: enveloppées dans USvisaException.
    """
    try:
        # Mode "rb" n'est pas obligatoire pour YAML, mais ne pose pas problème.
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)  # parse sécurisé du YAML
    except Exception as e:
        # On remonte une exception métier avec le contexte sys
        raise USvisaException(e, sys) from e
    

    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Écrit un objet Python dans un fichier YAML.
    - file_path: chemin cible.
    - content: objet sérialisable en YAML (dict, list, etc.).
    - replace: si True, supprime le fichier existant avant écriture.
    """
    try:
        # Si replace=True et que le fichier existe, il est supprimé avant ré-écriture
        if replace and os.path.exists(file_path):
            os.remove(file_path)  # on force une réécriture propre

        # S’assure que le dossier existe (no-op si déjà là)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Écriture texte suffisant pour YAML
        with open(file_path, "w") as file:
            yaml.dump(content, file)  # attention: par défaut non “safe_dump”
    except Exception as e:
        raise USvisaException(e, sys) from e



def load_object(file_path: str) -> object:
    """
    Charge un objet sérialisé avec dill depuis file_path.
    - file_path: chemin du fichier binaire .pkl/.dill.
    - Retour: l'objet désérialisé.
    """
    logging.info("Entered the load_object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)  # désérialisation
        logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise USvisaException(e, sys) from e
    


def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Sauvegarde un tableau NumPy dans un fichier .npy.
    - file_path: chemin cible.
    - array: np.array à enregistrer.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)  # format .npy
    except Exception as e:
        raise USvisaException(e, sys) from e
    



def load_numpy_array_data(file_path: str) -> np.array:
    """
    Charge un tableau NumPy depuis un fichier .npy.
    - file_path: chemin source.
    - Retour: np.array chargé.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)  # retourne directement l'array
    except Exception as e:
        raise USvisaException(e, sys) from e




def save_object(file_path: str, obj: object) -> None:
    """
    Sérialise un objet Python avec dill et l'écrit dans file_path.
    - file_path: chemin cible.
    - obj: objet à sérialiser.
    """
    logging.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)  # sérialisation binaire
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise USvisaException(e, sys) from e



def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    Supprime des colonnes d'un DataFrame Pandas et retourne le résultat.
    - df: DataFrame source.
    - cols: liste des noms de colonnes à supprimer.
    """
    logging.info("Entered drop_columns method of utils")
    try:
        # axis=1 redondant avec columns=..., mais inoffensif
        df = df.drop(columns=cols, axis=1)
        logging.info("Exited the drop_columns method of utils")
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e