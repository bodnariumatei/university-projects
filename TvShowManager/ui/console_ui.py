from termcolor import colored

from exceptions.exceptions import ShowValidationException, DuplicateIdException, ShowNotFoundException


class ConsoleUI:
    def __init__(self, show_service):
        self.__show_service = show_service

    def __print_shows_list(self):
        shows_list = self.__show_service.get_all_shows()
        print(colored('Serialele sunt:', 'magenta'))
        for show in shows_list:
            print('     ', colored(show.get_title(), 'blue'), '(', show.get_show_id(), ') -- genul:',
                  show.get_genre(), '-- nr. de episoade:', show.get_no_eps())

    def __add_show(self):
        show_id = input('ID-ul serialului: ')
        title = input('Titlul serialului: ')
        genre = input('Genul serialului: ')
        try:
            no_eps = int(input('Numărul de episoade: '))
            self.__show_service.add_show(show_id, title, genre, no_eps)
        except ValueError:
            print(colored('Numărul de episoade trebuie să fie un număr natural.', 'red'))
        except ShowValidationException as sve:
            print(colored(sve, 'red'))
        except DuplicateIdException as die:
            print(colored(die, 'red'))

    def __search_by_genre(self):
        genre = input('Genul serialului: ')
        shows_by_genre = self.__show_service.search_by_genre(genre)
        if len(shows_by_genre) == 0:
            print('Nu sunt seriale din acest gen.')
        else:
            print(f'Seriale din genul {genre} sunt:')
            for show in shows_by_genre:
                print('     ', colored(show.get_title(), 'blue'), '(', show.get_show_id(), ') -- genul:',
                      show.get_genre(), '-- nr. de episoade:', show.get_no_eps())

    def __get_preference(self):
        self.__print_shows_list()
        show_id = input('ID-ul serialului: ')
        try:
            no_seen_eps = int(input('Numărul de episoade văzute: '))
            pref = self.__show_service.get_preference(show_id, no_seen_eps)
            print('Nivelul de preferință pentru serialul cu id-ul dat este:', colored(pref, 'blue'))
        except ValueError:
            print(colored('Numărul de episoade trebuie să fie un număr natural.', 'red'))
        except ShowNotFoundException as snfe:
            print(colored(snfe, 'red'))

    def __print_commands(self):
        print(colored('Comenzile disponibile sunt:', 'yellow'))
        print('     ', colored('print_shows', 'cyan'), '- afișează toate serialele')
        print('     ', colored('add_show', 'cyan'), '- adaugă un serial nou')
        print('     ', colored('search_by_genre', 'cyan'), '- caută show-uri după gen')
        print('     ', colored('get_preference', 'cyan'), '- afișează preferința pentru un serial')
        print('     ', colored('close_app', 'cyan'), '- închide aplicația')
        print()

    def start_ui(self):
        while True:
            self.__print_commands()
            cmd = input('Comanda dorită este: ')
            if cmd == 'print_shows':
                self.__print_shows_list()
            elif cmd == 'add_show':
                self.__add_show()
            elif cmd == 'search_by_genre':
                self.__search_by_genre()
            elif cmd == 'get_preference':
                self.__get_preference()
            elif cmd == 'close_app':
                return
