from termcolor import colored
from random import randint
import random, string
from repository.repo_errors import DuplicatePersonError, DuplicateEventError, AlreadySignedUpError, \
    EventNotFoundException, PersonNotFoundException


class Console:
    def __init__(self, people_service, events_service, signup_service):
        """
        Inițializează consola
        :type people_service: PeopleService
        :type events_service: EventService
        :type signup_service: SignUpService
        """
        self.__psrv = people_service
        self.__esrv = events_service
        self.__isrv = signup_service

    def __print_person(self, p):
        print('     ', p.getLastname(), p.getFirstname(), '- id:', p.getPID(), '- adresa: ', p.getAdress())

    def __print_all_people(self):
        """
        Afișează toate persoanele
        """
        people_list = self.__psrv.get_all_people()
        if len(people_list) == 0:
            print('Nu sunt persoane în listă.')
        else:
            k = 1
            print(colored('Persoanele sunt:', 'cyan'))
            for p in people_list:
                print('     ', k, '--', p.getLastname(),
                      p.getFirstname(), '- id:', p.getPID(), '- adresa: ', p.getAdress())
                k += 1

    def __print_event(self, e):
        print('     ', e.getDescription(), ' - id eveniment:', e.getEID(),
              '- data:', e.getDate(), '- ora:', e.getTime())

    def __print_all_events(self):
        """
        Afișează toate evenimentele
        """
        events_list = self.__esrv.get_all_events()
        if len(events_list) == 0:
            print('Nu sunt evenimente în listă.')
        else:
            k = 1
            print(colored('Evenimentele sunt:', 'cyan'))
            for e in events_list:
                print('     ', k, '--', e.getDescription(), ' - id eveniment:',
                      e.getEID(), '- data:', e.getDate(), '- ora:', e.getTime())
                k += 1

    def __print_all_signups(self):
        signups_list = self.__isrv.get_all_signups()
        if len(signups_list) == 0:
            print('Nu s-au realizat înscrieri.')
        else:
            for i in signups_list:
                print(f'    {i.getPerson().getLastname()} {i.getPerson().getFirstname()} '
                      f' este înscris(ă) la {i.getEvent().getDescription()}')

    def __print_people_by_name(self):
        people_list = self.__psrv.sort_people_by_name()
        if len(people_list) == 0:
            print('Nu sunt persoane în listă.')
        else:
            k = 1
            print(colored('Persoanele sunt:', 'cyan'))
            for p in people_list:
                print('     ', k, '--', p.getLastname(),
                      p.getFirstname(), '- id:', p.getPID(), '- adresa: ', p.getAdress())
                k += 1

    def __add_person(self):
        """
        Adaugă o persoană cu date citite de la tastatură.
        """
        try:
            pid = int(input('Id-ul persoanei: '))
            if pid < 0:
                raise ValueError
            firstname = input('Prenume: ')
            lastname = input('Nume: ')
            adress = input('Adresa: ')
            try:
                added_person = self.__psrv.add_person(pid, firstname, lastname, adress)
                print('Persoana', added_person.getLastname(), added_person.getFirstname(), 'a fost adăugată cu succes.')
            except ValueError as ve:
                print(colored(ve, 'red'))
            except DuplicatePersonError as dpe:
                print(colored(dpe, 'red'))
        except ValueError:
            print(colored('Id-ul trebuie să fie un număr natural', 'red'))

    def __add_event(self):
        """
        Adaugă un eveniment cu date citite de la tastatură.
        """
        try:
            eid = int(input('Id-ul evenimentului: '))
            if eid < 0:
                raise ValueError
            date = input('Data(în format zz/ll/aaaa): ')
            time = input('Ora(în format hh:mm): ')
            description = input('Descrierea evenimentului: ')
            try:
                added_event = self.__esrv.add_event(eid, date, time, description)
                print('Evenimentul', added_event.getDescription(), 'a fost adăugat cu succes.')
            except ValueError as ve:
                print(colored(ve, 'red'))
            except DuplicateEventError as dee:
                print(colored(dee, 'red'))
        except ValueError:
            print(colored('Id-ul trebuie să fie un număr natural', 'red'))

    def __delete_person(self):
        """
        Șterge o persoană din listă.
        """
        self.__print_all_people()
        if len(self.__psrv.get_all_people()) == 0:
            print('Nu există persoane care se pot șterge.')
        else:
            try:
                pid = int(input('ID-ul persoanei care va fi ștearsă: '))
                self.__psrv.delete_person(pid)
                print('Persoană ștearsă.')
                self.__isrv.remove_by_person(pid)
            except ValueError:
                print(colored('ID-ul trebuie să fie un număr.'))
            except PersonNotFoundException as pnfe:
                print(colored(pnfe, 'red'))

    def __delete_event(self):
        """
        Șterge un eveniment din listă.
        """
        self.__print_all_events()
        if len(self.__esrv.get_all_events()) == 0:
            print('Nu există evenimente care se pot șterge.')
        else:
            try:
                eid = int(input('ID-ul evenimentului care va fi ștears: '))
                self.__esrv.delete_event(eid)
                print('Eveniment ștears.')
            except ValueError:
                print(colored('ID-ul trebuie să fie un număr.'))
            except EventNotFoundException as enfe:
                print(colored(enfe, 'red'))

    def __modify_person(self):
        """
        Modifică datele unei persoane cu date citite de la tastatură.
        """
        self.__print_all_people()
        if len(self.__psrv.get_all_people()) == 0:
            print('Nu există persoane care se pot modifica.')
        else:
            try:
                pid = int(input('ID-ul persoanei care va fi modificată: '))
                firstname = input('Prenume: ')
                lastname = input('Nume: ')
                adress = input('Adresa: ')
                try:
                    self.__psrv.modify_person(pid, firstname, lastname, adress)
                    print('Persoană modificată.')
                except PersonNotFoundException as pnfe:
                    print(colored(pnfe, 'red'))
            except ValueError:
                print(colored('Id-ul trebuie să fie un număr.', 'red'))

    def __modify_event(self):
        """
        Modifică datele unui eveniment cu citire de la tastatură.
        """
        self.__print_all_events()
        if len(self.__esrv.get_all_events()) == 0:
            print('Nu există evenimente care se pot modifica.')
        else:
            try:
                eid = int(input('Id-ul evenimentului: '))
                date = input('Data(în format zz/ll/aaaa): ')
                time = input('Ora(în format hh:mm): ')
                description = input('Descrierea evenimentului: ')
                try:
                    self.__esrv.modify_event(eid, date, time, description)
                    print('Eveniment modificat.')
                except EventNotFoundException as enfe:
                    print(colored(enfe, 'red'))
            except ValueError:
                print(colored('Id-ul trebuie să fie un număr.', 'red'))

    def __find_person(self):
        """
        Caută o persoană
        """
        try:
            pid = int(input('Id-ul persoanei căutate: '))
            try:
                sp = self.__psrv.find_person(pid)
                self.__print_person(sp)
            except ValueError as ve:
                print(colored(ve, 'red'))
        except ValueError:
            print(colored('Id-ul trebuie să fie un număr.', 'red'))

    def __find_event(self):
        """
        Caută o persoană
        """
        try:
            eid = int(input('Id-ul evenimentului căutat: '))
            try:
                se = self.__esrv.find_event_with_recursivitate(eid)
                self.__print_event(se)
            except ValueError as ve:
                print(colored(ve, 'red'))
        except ValueError:
            print(colored('Id-ul trebuie să fie un număr.', 'red'))

    def __randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def __generate_people(self):
        """
        Generează entități persoană random.
        """
        try:
            x = int(input('Numărul de entități care se vor genera: '))
            if x < 0:
                raise ValueError
            for person in range(x):
                pid = randint(1000000000000, 9999999999999)
                fnl = randint(3, 10)
                firstname = self.__randomword(fnl).capitalize()
                lnl = randint(3, 12)
                lastname = self.__randomword(lnl).capitalize()
                cl = randint(3, 15)
                city = self.__randomword(cl).capitalize()
                sl = randint(10, 20)
                street = self.__randomword(sl).capitalize()
                snr = randint(10, 200)
                adress = ' ,'.join([city, street, str(snr)])
                try:
                    added_person = self.__psrv.add_person(pid, firstname, lastname, adress)
                    # print('Persoana', added_person.getLastname(), added_person.getFirstname(),
                    #      'a fost adăugată cu succes.')
                except ValueError as ve:
                    print(colored(ve, 'red'))
            print(colored('Generare reușită!', 'green'))
        except ValueError:
            print(colored('Trebuie să fie un număr natural.'))

    def __generate_events(self):
        """
        Generează entități persoană random.
        """
        try:
            x = int(input('Numărul de entități care se vor genera: '))
            if x < 0:
                raise ValueError
            for person in range(x):
                eid = randint(100000, 999999)
                day = randint(1, 31)
                month = str(randint(1, 12))
                year = randint(2022, 2025)
                if len(month) == 1:
                    month = ''.join(['0', month])
                date = '/'.join([str(day), month, str(year)])
                hour = randint(0, 23)
                minute = randint(0, 59)
                time = ':'.join([str(hour), str(minute)])
                desclen = randint(15, 50)
                description = self.__randomword(desclen).capitalize()
                try:
                    added_event = self.__esrv.add_event(eid, date, time, description)
                    # print('Evenimentul', added_event.getDescription(), 'a fost adăugat cu succes.')
                except ValueError as ve:
                    print(colored(ve, 'red'))
            print(colored('Generare reușită!', 'green'))
        except ValueError:
            print(colored('Trebuie să fie un număr natural.'))

    def __signup_to_event(self):
        """
        Înscrie o persoană la un eveniment.
        """
        self.__print_all_people()
        try:
            pid = int(input('Id-ul persoanei care se înscrie: '))
            person = self.__psrv.find_person(pid)
            self.__print_all_events()
            try:
                eid = int(input('Id-ul evenimentului la care se înscrie persoana: '))
                event = self.__esrv.find_event(eid)
                try:
                    self.__isrv.add_signup(person, event)
                    print(f'{person.getLastname()} {person.getFirstname()} '
                          f' a fost înscris(ă) la {event.getDescription()}')
                except AlreadySignedUpError as asue:
                    print(colored(asue, 'red'))
            except ValueError:
                print(colored('Id-ul evenimentului este invalid.', 'red'))
        except ValueError:
            print(colored('Id-ul persoanei este invalid.', 'red'))

    def __report_events_by_date(self):
        """
        Afișează toate evenimentele la care participă o anumită persoană ordonate după dată.
        """
        try:
            pid = int(input('Id-ul persoanei: '))
            events_list = self.__isrv.report_events_for_person_by_date(pid)
            print(f'{self.__psrv.find_person(pid).getLastname()} {self.__psrv.find_person(pid).getFirstname()}'
                  f' participă la: ')
            for e in events_list:
                self.__print_event(e)
        except ValueError:
            print(colored('Id-ul trebuie să fie număr.', 'red'))
        except PersonNotFoundException as pnfe:
            print(colored(pnfe, 'red'))

    def __report_events_by_desc(self):
        """
        Afișează toate evenimentele la care participă o anumită persoană ordonate alfabetic după descriere.
        """
        try:
            pid = int(input('Id-ul persoanei: '))
            events_list = self.__isrv.report_events_for_person_by_desc(pid)
            print(f'{self.__psrv.find_person(pid).getLastname()} {self.__psrv.find_person(pid).getFirstname()}'
                  f' participă la: ')
            for e in events_list:
                self.__print_event(e)
        except ValueError:
            print(colored('Id-ul trebuie să fie număr.', 'red'))
        except PersonNotFoundException as pnfe:
            print(colored(pnfe, 'red'))

    def __report_busy_people(self):
        """
        Afișează persoanele care sunt înscrise la cele mai multe evenimente.
        """
        people_list = self.__psrv.get_all_people()
        signup_track = self.__isrv.report_busy_people(people_list)
        max_events = signup_track[0][1]
        if max_events == 0:
            print('Persoanele nu sunt înscrise la niciun eveniment.')
        else:
            print('Persoanele care participă la cele mai multe evenimente sunt: ')
            for s in signup_track:
                if s[1] == max_events or s[1] == max_events-1:
                    print(self.__psrv.find_person(s[0]).getLastname(), self.__psrv.find_person(s[0]).getFirstname(),
                          'participă la', s[1], 'evenimente')

    def __report_succesful_events(self):
        """
        Afișează primele 20% de evenimente cu cei mai mulți particianți.
        """
        events_list = self.__esrv.get_all_events()
        nr_prints = len(events_list)//5
        signup_track = self.__isrv.report_succesful_events(events_list)
        if nr_prints == 0:
            print('Nu există suficiente evenimente pentru acest raport.')
        else:
            for i in range(nr_prints):
                print(self.__esrv.find_event(signup_track[i][0]).getDescription(),
                      'are', signup_track[i][1], 'participanți.')

    def __report_busy_dates(self):
        """
        Afișează primele 3 date cu cei mai mulți participanți.
        """
        first3 = list(self.__isrv.report_busy_dates().items())[:3]
        for i in first3:
            print(f'Data {i[0]} --- Număr de participanți: {i[1]}')

    def __print_menu(self, option=-1):
        if option == -1:
            print()
            print(colored('Introduceți cifra din dreptul comenzii dorite: ', 'yellow'))
            print('0 - Deschide submeniul', colored('Afișări', 'blue'))
            print('1 - Deschide submeniul', colored('Adăugări', 'blue'))
            print('2 - Deschide submeniul', colored('Ștergeri', 'blue'))
            print('3 - Deschide submeniul', colored('Modificări', 'blue'))
            print('4 - Deschide submeniul', colored('Căutări', 'blue'))
            print('5 -', colored('Înscrie persoană la eveniment', 'blue'))
            print('6 - Deschide submeniul', colored('Rapoarte', 'blue'))
            print('7 -', colored('Generare random', 'blue'))
            print('8 -', colored('Închide aplicația', 'blue'))
        if option == 0:
            print(colored('Afișări:', 'blue'))
            print('     1. Afișează lista de persoane')
            print('     2. Afișează lista de evenimente')
            print('     3. Afișează lista de înscrieri')
            print('     4. Afișează lista de persoane ordonată după nume, prenume')
            print('     5. Înapoi')
        if option == 1:
            print(colored('Adăugări:', 'blue'))
            print('     1. Adaugă o persoană')
            print('     2. Adaugă un eveniment')
            print('     3. Înapoi')
        if option == 2:
            print(colored('Ștergeri:', 'blue'))
            print('     1. Șterge datele unei persoane')
            print('     2. Șterge un eveniment')
            print('     3. Înapoi')
        if option == 3:
            print(colored('Modificări:', 'blue'))
            print('     1. Modifică datele unei persoane')
            print('     2. Modifică un eveniment')
            print('     3. Înapoi')
        if option == 4:
            print(colored('Căutări:', 'blue'))
            print('     1. Caută o persoană')
            print('     2. Caută un eveniment')
            print('     3. Înapoi')
        if option == 6:
            print(colored('Rapoarte: ', 'blue'))
            print('     1. Lista de evenimente la care participă o persoană ordonată după dată.')
            print('     2. Lista de evenimente la care participă o persoană ordonată alfabetic după descriere.')
            print('     3. Persoane participante la cele mai multe evenimente.')
            print('     4. Primele 20% evenimente cu cei mai mulți participanți.')
            print('     5. Zilele în care numărul de participanți e cel mai mare.')
            print('     6. Înapoi')
        if option == 7:
            print(colored('Generări:', 'blue'))
            print('     1. Generează persoane')
            print('     2. Generează evenimente')
            print('     3. Înapoi')

    def startui(self):
        """
        Interfața cu utilizatorul
        """
        while True:
            self.__print_menu()
            option = input('Introduceți opțiunea dorită: ')
            if option == '0':
                self.__print_menu(0)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__print_all_people()
                elif cmd == '2':
                    self.__print_all_events()
                elif cmd == '3':
                    self.__print_all_signups()
                elif cmd == '4':
                    self.__print_people_by_name()
                elif cmd == '5':
                    continue
            elif option == '1':
                self.__print_menu(1)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__add_person()
                elif cmd == '2':
                    self.__add_event()
                elif cmd == '3':
                    continue
            elif option == '2':
                self.__print_menu(2)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__delete_person()
                elif cmd == '2':
                    self.__delete_event()
                elif cmd == '3':
                    continue
            elif option == '3':
                self.__print_menu(3)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__modify_person()
                elif cmd == '2':
                    self.__modify_event()
                elif cmd == '3':
                    continue
            elif option == '4':
                self.__print_menu(4)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__find_person()
                elif cmd == '2':
                    self.__find_event()
                elif cmd == '3':
                    continue
            elif option == '5':
                self.__signup_to_event()
            elif option == '6':
                self.__print_menu(6)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__report_events_by_date()
                elif cmd == '2':
                    self.__report_events_by_desc()
                elif cmd == '3':
                    self.__report_busy_people()
                elif cmd == '4':
                    self.__report_succesful_events()
                elif cmd == '5':
                    self.__report_busy_dates()
                elif cmd == '6':
                    continue
            elif option == '7':
                self.__print_menu(7)
                cmd = input('Opțiune: ')
                if cmd == '1':
                    self.__generate_people()
                elif cmd == '2':
                    self.__generate_events()
                elif cmd == '3':
                    continue
            elif option == '8':
                return
            else:
                print(colored('Comandă invalidă!', 'red'))
