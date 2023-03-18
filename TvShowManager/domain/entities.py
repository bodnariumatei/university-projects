class TvShow:
    """
    Clasă care are rolul de a gestiona atributele unui show.
    """
    def __init__(self, show_id, title, genre, no_eps):
        """
        Inițializăm clasa
        :param show_id: id-ul serialului
        :type show_id: str
        :param title: titlul serialului
        :type title: str
        :param genre: genul serialului
        :type genre: str
        :param no_eps: numărul de episoade difuzate
        :type no_eps: int
        """
        self.__show_id = show_id
        self.__title = title
        self.__genre = genre
        self.__no_eps = no_eps

    def get_show_id(self):
        return self.__show_id

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_no_eps(self):
        return self.__no_eps

    def set_show_id(self, show_id):
        self.__show_id = show_id

    def set_title(self, title):
        self.__title = title

    def set_genre(self, genre):
        self.__genre = genre

    def set_no_eps(self, no_eps):
        self.__no_eps = no_eps

    def __eq__(self, other):
        if self.__show_id == other.get_show_id() and self.__title == other.get_title():
            return True
        return False


class ShowEvaluation:
    def __init__(self, show, no_seen_eps):
        """
        Initializăm
        :param show: serialul pentru care se face evaluarea
        :type show: TvShow
        :param no_seen_eps: numărul de episoade văzute
        :type no_seen_eps: int
        """
        self.__show = show
        self.__no_seen_eps = no_seen_eps

    def get_preference(self):
        """
        Returnează nivelul de preferință al utilizatorului pentru serial
        :return: pref (poate fi 'favorit'/'if_bored'/'disliked')
        :rtype: str
        """
        no_eps = self.__show.get_no_eps()
        one_third = no_eps/3
        two_thirds = (no_eps*2)/3
        if self.__no_seen_eps > two_thirds:
            pref = 'favorit'
        elif two_thirds > self.__no_seen_eps > one_third:
            pref = 'if_bored'
        else:
            pref = 'disliked'
        return pref
