class DuplicatePersonError(Exception):
    """
    Apare când se găsesc în repo două persoane cu același id(aceleași atribute).
    """
    pass


class DuplicateEventError(Exception):
    """
    Apare când se găsesc în repo două evenimente cu același id.
    """
    pass


class AlreadySignedUpError(Exception):
    """
    Apare când se încearcă înscrierea unei persoane la un eveniment la care este deja înscrisă.
    """
    pass


class EventNotFoundException(Exception):
    """
    Apare când nu este găsit un eveniment cu un id furnizat.
    """
    pass


class PersonNotFoundException(Exception):
    """
    Apare când nu este găsită o persoană cu un id furnizat.
    """
    pass
