from domain.entities import TvShow, ShowEvaluation


class ShowService:
    """
    Gestionează acțiunile care fac legătura între datele din repozitor și interfață.
    """
    def __init__(self, s_repo, s_val):
        """
        Inițializăm service-ul pentru seriale
        :param s_repo: ShowFileRepo/ShowRepo
        :param s_val: ShowValidator
        """
        self.__repo = s_repo
        self.__val = s_val

    def add_show(self, show_id, title, genre, no_episodes):
        """
        Adaugă un serial
        :param show_id: id-ul serialului
        :param title: titlul serialului
        :param genre: genul serialului
        :param no_episodes: numărul de episoade
        :return: -
        :raise: ShowValidationException dacă parametrii primiți sunt invalizi
                DuplicateIdException dacă există un alt serial cu același ID.
        """
        show = TvShow(show_id, title, genre, no_episodes)
        self.__val.validate_show(show)
        self.__repo.store(show)

    def get_all_shows(self):
        """
        Returnează o listă cu toate serialele.
        :return: shows_list - lista de seriale
        :rtype: list (of TvShow objects)
        """
        shows_list = self.__repo.get_all()
        return shows_list

    def search_by_genre(self, genre):
        """
        Returnează o listă cu toate serialele din genul dat
        :param genre: genul dat
        :type genre: str
        :return: shows_in_genre - lista cerută
        :rtype: list (of TvShow objects)
        """
        shows_in_genre = self.__repo.get_shows_by_genre(genre)
        return shows_in_genre

    def get_preference(self, show_id, no_seen_eps):
        """
        Returnează preferința utilizatorului pentru un anumit serial.
        :param show_id: id-ul serialului pentru care se returnează preferința
        :return: pref
        :rtype: str
        :raise: ShowNotFoundException dacă nu se găsește serial cu id-ul dat
        """
        self.__repo.find(show_id)
        show_evaluation = ShowEvaluation(self.__repo.find(show_id), no_seen_eps)
        return show_evaluation.get_preference()