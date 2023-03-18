class ShowValidationException(Exception):
    """
    Apare când datele serialului sunt invalide.
    """
    pass

class DuplicateIdException(Exception):
    """
    Apare când se duplică un id.
    """
    pass

class ShowNotFoundException(Exception):
    """
    Apare când nu este găsit un serial căutat.
    """
    pass