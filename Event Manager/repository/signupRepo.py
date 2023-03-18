from domain.entities import SignUp, Person, Event
from repository.repo_errors import AlreadySignedUpError, PersonNotFoundException, EventNotFoundException


class SignUpRepository:
    """
    Clasă cu rolul de a gestiona înscrierile la evenimente.
    """
    def __init__(self):
        self.__sign_up_list = []

    def store(self, sign_up):
        """
        Adaugă în lista de înscrieri o înscriere.
        :param sign_up: înscrerea care se adaugă
        :type sign_up: SignUp
        raises AlreadySignedUpError dacă persoana s-a înscris la eveniment deja
        """
        pid = sign_up.getPerson().getPID()
        eid = sign_up.getEvent().getEID()
        for i in self.__sign_up_list:
            if i.getPerson().getPID() == pid and i.getEvent().getEID() == eid:
                raise AlreadySignedUpError('Persoana a fost deja înscrisă la eveniment.')
        self.__sign_up_list.append(sign_up)

    def get_all(self):
        """
        Returnează lista cu toate înscrierile.
        """
        return self.__sign_up_list

    def remove_for_person(self, pid):
        """
        Șterge toate înscrierile unei persoane.
        :param pid: id-ul persoanei pentru care se șterg înscrierile
        :type pid: int
        """
        k = len(self.__sign_up_list) - 1
        i = 0
        while i <= k:
            if self.__sign_up_list[i].getPerson().getPID() == pid:
                self.__sign_up_list.pop(i)
                k -= 1
            else:
                i += 1

    def remove_for_event(self, eid):
        """
        Șterge toate înscrierile la un eveniment.
        :param eid: id-ul evenimentului pentru care se șterg înscrierile
        :type eid: int
        """
        k = len(self.__sign_up_list) - 1
        i = 0
        while i <= k:
            if self.__sign_up_list[i].getEvent().getEID() == eid:
                self.__sign_up_list.pop(i)
                k -= 1
            else:
                i += 1

    def get_events_for_person(self, pid):
        """
        Returnează lista cu toate evenimentele la care participă o persoană.
        :param pid: id-ul persoanei pentru care se caută lista de evenimente.
        :type pid: int
        :return: events_list - lista evenimentelor la care participă persoana cu id-ul 'pid'
        :rtype: list (of Event objects)
        """
        events_list = []
        ok = 0
        for i in self.__sign_up_list:
            if i.getPerson().getPID() == pid:
                events_list.append(i.getEvent())
                ok = 1
        if ok == 1:
            return events_list
        raise PersonNotFoundException('Persoana nu este înscrisă la niciun eveniment.')

    def get_people_for_event(self, eid):
        """
        Returnează lista cu toate persoanele la care participă la un eveniment.
        :param eid: id-ul evenimnetului pentru care se caută lista de personae participante.
        :type eid: int
        :return: people_list - lista persoanelor care participă la evenimentul cu id-ul 'eid'
        :rtype: list (of Person objects)
        """
        people_list = []
        ok = 0
        for i in self.__sign_up_list:
            if i.getEvent().getEID() == eid:
                people_list.append(i.getPerson())
                ok = 1
        if ok == 1:
            return people_list
        raise EventNotFoundException('Nu există persoane înscrise la acest eveniment.')

    def remove_all(self):
        self.__sign_up_list = []


def test_store_getall():
    irepo = SignUpRepository()
    person = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    sign_up = SignUp(person, event)
    irepo.store(sign_up)
    sign_up_list = irepo.get_all()
    assert (len(sign_up_list) == 1)
    assert (sign_up_list[0] == sign_up)
    try:
        irepo.store(sign_up)
        assert False
    except AlreadySignedUpError:
        assert True


def test_remove_for_person():
    irepo = SignUpRepository()
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    irepo.store(SignUp(person1, event1))
    event2 = Event(5643, '30/11/2021', '13:00', 'Eveniment')
    irepo.store(SignUp(person1, event2))
    sign_up_list = irepo.get_all()
    assert(len(sign_up_list) == 2)
    irepo.remove_for_person(1531235)
    sign_up_list = irepo.get_all()
    assert (len(sign_up_list) == 0)


def test_remove_for_event():
    irepo = SignUpRepository()
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    person2 = Person(3463446, 'Oliver', 'Twist', 'oras, strada, numar')
    event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    irepo.store(SignUp(person1, event))
    irepo.store(SignUp(person2, event))
    sign_up_list = irepo.get_all()
    assert(len(sign_up_list) == 2)
    irepo.remove_for_event(1243)
    sign_up_list = irepo.get_all()
    assert (len(sign_up_list) == 0)


def test_get_events_for_person():
    irepo = SignUpRepository()
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    event2 = Event(5643, '30/11/2021', '13:00', 'Eveniment')
    irepo.store(SignUp(person1, event1))
    irepo.store(SignUp(person1, event2))
    events_for_person = irepo.get_events_for_person(1531235)
    assert (len(events_for_person) == 2)
    try:
        events_for_person = irepo.get_events_for_person(3253235324234)
        assert False
    except PersonNotFoundException:
        assert True


def test_get_people_for_event():
    irepo = SignUpRepository()
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    person2 = Person(3463446, 'Oliver', 'Twist', 'oras, strada, numar')
    event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    irepo.store(SignUp(person1, event))
    irepo.store(SignUp(person2, event))
    people_list = irepo.get_people_for_event(1243)
    assert (len(people_list) == 2)
    try:
        people_list = irepo.get_people_for_event(311341)
        assert False
    except EventNotFoundException:
        assert True


test_store_getall()
test_remove_for_person()
test_remove_for_event()
test_get_events_for_person()
test_get_people_for_event()
