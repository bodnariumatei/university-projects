from domain.entities import Person, Event
from repository.repo_errors import DuplicatePersonError, DuplicateEventError, EventNotFoundException, \
    PersonNotFoundException


class PeopleRepository:
    """
    Clasă cu responsabilitatea de a gestiona lista de persoane.
    """
    def __init__(self):
        # people - lista de persoane
        self.__people = []

    def store(self, person):
        """
        Adaugă o persoană în lista de persoane.
        :param person: persoana care se adaugă
        :type person: Person
        :return: - ; se modifică lista
        :rtype: -
        :raises: DuplicatePersonError dacă persoana există deja în listă
        """
        for p in self.__people:
            if p == person:
                raise DuplicatePersonError('Persoana se află deja în listă!')
        self.__people.append(person)

    def get_all_people(self):
        """
        Furnizeză lista de persoane.
        :return: people - lista de persoane
        :rtype: list
        """
        return self.__people

    def delete(self, pid):
        """
        Șterge o persoană din listă.
        :param pid: id-ul persoanei care trebuie ștearsă
        :type pid: int
        :raises: PersonNotFoundException dacă nu există persoană cu id-ul furnizat
        """
        index = -1
        ok = 0
        for p in self.__people:
            index += 1
            if p.getPID() == pid:
                ok = 1
                break
        if ok == 1:
            self.__people.pop(index)
        else:
            raise PersonNotFoundException('Nu există persoană cu acest id.')

    def modify(self, pid, mod_person):
        """
        Modifică datele unei persoane existente.
        :param pid: id-ul persoanei care se modifică
        :type pid: int
        :param mod_person: datele modificate ale persoanei
        :type mod_person: Person
        :raises: PersonNotFoundException dacă nu există persoană cu id-ul furnizat
        """
        index = -1
        ok = 0
        for p in self.__people:
            index += 1
            if p.getPID() == pid:
                ok = 1
                break
        if ok == 1:
            self.__people[index] = mod_person
        else:
            raise PersonNotFoundException('Nu există personă cu acest id.')

    def find(self, pid):
        """
        Caută o persoană.
        :param pid: id-ul persoanei căutate
        :type pid: int
        :return: person - persoana căutată
        :rtype: Person
        ridică ValueError dacă persoana cu id-ul furnizat nu există
        """
        for person in self.__people:
            if person.getPID() == pid:
                return person
        raise ValueError('Nu există persoana cu id-ul introdus.')

    def remove_all(self):
        """
        Golește repozitorul
        """
        self.__people = []


class EventsRepository:
    """
    Clasă cu responsabilitatea de a gestiona lista de evenimente.
    """
    def __init__(self):
        # events - lista de evenimente
        self.__events = []

    def store(self, event):
        """
        Adaugă un eveniment în listă.
        :param event: evenimentul care se adaugă
        :type event: Event
        :return: - ; se nodifică lista
        :rtype: -
        :raises: DuplicateEventError dacă evenimnetul a fost deja înregistrat
                (dacă se alfă deja în listă un eveniment cu același id)
        """
        for e in self.__events:
            if e == event:
                raise DuplicateEventError('Evenimentul este deja înregistrat!')
        self.__events.append(event)

    def get_all_events(self):
        """
        Returnează lista cu toate evenimentele.
        :return: events - lista de evenimente
        :rtype: list
        """ 
        return self.__events

    def delete(self, eid):
        """
        Șterge un eveniment din listă.
        :param eid: id-ul evenimentului care trebuie ștears
        :type eid: int
        :raises: EventNotFoundException dacă id-ul furnizat nu corespunde niciunui eveniment
        """
        index = -1
        ok = 0
        for e in self.__events:
            index += 1
            if e.getEID() == eid:
                ok = 1
                break
        if ok == 1:
            self.__events.pop(index)
        else:
            raise EventNotFoundException('Nu există eveniment cu acest id.')

    def modify(self, eid, mod_event):
        """
        Modifică datele unui eveniment existent.
        :param eid: id-ul evenimentului care se modifică
        :type eid: int
        :param mod_event: datele modificate ale evenimentului
        :type mod_event: Event
        """
        index = -1
        ok = 0
        for e in self.__events:
            index += 1
            if e.getEID() == eid:
                ok = 1
                break
        if ok == 1:
            self.__events[index] = mod_event
        else:
            raise EventNotFoundException('Nu există eveniment cu acest id.')

    def find(self, eid):
        """
        Caută un eveniment.
        :param eid: id-ul evenimentului
        :type eid: int
        :return: event - evenimentul căutat
        :rtype: Event
        ridică ValueError dacă evenimentul cu id-ul furnizat nu există
        """
        for event in self.__events:
            if event.getEID() == eid:
                return event
        raise ValueError('Nu există evenimentul cu id-ul introdus.')

    def find_recursiv(self, eid, index):
        """
        Caută un eveniment.
        :param eid: id-ul evenimentului
        :type eid: int
        :return: event - evenimentul căutat
        :rtype: Event
        ridică ValueError dacă evenimentul cu id-ul furnizat nu există
        """
        if self.__events[index].getEID() == eid:
            return self.__events[index]
        if index == -1:
            raise ValueError('Nu există evenimentul cu id-ul introdus.')
        return self.find_recursiv(eid, index-1)

    def remove_all(self):
        """
        Golește repozitorul
        """
        self.__events = []


def test_store_getall_people():
    prepo = PeopleRepository()
    p1 = Person(1234567891523, 'John', 'Doe', 'Cluj-Napoca, str. Nufărului, nr.24')
    prepo.store(p1)
    plist1 = prepo.get_all_people()
    assert (len(plist1) == 1)
    assert (plist1[0] == p1)
    p2 = Person(8934569743323, 'Oliver', 'Twist', 'Cluj-Napoca, str. Charles Dickiens, nr.37')
    prepo.store(p2)
    plist2 = prepo.get_all_people()
    assert (len(plist2) == 2)
    assert (plist2[0] == p1)
    assert (plist2[1] == p2)


def test_delete_person():
    prepo = PeopleRepository()
    p1 = Person(1234567891523, 'John', 'Doe', 'Cluj-Napoca, str. Nufărului, nr.24')
    p2 = Person(3214569743323, 'Oliver', 'Twist', 'Cluj-Napoca, str. Charles Dickiens, nr.37')
    prepo.store(p1)
    prepo.store(p2)
    plist = prepo.get_all_people()
    assert (len(plist) == 2)
    assert (plist[0] == p1)
    prepo.delete(1234567891523)
    plist = prepo.get_all_people()
    assert(len(plist) == 1)
    assert(plist[0] == p2)
    prepo.delete(3214569743323)
    plist = prepo.get_all_people()
    assert (len(plist) == 0)


def test_find_person():
    prepo = PeopleRepository()
    p1 = Person(1234567891523, 'John', 'Doe', 'Cluj-Napoca, str. Nufărului, nr.24')
    p2 = Person(3214569743323, 'Oliver', 'Twist', 'Cluj-Napoca, str. Charles Dickiens, nr.37')
    prepo.store(p1)
    prepo.store(p2)
    pf = prepo.find(1234567891523)
    assert (pf == p1)
    try:
        ps = prepo.find(9876543210142)
        assert False
    except ValueError:
        assert True


def test_store_getall_events():
    erepo = EventsRepository()
    e1 = Event(12412, '20/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    erepo.store(e1)
    elist1 = erepo.get_all_events()
    assert (len(elist1) == 1)
    assert (elist1[0] == e1)
    e2 = Event(73432, '23/11/2021', '13:00', 'Festivalul iernii, ...')
    erepo.store(e2)
    elist2 = erepo.get_all_events()
    assert (len(elist2) == 2)
    assert (elist1[0] == e1)
    assert (elist2[1] == e2)


def test_delete_event():
    erepo = EventsRepository()
    e1 = Event(12412, '20/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    erepo.store(e1)
    e2 = Event(73432, '23/11/2021', '13:00', 'Festivalul iernii, ...')
    erepo.store(e2)
    elist = erepo.get_all_events()
    assert (len(elist) == 2)
    assert (elist[0] == e1)
    erepo.delete(73432)
    elist = erepo.get_all_events()
    assert (len(elist) == 1)
    assert (elist[0] == e1)
    erepo.delete(12412)
    elist = erepo.get_all_events()
    assert (len(elist) == 0)


def test_find_event():
    erepo = EventsRepository()
    e1 = Event(12412, '20/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    e2 = Event(73432, '23/11/2021', '13:00', 'Festivalul iernii, ...')
    erepo.store(e1)
    erepo.store(e2)
    ef = erepo.find(12412)
    assert (ef == e1)
    try:
        es = erepo.find(98765)
        assert False
    except ValueError:
        assert True


test_store_getall_people()
test_delete_person()
test_find_person()
test_store_getall_events()
test_delete_event()
test_find_event()
