import os      # (inutile ici : rien dans ce fichier n'utilise os)
import sys     # utilisé pour récupérer la traceback courante via sys.exc_info()

"""
Récupère la traceback courante, extrait les détails de l'erreur puis construit un message d'erreur détaillé en précisant
 le fichier source et le numéro de ligne.

"""

def error_message_detail(error, error_detail: sys):
    # Récupère (type, valeur, traceback) de l'exception en cours dans ce thread
    _, _, exc_tb = error_detail.exc_info()

    # Nom du fichier source où l'exception s'est produite
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Message enrichi : fichier, numéro de ligne, message de l’erreur d’origine
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: message de l'erreur (souvent l'exception d'origine)
        :param error_detail: généralement le module sys pour récupérer la traceback
        """
        super().__init__(error_message)  # initialise Exception avec le message brut
        # Construit et stocke un message détaillé (fichier + ligne + message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Affiche le message détaillé lorsqu'on str() l'exception
        return self.error_message
