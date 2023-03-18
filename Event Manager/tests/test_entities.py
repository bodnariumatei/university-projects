import unittest

from domain.entities import Person, Event, SignUp


class TestEntities(unittest.TestCase):
    def test_create_person(self):
        person = Person(48521, 'John', 'Doe', 'Suceava, str. Mihai Eminescu, nr.38')
        self.assertTrue(person.getPID() == 48521)
        self.assertTrue(person.getLastname() == 'Doe')
        self.assertTrue(person.getFirstname() == 'John')
        self.assertTrue(person.getAdress() == 'Suceava, str. Mihai Eminescu, nr.38')

        person.setPID(59632)
        person.setFirstname('Oliver')
        person.setLastname('Twist')
        person.setAdress('Cluj-Napoca, str. Teodor Mihaly, nr.83')
        self.assertTrue(person.getPID() == 59632)
        self.assertTrue(person.getLastname() == 'Twist')
        self.assertTrue(person.getFirstname() == 'Oliver')
        self.assertTrue(person.getAdress() == 'Cluj-Napoca, str. Teodor Mihaly, nr.83')

    def test_equal_persons(self):
        person1 = Person(48521, 'John', 'Doe', 'Suceava, str. Mihai Eminescu, nr.38')
        person2 = Person(48521, 'John', 'Doe', 'Cluj-Napoca, str. Memorandului, nr.18')
        self.assertTrue(person1 == person2)

        person3 = Person(59632, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.83')
        self.assertTrue(person1 != person3)

    def test_create_event(self):
        event = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        self.assertTrue(event.getEID() == 198347)
        self.assertTrue(event.getDate() == '15/11/2021')
        self.assertTrue(event.getTime() == '18:30')
        self.assertTrue(event.getDescription() == 'Gala oamenilor de treabă, ...')

        event.setEID(209458)
        event.setDate('17/11/2021')
        event.setTime('20:00')
        event.setDescription('Concurs de zburat cu gândul, ...')
        self.assertTrue(event.getEID() == 209458)
        self.assertTrue(event.getDate() == '17/11/2021')
        self.assertTrue(event.getTime() == '20:00')
        self.assertTrue(event.getDescription() == 'Concurs de zburat cu gândul, ...')

    def test_equal_events(self):
        event1 = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        event2 = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        self.assertTrue(event1 == event2)

        event3 = Event(209458, '17/11/2021', '20:00', 'Concurs de zburat cu gândul, ...')
        self.assertTrue(event1 != event3)

    def test_create_signup(self):
        person = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        event = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
        sign_up = SignUp(person, event)
        self.assertTrue(sign_up.getPerson() == person)
        self.assertTrue(sign_up.getEvent() == event)

    def test_equal_signups(self):
        person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
        inscriere1 = SignUp(person1, event1)
        person2 = Person(1531235, 'asfaf', 'asfas', 'oras, strada, numar')
        event2 = Event(1243, '24/12/2025', '20:00', 'Gală casfasf')
        inscriere2 = SignUp(person2, event2)
        self.assertTrue(inscriere1 == inscriere2)
        person3 = Person(5448456, 'Johhny', 'Bravo', 'oras, strada, numar')
        event3 = Event(1243, '24/12/2025', '20:00', 'Gală caritabilă')
        inscriere3 = SignUp(person3, event3)
        self.assertTrue(inscriere1 != inscriere3)
        person4 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        event4 = Event(8363, '24/12/2021', '18:00', 'Gală de Crăciun')
        inscriere4 = SignUp(person4, event4)
        self.assertTrue(inscriere4 != inscriere1)