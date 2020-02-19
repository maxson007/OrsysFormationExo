#Exception de saissie invalide
class SaisieInvalide(Exception):
    def __init__(self, valeur):
        self.valeur=valeur

    def __str__(self):
        return repr(self.valeur)