import unittest

from domain.entities import Person, Event
from repository.fileRepos import FilePeopleRepo, FileEventsRepo
from repository.repo_errors import DuplicatePersonError, PersonNotFoundException, DuplicateEventError, \
    EventNotFoundException


class TestCaseFilePeopleRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = FilePeopleRepo('tests.txt')
        self.__add_predefined_people()

    def __add_predefined_people(self):
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

    def test_find(self):
        p = self.__repo.find(9234263423363)
        self.assertEqual(p.getFirstname(), 'Kvothe')
        self.assertEqual(p.getLastname(), 'Lockless')
        self.assertTrue(p.getPID() == 9234263423363)
        self.assertFalse(p.getAdress() == 'Cluj-Napoca, str. Charles Dickiens, nr.37')
        self.assertRaises(ValueError, self.__repo.find, 3232)

    def test_get_all(self):
        plist = self.__repo.get_all_people()
        self.assertEqual(len(plist), 6)
        self.assertTrue(plist[0].getFirstname() == 'John')
        self.assertTrue(plist[0].getLastname() == 'Doe')
        self.assertTrue(plist[5].getFirstname() == 'Bruce')
        self.assertTrue(plist[5].getLastname() == 'Wayne')

    def test_store_person(self):
        initial_lenght = len(self.__repo.get_all_people())
        p1 = Person(8437200002123, 'Natasha', 'Romanoff', 'Cluj-Napoca, str. Lunga, nr.24')
        p2 = Person(1068729994431, 'Hermione', 'Granger', 'Hogwarts, Girl\'s quarters , nr.5')
        self.__repo.store(p1)
        plist = self.__repo.get_all_people()
        self.assertTrue(len(plist) == initial_lenght+1)
        self.assertEqual(plist[-1], p1)
        self.__repo.store(p2)
        plist = self.__repo.get_all_people()
        self.assertTrue(len(plist) == initial_lenght + 2)
        self.assertEqual(plist[-1], p2)
        self.assertRaises(DuplicatePersonError, self.__repo.store, p1)

    def test_delete(self):
        initial_lenght = len(self.__repo.get_all_people())
        self.__repo.delete(1234567891523)
        plist = self.__repo.get_all_people()
        self.assertEqual(len(plist), initial_lenght-1)
        self.assertRaises(PersonNotFoundException, self.__repo.delete, 3232)

    def tearDown(self):
        self.__repo.remove_all()


class TestCaseFileEventsRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = FileEventsRepo('tests.txt')
        self.__add_predefined_events()

    def __add_predefined_events(self):
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

    def test_find(self):
        e = self.__repo.find(73432)
        self.assertEqual(e.getDate(), '4/12/2021')
        self.assertEqual(e.getTime(), '04:00')
        self.assertTrue(e.getEID() == 73432)
        self.assertFalse(e.getDescription() == 'Petrecere mare cu Dan Negru, ...')

        self.assertRaises(ValueError, self.__repo.find, 3232)

    def test_get_all(self):
        elist = self.__repo.get_all_events()
        self.assertEqual(len(elist), 6)
        self.assertTrue(elist[0].getDescription() == 'Gala oamenilor de treaba, ...')
        self.assertTrue(elist[0].getEID() == 12412)
        self.assertTrue(elist[5].getDescription() == 'Gala primaverii, ...')
        self.assertTrue(elist[5].getEID() == 17492)

    def test_store_event(self):
        initial_lenght = len(self.__repo.get_all_events())
        e1 = Event(99984, '10/01/2022', '13:30', 'Descriere Eveniment, ...')
        e2 = Event(10054, '20/01/2022', '15:30', 'Descriere Eveniment #2, ...')
        self.__repo.store(e1)
        elist = self.__repo.get_all_events()
        self.assertTrue(len(elist) == initial_lenght+1)
        self.assertEqual(elist[-1], e1)
        self.__repo.store(e2)
        elist = self.__repo.get_all_events()
        self.assertTrue(len(elist) == initial_lenght + 2)
        self.assertEqual(elist[-1], e2)
        self.assertRaises(DuplicateEventError, self.__repo.store, e1)

    def test_delete(self):
        initial_lenght = len(self.__repo.get_all_events())
        self.__repo.delete(90232)
        elist = self.__repo.get_all_events()
        self.assertEqual(len(elist), initial_lenght-1)
        self.assertRaises(EventNotFoundException, self.__repo.delete, 3232)

    def tearDown(self):
        self.__repo.remove_all()


class TestCaseFileSignUpRepo(unittest.TestCase):
    pass
