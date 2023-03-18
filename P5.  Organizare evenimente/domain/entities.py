class Person:
    """
    Clasă cu rolul de a gestiona atributele unei persoane și metodele care se pot aplica asupra acesteia.
    """
    def __init__(self, personID, firstname, lastname, adress):
        """
        Creează o entitate de tipul persoană cu atributele personID, prenume, nume și adresă.
        :param personID: id-ul persoanei
        :type personID: int
        :param firstname: prenumele persoanei
        :type firstname: str
        :param lastname: numele persoanei
        :type lastname: str
        :param adress: adresa persoanei
        :type adress: str
        """
        self.__pid = personID
        self.__firstname = firstname
        self.__lastname = lastname
        self.__adress = adress
        self.events_list = []
    
    def getPID(self):
        return self.__pid
    
    def getFirstname(self):
        return self.__firstname

    def getLastname(self):
        return self.__lastname

    def getAdress(self):
        return self.__adress

    def setPID(self, pid):
        self.__pid = pid
    
    def setFirstname(self, firstname):
        self.__firstname = firstname

    def setLastname(self, lastname):
        self.__lastname = lastname

    def setAdress(self, adress):
        self.__adress = adress

    def __eq__(self, other):
        """
        Determină egalitatea dintre persoana curentă și persoana other.
        :param other: obiect din clasa Person
        :type other: Person
        :return: True dacă există egalitate(dacă au același pid (și același nume)S)
                False altfel
        """
        if self.__pid == other.getPID():  # and self.__lastname == other.getLastname():
            return True
        return False


###################################################################################################################


class Event:
    """
    Clasă cu rolul de a gestiona atributele unui eveniment și metodele care se pot aplica asupra acestuia.
    """
    def __init__(self, eventID, date, time, description):
        """
        Crează o entitate de tip eveniment cu atributele eventID, date, time, description.
        :param eventID: id-ul evenimentului
        :type eventID: int
        :param date: data de desfășurare a evenimentului
        :type date: str
        :param time: ora și minutul la care începe evenimentul
        :type time: str
        :param description: descrierea evenimentului
        :type description: str
        """
        self.__eventID = eventID
        self.__date = date
        self.__time = time
        self.__description = description

    def getEID(self):
        return self.__eventID

    def getDate(self):
        return self.__date
    
    def getTime(self):
        return self.__time
    
    def getDescription(self):
        return self.__description

    def setEID(self, eid):
        self.__eventID = eid

    def setDate(self, date):
        self.__date = date

    def setTime(self, time):
        self.__time = time

    def setDescription(self, description):
        self.__description = description
    
    def __eq__(self, other):
        """
        Verifică egalitatea între evenimentul curent și evenimentul other.
        :param other: obiect din clasa Event
        :type other: Event
        :return: True dacă evenimentele sunt egale(au EID-ul egal)
                False altfel
        :rtype: bool
        """
        if self.__eventID == other.getEID():
            return True
        return False


#################################################################################################################

class SignUp:
    """
    Clasă care gestionează înscrierile/participările persoanelor la evenimente.
    """
    def __init__(self, person, event):
        """
        Creează un obiect care retine o persoana si evenimentul la care participa
        :param person: persoana care se înscrie la eveniment
        :type person: Person
        :param event: evenimentul la care se înscrie persoana
        :type event: Event
        """
        self.__person = person
        self.__event = event

    def getPerson(self):
        return self.__person

    def getEvent(self):
        return self.__event

    def setPerson(self, person):
        self.__person = person

    def setEvent(self, event):
        self.__event = event

    def __eq__(self, other):
        """
        Verifică egalitatea între două inscrieri.
        :param other: obiect din clasa SignUp
        :type other: SignUp
        :return: True dacă SignUpa curentă este efectuată între aceeași persoană și eveniment ca
                        înscrierea din 'other'
            False altfel
        :rtype: bool
        """
        if self.__event.getEID() == other.getEvent().getEID() and self.__person.getPID() == other.getPerson().getPID():
            return True
        return False

###################################################################################################################


def test_create_person():
    person = Person(48521, 'John', 'Doe', 'Suceava, str. Mihai Eminescu, nr.38')
    assert (person.getPID() == 48521)
    assert (person.getLastname() == 'Doe')
    assert (person.getFirstname() == 'John')
    assert (person.getAdress() == 'Suceava, str. Mihai Eminescu, nr.38')

    person.setPID(59632)
    person.setFirstname('Oliver')
    person.setLastname('Twist')
    person.setAdress('Cluj-Napoca, str. Teodor Mihaly, nr.83')
    assert (person.getPID() == 59632)
    assert (person.getLastname() == 'Twist')
    assert (person.getFirstname() == 'Oliver')
    assert (person.getAdress() == 'Cluj-Napoca, str. Teodor Mihaly, nr.83')


def test_equal_persons():
    person1 = Person(48521, 'John', 'Doe', 'Suceava, str. Mihai Eminescu, nr.38')
    person2 = Person(48521, 'John', 'Doe', 'Cluj-Napoca, str. Memorandului, nr.18')
    assert (person1 == person2)

    person3 = Person(59632, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.83')
    assert (person1 != person3)


def test_create_event():
    event = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    assert(event.getEID() == 198347)
    assert(event.getDate() == '15/11/2021')
    assert(event.getTime() == '18:30')
    assert(event.getDescription() == 'Gala oamenilor de treabă, ...')

    event.setEID(209458)
    event.setDate('17/11/2021')
    event.setTime('20:00')
    event.setDescription('Concurs de zburat cu gândul, ...')
    assert(event.getEID() == 209458)
    assert(event.getDate() == '17/11/2021')
    assert(event.getTime() == '20:00')
    assert(event.getDescription() == 'Concurs de zburat cu gândul, ...')


def test_equal_events():
    event1 = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    event2 = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    assert(event1 == event2)

    event3 = Event(209458, '17/11/2021', '20:00', 'Concurs de zburat cu gândul, ...')
    assert(event1 != event3)


def test_create_signup():
    person = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    sign_up = SignUp(person, event)
    assert (sign_up.getPerson() == person)
    assert (sign_up.getEvent() == event)


def test_equal_signups():
    person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
    inscriere1 = SignUp(person1, event1)
    person2 = Person(1531235, 'asfaf', 'asfas', 'oras, strada, numar')
    event2 = Event(1243, '24/12/2025', '20:00', 'Gală casfasf')
    inscriere2 = SignUp(person2, event2)
    assert (inscriere1 == inscriere2)
    person3 = Person(5448456, 'Johhny', 'Bravo', 'oras, strada, numar')
    event3 = Event(1243, '24/12/2025', '20:00', 'Gală caritabilă')
    inscriere3 = SignUp(person3, event3)
    assert (inscriere1 != inscriere3)
    person4 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
    event4 = Event(8363, '24/12/2021', '18:00', 'Gală de Crăciun')
    inscriere4 = SignUp(person4, event4)
    assert (inscriere4 != inscriere1)


test_create_person()
test_equal_persons()

test_create_event()
test_equal_events()

test_create_signup()
test_equal_signups()
