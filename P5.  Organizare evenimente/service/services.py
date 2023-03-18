from repository.repos import PeopleRepository, EventsRepository
from domain.entities import Person, Event
from domain.validators import PersonValidator, EventValidator
from utils.sortings import selection_sort, selection_sort_recursive


class PeopleService:
    """
    Coordoneaza operatiile necesare pentru a realiza actiunea declansata de
    utilizator cu efect asupra listei de persoane.
    """

    def __init__(self, p_repo, p_validator):
        """
        Inițializează service
        :param p_repo: obiect de tip repository care ne ajută la gestionarea mulțimii de persoane.
        :type p_repo: PeopleRepository
        :param p_validator: validator pentru verificarea persoanelor
        :type p_validator: PersonValidator
        """
        self.__repo = p_repo
        self.__validator = p_validator

    def add_person(self, pid, firstname, lastname, adress):
        """
        Adaugă persoană
        :param pid: ID-ul persoanei adăugate
        :type pid: int
        :param lastname: numele persoanei
        :type lastname: str
        :param firstname: prenumele persoanei
        :type firstname: str
        :param adress: adresa persoanei
        :type adress: str
        return: obiectul de tip Person creat
        :rtype:-; persoana s-a adaugat in lista
        :raises: ValueError daca datele sunt invalide
                 DuplicatePersonError dacă persoana se află deja în listă
        """
        p = Person(pid, firstname, lastname, adress)
        self.__validator.validate_person(p)
        self.__repo.store(p)
        return p

    def get_all_people(self):
        """
        Returneaza o lista cu toate persoanele
        :return: lista cu persoane
        :rtype: list of objects de tip Person
        """
        return self.__repo.get_all_people()

    def delete_person(self, pid):
        """
        Șterge o persoană din listă.
        :param pid: id-ul persoanei care trebuie ștearsă
        :type pid: int
        """
        self.__repo.delete(pid)

    def modify_person(self, pid, firstname, lastname, adress):
        """
        Modifică datele unei persoane
        :param pid: ID-ul persoanei care va fi modificată
        :type pid: int
        :param lastname: numele persoanei
        :type lastname: str
        :param firstname: prenumele persoanei
        :type firstname: str
        :param adress: adresa persoanei
        :type adress: str
        :return: obiectul de tip Person creat
        :rtype:-; persoana s-a adaugat in lista
        :raises: ValueError daca datele sunt invalide
        """
        p = Person(pid, firstname, lastname, adress)
        self.__validator.validate_person(p)
        self.__repo.modify(pid, p)

    def find_person(self, pid):
        """
        Găsește o persoană după id-ul său.
        :param pid: id-ul persoanei căutate
        :type pid: int
        :return: persoana căutată
        :rtype: Person
        ridică ValueError dacă persoana cu id-ul furnizat nu există
        """
        p = self.__repo.find(pid)
        return p

    def sort_people_by_name(self):
        """
        Returnează lista cu toate persoanele ordonată după nume, apoi prenume în caz de egalitate.
        """
        def cmp_names(p1, p2):
            if p1.getLastname() == p2.getLastname():
                return p1.getFirstname() > p2.getFirstname()
            return p1.getLastname() > p2.getLastname()

        people = self.__repo.get_all_people()
        sorted_people = selection_sort_recursive(people, len(people)-1, cmp=cmp_names)
        return sorted_people

class EventService:
    """
    Coordoneaza operatiile necesare pentru a realiza actiunea declansata de
    utilizator cu efect asupra listei de evenimente.
    """

    def __init__(self, e_repo, e_validator):
        """
        Inițializează service
        :param e_repo: obiect de tip repository care ne ajută la gestionarea mulțimii de evenimente.
        :type e_repo: EventsRepository
        :param e_validator: validator pentru verificarea evenimentelor
        :type e_validator: EventValidator
        """
        self.__repo = e_repo
        self.__validator = e_validator

    def add_event(self, eid, date, time, description):
        """
        Adaugă eveniment
        :param eid: ID-ul evenimentului adăugat
        :type eid: int
        :param time: ora de desfășurare a evenimentului
        :type time: str
        :param date: data la cere se desfășoară evenimentul
        :type date: str
        :param description: descrierea evenimentului
        :type description: str
        return: obiectul de tip Event creat
        :rtype:-; evenimentul s-a adaugat in lista
        :raises: ValueError daca datele sunt invalide
                DuplicateEventError dacă evenimentul se află deja în listă
        """
        e = Event(eid, date, time, description)
        self.__validator.validate_event(e)
        self.__repo.store(e)
        return e

    def get_all_events(self):
        """
        Returneaza o lista cu toate evenimentele
        :return: lista cu evenimente
        :rtype: list of objects de tip Event
        """
        return self.__repo.get_all_events()

    def delete_event(self, eid):
        """
        Șterge un eveniment din listă.
        :param eid: id-ul evenimentului care trebuie ștears
        :type eid: int
        """
        self.__repo.delete(eid)

    def modify_event(self, eid, date, time, description):
        """
        Modifică eveniment
        :param eid: ID-ul evenimentului care va fi modificat
        :type eid: int
        :param time: ora de desfășurare a evenimentului
        :type time: str
        :param date: data la cere se desfășoară evenimentul
        :type date: str
        :param description: descrierea evenimentului
        :type description: str
        return: obiectul de tip Event creat
        :rtype:-; evenimentul s-a adaugat in lista
        :raises: ValueError daca datele sunt invalide
        """
        e = Event(eid, date, time, description)
        self.__validator.validate_event(e)
        self.__repo.modify(eid, e)

    def find_event(self, eid):
        """
        Găsește un eveniment după id-ul său.
        :param eid: id-ul evenimentului căutat
        :type eid: int
        :return: evenimentul căutat
        :rtype: Event
        ridică ValueError dacă evenimentul cu id-ul furnizat nu există
        """
        e = self.__repo.find(eid)
        return e

    def find_event_with_recursivitate(self, eid):
        """
        Găsește un eveniment după id-ul său.
        :param eid: id-ul evenimentului căutat
        :type eid: int
        :return: evenimentul căutat
        :rtype: Event
        ridică ValueError dacă evenimentul cu id-ul furnizat nu există
        """
        lungime = len(self.__repo.get_all_events())
        e = self.__repo.find_recursiv(eid, lungime-1)
        return e


def test_add_person():
    prepo = PeopleRepository()
    pval = PersonValidator()
    psrv = PeopleService(prepo, pval)
    psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
    try:
        psrv.add_person(154215, '', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        assert False
    except ValueError:
        assert True
    try:
        psrv.add_person(516555, 'John', '', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        assert False
    except ValueError:
        assert True
    try:
        psrv.add_person(516555, 'John', 'Doe', 'Suceava')
        assert False
    except ValueError:
        assert True


def test_get_all_people():
    prepo = PeopleRepository()
    pval = PersonValidator()
    psrv = PeopleService(prepo, pval)
    p_list = psrv.get_all_people()
    assert (p_list == [])
    assert (len(p_list) == 0)
    psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
    p_list = psrv.get_all_people()
    assert (len(p_list) == 1)
    psrv.add_person(615649, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
    psrv.add_person(567415, 'David', 'Copperfield', 'Suceava, str. Mihai Eminescu, nr.24')
    psrv.add_person(125615, 'Bernard', 'Rieux', 'București, str. Dorobanților, nr.16')
    p_list = psrv.get_all_people()
    assert (len(p_list) == 4)


def test_delete_person():
    prepo = PeopleRepository()
    pval = PersonValidator()
    psrv = PeopleService(prepo, pval)
    psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
    psrv.add_person(615649, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
    psrv.add_person(924715, 'David', 'Copperfield', 'Suceava, str. Mihai Eminescu, nr.24')
    psrv.add_person(187415, 'Bernard', 'Rieux', 'București, str. Dorobanților, nr.16')
    p_list = psrv.get_all_people()
    assert (len(p_list) == 4)
    psrv.delete_person(924715)
    p_list = psrv.get_all_people()
    assert (len(p_list) == 3)
    psrv.delete_person(615649)
    psrv.delete_person(465415)
    psrv.delete_person(187415)
    p_list = psrv.get_all_people()
    assert (len(p_list) == 0)


def test_modify_person():
    prepo = PeopleRepository()
    pval = PersonValidator()
    psrv = PeopleService(prepo, pval)
    psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
    p_list = psrv.get_all_people()
    assert (p_list[0].getPID() == 465415)
    assert (p_list[0].getFirstname() == 'John')
    assert (p_list[0].getLastname() == 'Doe')
    assert (p_list[0].getAdress() == 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
    psrv.modify_person(465415, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
    p_list = psrv.get_all_people()
    assert (p_list[0].getPID() == 465415)
    assert (p_list[0].getFirstname() == 'Oliver')
    assert (p_list[0].getLastname() == 'Twist')
    assert (p_list[0].getAdress() == 'Cluj-Napoca, str. Teodor Mihaly, nr.65')


def test_find_person():
    prepo = PeopleRepository()
    pval = PersonValidator()
    psrv = PeopleService(prepo, pval)
    psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
    psrv.add_person(615649, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
    try:
        p1 = psrv.find_person(465415)
        assert True
    except ValueError:
        assert False
    try:
        p1 = psrv.find_person(987652)
        assert False
    except ValueError:
        assert True


def test_add_event():
    erepo = EventsRepository()
    evali = EventValidator()
    esrv = EventService(erepo, evali)
    esrv.add_event(2548, '9/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    try:
        esrv.add_event(5515, '9.11.2021', '18:30', 'Gala oamenilor de treabă, ...')
        assert False
    except ValueError:
        assert True
    try:
        esrv.add_event(5648, '9/11/2021', '18', 'Gala oamenilor de treabă, ...')
        assert False
    except ValueError:
        assert True


def test_get_all_events():
    erepo = EventsRepository()
    evali = EventValidator()
    esrv = EventService(erepo, evali)
    e_list = esrv.get_all_events()
    assert (e_list == [])
    assert (len(e_list) == 0)
    esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    e_list = esrv.get_all_events()
    assert (len(e_list) == 1)
    esrv.add_event(5654, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
    esrv.add_event(2176, '14/11/2021', '14:30', 'Sesiune de relaxare cu soare, ...')
    e_list = esrv.get_all_events()
    assert (len(e_list) == 3)


def test_delete_event():
    erepo = EventsRepository()
    evali = EventValidator()
    esrv = EventService(erepo, evali)
    esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    esrv.add_event(5654, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
    esrv.add_event(2176, '14/11/2021', '14:30', 'Sesiune de relaxare cu soare, ...')
    e_list = esrv.get_all_events()
    assert (len(e_list) == 3)
    esrv.delete_event(2176)
    e_list = esrv.get_all_events()
    assert (len(e_list) == 2)
    esrv.delete_event(5654)
    esrv.delete_event(2548)
    e_list = esrv.get_all_events()
    assert (len(e_list) == 0)


def test_modify_event():
    erepo = EventsRepository()
    evali = EventValidator()
    esrv = EventService(erepo, evali)
    esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    e_list = esrv.get_all_events()
    assert (e_list[0].getEID() == 2548)
    assert (e_list[0].getDate() == '12/11/2021')
    assert (e_list[0].getTime() == '18:30')
    assert (e_list[0].getDescription() == 'Gala oamenilor de treabă, ...')
    esrv.modify_event(2548, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
    e_list = esrv.get_all_events()
    assert (e_list[0].getEID() == 2548)
    assert (e_list[0].getDate() == '18/11/2021')
    assert (e_list[0].getTime() == '12:00')
    assert (e_list[0].getDescription() == 'Prânz și muzică bună, ...')


def test_find_event():
    erepo = EventsRepository()
    evali = EventValidator()
    esrv = EventService(erepo, evali)
    esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    esrv.add_event(5654, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
    e1 = esrv.find_event(2548)
    assert (e1 == Event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...'))
    try:
        e1 = esrv.find_event(9876)
        assert False
    except ValueError:
        assert True


test_add_person()
test_get_all_people()
test_delete_person()
test_modify_person()
test_find_person()

test_add_event()
test_get_all_events()
test_delete_event()
test_modify_event()
test_find_event()
