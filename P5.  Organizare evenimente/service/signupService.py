from domain.entities import SignUp, Person, Event
from repository.repo_errors import AlreadySignedUpError, PersonNotFoundException, EventNotFoundException
from repository.signupRepo import SignUpRepository
from utils.sortings import selection_sort, shake_sort


class SignUpService:
    """
    Coordoneaza operatiile necesare pentru a realiza actiunea declanșată de
    utilizator cu efect asupra listei de înscrieri.
    """
    def __init__(self, i_repo):
        """
        Inițializează service
        :param i_repo: obiect de tip repository care ne ajută la gestionarea listei de înscreri.
        :type i_repo: SignUpRepository
        """
        self.__irepo = i_repo

    def add_signup(self, person, event):
        """
        Adaugă o înscrere în lista de înscrieri. / Înscrie o persoană la un eveniment.
        :param person: persoana care se înscrie la evenimnet
        :type person: Person
        :param event: evenimnetul la care se înscrie
        :type event: Event
        :raises: AlreadySignedUpError dacă înscrierea a fost deja efectuată.
        """
        sign_up = SignUp(person, event)
        self.__irepo.store(sign_up)

    def get_all_signups(self):
        """
        Returnează lista cu toate înscrierile.
        """
        return self.__irepo.get_all()

    def remove_by_person(self, pid):
        """
        Șterge toate înscrierile pentru o persoană.
        :param pid: id-ul persoanei pentru care se șterg înregistrările
        :type pid: int
        """
        self.__irepo.remove_for_person(pid)

    def remove_by_event(self, eid):
        """
        Șterge toate înscrierile la un eveniment anume.
        :param eid: id-ul evenimentului pentru care se șterg înregistrările
        :type eid: int
        """
        self.__irepo.remove_for_event(eid)

    def __date_to_comparable_string(self, e):
        """
        Transformă data unui eveniment primită din formatul 'dd/ll/aaaa' în 'aaaalldd' și returnează acest rezultat.
        Transformarea este necesară pentru compararea datelor evenimentelor între ele.
        :param e: eveniment
        :type e: Event
        :return: compare_date - data în formatul modificat
        :rtype: str
        """
        date = e.getDate()
        date_string = date.split('/')
        date_string.reverse()
        compare_date = ''.join(date_string)
        return compare_date

    def report_events_for_person_by_date(self, pid):
        """
        Returnează lista de evenimnete la care participă o persoană ordonată după dată.
        :param pid: id-ul persoanei
        :type pid: int
        :return: events_list_by_date - lista de evenimente la care participă persoana cu id-ul 'pid'
                ordonate după dată
        :rtype: list (of Event objects)
        :raises: PersonNotFoundException dacă nu exită persoană cu id-ul 'pid'.
        """
        events_list = self.__irepo.get_events_for_person(pid)
        return selection_sort(events_list, key=self.__date_to_comparable_string)

    def __description_of_event(self, e):
        return e.getDescription()

    def report_events_for_person_by_desc(self, pid):
        """
        Returnează lista de evenimente la care participă o persoană ordonată alfabetic după descriere.
        :param pid: id-ul persoanei
        :type pid: int
        :return: events_list_by_desc - lista de evenimente la care participă persoana cu id-ul 'pid'
                ordonate alfabetic după descriere
        :rtype: list (of Event objects)
        :raises: PersonNotFoundException dacă nu exită persoană cu id-ul 'pid'.
        """
        events_list = self.__irepo.get_events_for_person(pid)
        return selection_sort(events_list, key=self.__description_of_event)

    def __number_of_events(self, pe):
        return pe[1]

    def report_busy_people(self, list_of_people):
        """
        Returnează o listă din perechi formate din id-urile persoanelor
        și numărul de evenimente la care participă fiecare.
        :param list_of_people: lista de persoane
        :type list_of_people: list (of Person objects)
        :return: signup_track - listă de perechi formate din id-ul persoanei și numărul de evenimente
                 la care participă ordonate descrescător după numărul de evenimente.
        :rtype: list
        """
        signup_track = []
        for p in list_of_people:
            try:
                signup_track.append([p.getPID(), len(self.__irepo.get_events_for_person(p.getPID()))])
            except PersonNotFoundException:
                signup_track.append([p.getPID(), 0])
        return shake_sort(signup_track, reversed=True, key=self.__number_of_events)

    def report_succesful_events(self, list_of_events):
        """
        Returnează o listă din perechi formate din id-urile evenimentelor și numărul de participanți al fiecăruia.
        :param list_of_events: lista de evenimente
        :type list_of_events: list (of Event objects)
        :return: signup_track - listă de perechi formate din id-ul evenimentului și numărul de participanți
                 ordonate descrescător după numărul de participanți.
        :rtype: list
        """
        signup_track = []
        for e in list_of_events:
            try:
                signup_track.append([e.getEID(), len(self.__irepo.get_people_for_event(e.getEID()))])
            except EventNotFoundException:
                signup_track.append([e.getEID(), 0])
        signup_track.sort(reverse=True, key=self.__number_of_events)
        return signup_track

    def report_busy_dates(self):
        """
        Returnează un dictionar care conține datele și numărul de participanți ordonate
        descrescător în ordinea numărului de participanți.
        """
        signup_list = self.__irepo.get_all()
        # date track <- {data:nr_participanti}
        date_track = {}
        for s in signup_list:
            if s.getEvent().getDate() not in date_track:
                date_track[s.getEvent().getDate()] = 1
            else:
                date_track[s.getEvent().getDate()] += 1
        top_dates = {k: v for k, v in sorted(date_track.items(), key=lambda item: item[1], reverse=True)}
        return top_dates


def test_add_signup():
    i_repo = SignUpRepository()
    i_srv = SignUpService(i_repo)
    person = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    i_srv.add_signup(person, event)
    try:
        i_srv.add_signup(person, event)
        assert False
    except AlreadySignedUpError:
        assert True


def test_remove_by_person():
    i_repo = SignUpRepository()
    i_srv = SignUpService(i_repo)
    person = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    event2 = Event(4398, '30/11/2021', '13:00', 'Eveniment')
    i_srv.add_signup(person, event1)
    i_srv.add_signup(person, event2)
    assert(len(i_srv.get_all_signups()) == 2)
    i_srv.remove_by_person(person.getPID())
    assert(len(i_srv.get_all_signups()) == 0)


def test_remove_by_event():
    i_repo = SignUpRepository()
    i_srv = SignUpService(i_repo)
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    person2 = Person(4252324, 'Oliver', 'Twist', 'oras, strada, numar')
    event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    i_srv.add_signup(person1, event)
    i_srv.add_signup(person2, event)
    assert(len(i_srv.get_all_signups()) == 2)
    i_srv.remove_by_event(event.getEID())
    assert(len(i_srv.get_all_signups()) == 0)


def test_report_events_for_person_by_date():
    i_repo = SignUpRepository()
    i_srv = SignUpService(i_repo)
    person = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    event2 = Event(4398, '01/01/2022', '13:00', 'Eveniment 1')
    event3 = Event(6213, '15/01/2022', '13:00', 'Eveniment 2')
    event4 = Event(9324, '12/12/2021', '13:00', 'Eveniment 3')
    i_srv.add_signup(person, event1)
    i_srv.add_signup(person, event2)
    i_srv.add_signup(person, event3)
    i_srv.add_signup(person, event4)
    events_list = i_srv.report_events_for_person_by_date(1531235)
    assert (len(events_list) == 4)
    assert (events_list[0] == event1)
    assert (events_list[1] == event4)
    assert (events_list[3] == event3)
    try:
        events_list = i_srv.report_events_for_person_by_date(32452352)
        assert False
    except PersonNotFoundException:
        assert True


def test_report_busy_people():
    i_repo = SignUpRepository()
    i_srv = SignUpService(i_repo)
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    person2 = Person(9815445, 'John', 'Doe', 'oras, strada, numar')
    person3 = Person(4264817, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    event2 = Event(4398, '01/01/2022', '13:00', 'Eveniment 1')
    event3 = Event(6213, '15/01/2022', '13:00', 'Eveniment 2')
    event4 = Event(9324, '12/12/2021', '13:00', 'Eveniment 3')
    i_srv.add_signup(person1, event1)
    i_srv.add_signup(person1, event4)
    i_srv.add_signup(person2, event3)
    i_srv.add_signup(person2, event4)
    i_srv.add_signup(person2, event2)
    busy_people = i_srv.report_busy_people([person1, person2, person3])
    assert(len(busy_people) == 3)
    assert(busy_people[0][0] == 9815445)
    assert(busy_people[0][1] == 3)
    assert(busy_people[1][0] == 1531235)
    assert(busy_people[1][1] == 2)
    assert(busy_people[2][0] == 4264817)
    assert(busy_people[2][1] == 0)


def test_report_succesful_events():
    i_repo = SignUpRepository()
    i_srv = SignUpService(i_repo)
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    person2 = Person(9815445, 'John', 'Doe', 'oras, strada, numar')
    person3 = Person(4264817, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    event2 = Event(4398, '01/01/2022', '13:00', 'Eveniment 1')
    event3 = Event(6213, '15/01/2022', '13:00', 'Eveniment 2')
    event4 = Event(9324, '12/12/2021', '13:00', 'Eveniment 3')
    i_srv.add_signup(person1, event4)
    i_srv.add_signup(person3, event4)
    i_srv.add_signup(person2, event2)
    i_srv.add_signup(person3, event2)
    i_srv.add_signup(person2, event4)
    i_srv.add_signup(person2, event3)
    succesful_events = i_srv.report_succesful_events([event1, event2, event3, event4])
    assert(len(succesful_events) == 4)
    assert(succesful_events[0][0] == 9324)
    assert(succesful_events[0][1] == 3)
    assert(succesful_events[1][0] == 4398)
    assert(succesful_events[1][1] == 2)
    assert(succesful_events[2][0] == 6213)
    assert(succesful_events[2][1] == 1)
    assert (succesful_events[3][0] == 1243)
    assert (succesful_events[3][1] == 0)


test_add_signup()
test_remove_by_person()
test_remove_by_event()
test_report_events_for_person_by_date()
test_report_busy_people()
test_report_succesful_events()
