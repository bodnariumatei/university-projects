from domain.entities import TvShow
from exceptions.exceptions import DuplicateIdException, ShowNotFoundException


class ShowFileRepo:
    """
    Stochează/ scoate datele despre show-uri din/în fișier.
    """
    def __init__(self, filename):
        """
        Inițializăm repozitorul cu fișier
        :param filename: numele fișierului în care sunt stocate datele
        """
        self.__filename = filename
        self.__show_list = []
        self.__load_from_file()

    def __load_from_file(self):
        """
        Încarcă datele din fișier în program
        :return: -
        :raise: CorruptedFileException dacă apare vreo eroare când se citește din fișier
        """
        try:
            file = open(self.__filename, 'r')
        except IOError:
            # Eroare la deschidere
            return
        self.__show_list = []
        line = file.readline().strip()
        while line != "":
            atributes = line.split(',')
            show = TvShow(atributes[0].strip(), atributes[1].strip(), atributes[2].strip(), int(atributes[3]))
            self.__show_list.append(show)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        """
        Scrie datele despre show-uri în fișier.
        :return: -
        """
        try:
            file = open(self.__filename, 'w')
        except IOError:
            return
        for show in self.__show_list:
            sf = show.get_show_id() + ', ' + show.get_title() + ', ' + show.get_genre() + ', ' + str(show.get_no_eps())
            sf = sf + '\n'
            file.write(sf)
        file.close()

    def store(self, show):
        """
        Stochează un show
        :param show: show-ul dat
        :type show: TvShow
        :return: -
        :raise: DuplicateIdException dacă se află deja în listă un serial cu același id.
        """
        for s in self.__show_list:
            if show.get_show_id() == s.get_show_id():
                raise DuplicateIdException('Atenție ID duplicat!')
        self.__show_list.append(show)
        self.__store_to_file()

    def get_all(self):
        """
        Returnează o listă cu toate show-urile
        :return: shows_list - lista cu toate serialele
        :rtype: list of TvShow objects
        """
        shows_list = self.__show_list
        return shows_list

    def find(self, show_id):
        """
        Returnează serialul cu id-ul dat
        :param show_id: id-ul serialului căutat
        :return: show - serialul căutat
        :rtype: TvShow
        :raise: ShowNotFoundException dacă nu se găsește serial cu id-ul dat
        """
        for show in self.__show_list:
            if show.get_show_id() == show_id:
                return show
        raise ShowNotFoundException('Nu există serial cu id-ul dat.')

    def get_shows_by_genre(self, genre):
        """
        Returnează o listă cu toate serialele care contin în atributul gen șirul din 'genre'
        :param genre: genul care se caută
        :type genre: str
        :return: show_of_genre - lista cu seriale de un anumit gen
        :rtype: list (of TvShow objects)
        """
        shows_of_genre = []
        for show in self.__show_list:
            if genre.lower() in show.get_genre().lower():
                shows_of_genre.append(show)
        return shows_of_genre
