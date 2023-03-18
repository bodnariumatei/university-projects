import unittest

from domain.entities import Person, Event, SignUp
from repository.repo_errors import EventNotFoundException, PersonNotFoundException
from repository.repos import PeopleRepository, EventsRepository
from repository.signupRepo import SignUpRepository


class TestCaseMemoryPeopleRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = PeopleRepository()
        self.__add_predifined_people()

    def __add_predifined_people(self):
        p1 = Person(1234567891523, 'John', 'Doe', 'Cluj-Napoca, str. Nufarului, nr.24')
        p2 = Person(3214569743323, 'Oliver', 'Twist', 'Cluj-Napoca, str. Charles Dickiens, nr.37')
        p3 = Person(7903325923872, 'Johnny', 'Test', 'Cluj-Napoca, str. Memorandumului, nr.42')
        p4 = Person(9234263423363, 'Kvothe', 'Lockless', 'Vintas, str. Edema-Ruh, nr.45')
        p5 = Person(4293740003722, 'Mihai', 'Eminescu', 'Cluj-Napoca, str. Nufarului, nr.55')
        p6 = Person(5554232000773, 'Bruce', 'Wayne', 'Gotham, str. Liliacului, Wayne Manor')
        self.__repo.store(p1)
        self.__repo.store(p2)
        self.__repo.store(p3)
        self.__repo.store(p4)
        self.__repo.store(p5)
        self.__repo.store(p6)

    def test_get_all(self):
        plist = self.__repo.get_all_people()
        self.assertTrue(len(plist) != 0)
        self.assertEqual(len(plist), 6)
        self.assertEqual(plist[0].getPID(), 1234567891523)
        self.assertEqual(plist[5].getPID(), 5554232000773)

    def test_store(self):
        plist = self.__repo.get_all_people()
        initial_lenght = len(plist)
        p7 = Person(8885615422235, 'Maria', 'Ioana', 'Romania, str. Campionilor, nr. 1')
        self.__repo.store(p7)
        plist = self.__repo.get_all_people()
        self.assertTrue(initial_lenght != len(plist))
        self.assertEqual(len(plist), initial_lenght+1)
        self.assertTrue(plist[-1] == p7)

    def test_find(self):
        pf = self.__repo.find(3214569743323)
        self.assertTrue(pf.getPID() == 3214569743323)
        self.assertEqual(pf.getFirstname(), 'Oliver')
        self.assertRaises(ValueError, self.__repo.find, 6666666954125)

    def test_delete(self):
        plist = self.__repo.get_all_people()
        initial_lenght = len(plist)
        self.__repo.delete(4293740003722)
        plist = self.__repo.get_all_people()
        self.assertTrue(initial_lenght != len(plist))
        self.assertEqual(len(plist), initial_lenght - 1)
        self.assertRaises(ValueError, self.__repo.find, 4293740003722)
        self.assertRaises(PersonNotFoundException, self.__repo.delete, 32323232)

class TestCaseMemoryEventsRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = EventsRepository()
        self.__add_predifined_events()

    def __add_predifined_events(self):
        e1 = Event(12412, '30/11/2021', '18:30', 'Gala oamenilor de treaba, ...')
        e2 = Event(73432, '4/12/2021', '04:00', 'Normal day celebration, ...')
        e3 = Event(41245, '8/12/2021', '00:00', 'Rememberance of friendship day, ...')
        e4 = Event(90232, '24/12/2021', '16:00', 'Ajun, ...')
        e5 = Event(65480, '1/01/2022', '13:00', 'Petrecere mare cu Dan Negru, ...')
        e6 = Event(17492, '5/03/2022', '18:00', 'Gala primaverii, ...')
        self.__repo.store(e1)
        self.__repo.store(e2)
        self.__repo.store(e3)
        self.__repo.store(e4)
        self.__repo.store(e5)
        self.__repo.store(e6)

    def test_get_all(self):
        elist = self.__repo.get_all_events()
        self.assertTrue(len(elist) != 0)
        self.assertEqual(len(elist), 6)
        self.assertEqual(elist[0].getEID(), 12412)
        self.assertEqual(elist[5].getEID(), 17492)

    def test_store(self):
        elist = self.__repo.get_all_events()
        initial_lenght = len(elist)
        e7 = Event(99845, '15/02/2022', '18:30', 'Ceva eveniment nemaiauzit, ...')
        self.__repo.store(e7)
        elist = self.__repo.get_all_events()
        self.assertTrue(initial_lenght != len(elist))
        self.assertEqual(len(elist), initial_lenght+1)
        self.assertTrue(elist[-1] == e7)

    def test_find(self):
        ef = self.__repo.find(73432)
        self.assertTrue(ef.getEID() == 73432)
        self.assertEqual(ef.getDescription(), 'Normal day celebration, ...')
        self.assertRaises(ValueError, self.__repo.find, 66888)

    def test_delete(self):
        elist = self.__repo.get_all_events()
        initial_lenght = len(elist)
        self.__repo.delete(73432)
        elist = self.__repo.get_all_events()
        self.assertTrue(initial_lenght != len(elist))
        self.assertEqual(len(elist), initial_lenght - 1)
        self.assertRaises(ValueError, self.__repo.find, 73432)
        self.assertRaises(EventNotFoundException, self.__repo.delete, 32323232)


class TestCaseMemorySignupRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = SignUpRepository()
        self.__add_predifined_signups()

    def __add_predifined_signups(self):
        person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        person2 = Person(3463446, 'Oliver', 'Twist', 'oras, strada, numar')
        person3 = Person(9884515, 'Joana', 'D\'Arc', 'Franta, Orleans, str. Sfintilor')
        event1 = Event(1243, '25/12/2021', '20:00', 'Gală caritabilă')
        event2 = Event(5643, '30/12/2021', '13:00', 'Eveniment #1')
        event3 = Event(9844, '10/01/2022', '15:30', 'Eveniment #2')
        self.__repo.store(SignUp(person1, event2))
        self.__repo.store(SignUp(person1, event3))
        self.__repo.store(SignUp(person2, event1))
        self.__repo.store(SignUp(person2, event2))
        self.__repo.store(SignUp(person2, event3))
        self.__repo.store(SignUp(person3, event1))
        self.__repo.store(SignUp(person3, event3))

    def test_get_all(self):
        signup_list = self.__repo.get_all()
        self.assertTrue(len(signup_list) != 0)
        self.assertEqual(len(signup_list), 7)
        self.assertEqual(signup_list[0].getPerson().getPID(), 1531235)
        self.assertEqual(signup_list[0].getEvent().getEID(), 5643)
        self.assertEqual(signup_list[6].getPerson().getPID(), 9884515)
        self.assertEqual(signup_list[6].getEvent().getEID(), 9844)

    def test_store(self):
        person4 = Person(3463446, 'Johnny', 'Test', 'CN, str. Nostalgiei, nr. 10')
        event4 = Event(3001, '15/01/2022', '18:30', 'Eveniment #3')
        initial_lenght = len(self.__repo.get_all())
        self.__repo.store(SignUp(person4, event4))
        slist = self.__repo.get_all()
        self.assertEqual(len(slist), initial_lenght + 1)
        self.assertEqual(slist[-1].getPerson(), person4)
        self.assertEqual(slist[-1].getEvent(), event4)

    def test_remove_for_person(self):
        initial_lenght = len(self.__repo.get_all())
        self.__repo.remove_for_person(3463446)
        slist = self.__repo.get_all()
        self.assertTrue(len(slist) != initial_lenght)
        self.assertEqual(len(slist), initial_lenght - 3)

    def test_remove_for_event(self):
        initial_lenght = len(self.__repo.get_all())
        self.__repo.remove_for_event(9844)
        slist = self.__repo.get_all()
        self.assertTrue(len(slist) != initial_lenght)
        self.assertEqual(len(slist), initial_lenght - 3)

    def test_get_events_for_person(self):
        efp_list = self.__repo.get_events_for_person(3463446)
        self.assertTrue(len(efp_list) != 0)
        event1 = Event(1243, '25/12/2021', '20:00', 'Gală caritabilă')
        self.assertTrue(event1 in efp_list)
        self.assertEqual(len(efp_list), 3)
        self.assertRaises(PersonNotFoundException, self.__repo.get_events_for_person, 323232)

    def test_get_people_for_event(self):
        pfe_list = self.__repo.get_people_for_event(9844)
        self.assertTrue(len(pfe_list) != 0)
        person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        self.assertTrue(person1 in pfe_list)
        self.assertEqual(len(pfe_list), 3)
        self.assertRaises(EventNotFoundException, self.__repo.get_people_for_event, 323232)