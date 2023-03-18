import unittest

from domain.entities import Person, Event
from domain.validators import PersonValidator, EventValidator
from repository.repo_errors import AlreadySignedUpError, PersonNotFoundException
from repository.repos import PeopleRepository, EventsRepository
from repository.signupRepo import SignUpRepository
from service.services import PeopleService, EventService
from service.signupService import SignUpService


class TestCasePeopleService(unittest.TestCase):
    def setUp(self) -> None:
        self.__prepo = PeopleRepository()
        self.__pval = PersonValidator()
        self.__psrv = PeopleService(self.__prepo, self.__pval)

    def test_add_person(self):
        self.__psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        self.assertTrue(len(self.__psrv.get_all_people()) == 1)
        self.assertRaises(ValueError, self.__psrv.add_person, 154215, '', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        self.assertRaises(ValueError, self.__psrv.add_person, 516555, 'John', 'Doe', 'Suceava')

    def test_get_all_people(self):
        p_list = self.__psrv.get_all_people()
        self.assertTrue(p_list == [])
        self.assertTrue(len(p_list) == 0)
        self.__psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        p_list = self.__psrv.get_all_people()
        self.assertTrue(len(p_list) == 1)
        self.__psrv.add_person(615649, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
        self.__psrv.add_person(567415, 'David', 'Copperfield', 'Suceava, str. Mihai Eminescu, nr.24')
        self.__psrv.add_person(125615, 'Bernard', 'Rieux', 'București, str. Dorobanților, nr.16')
        p_list = self.__psrv.get_all_people()
        self.assertTrue(len(p_list) == 4)

    def test_delete_person(self):
        self.__psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        self.__psrv.add_person(615649, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
        self.__psrv.add_person(924715, 'David', 'Copperfield', 'Suceava, str. Mihai Eminescu, nr.24')
        self.__psrv.add_person(187415, 'Bernard', 'Rieux', 'București, str. Dorobanților, nr.16')
        p_list = self.__psrv.get_all_people()
        self.assertTrue (len(p_list) == 4)
        self.__psrv.delete_person(924715)
        p_list = self.__psrv.get_all_people()
        self.assertTrue (len(p_list) == 3)
        self.__psrv.delete_person(615649)
        self.__psrv.delete_person(465415)
        self.__psrv.delete_person(187415)
        p_list = self.__psrv.get_all_people()
        self.assertTrue (len(p_list) == 0)

    def test_modify_person(self):
        self.__psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        p_list = self.__psrv.get_all_people()
        self.assertTrue (p_list[0].getPID() == 465415)
        self.assertTrue (p_list[0].getFirstname() == 'John')
        self.assertTrue (p_list[0].getLastname() == 'Doe')
        self.assertTrue (p_list[0].getAdress() == 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        self.__psrv.modify_person(465415, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
        p_list = self.__psrv.get_all_people()
        self.assertTrue (p_list[0].getPID() == 465415)
        self.assertTrue (p_list[0].getFirstname() == 'Oliver')
        self.assertTrue (p_list[0].getLastname() == 'Twist')
        self.assertTrue (p_list[0].getAdress() == 'Cluj-Napoca, str. Teodor Mihaly, nr.65')

    def test_find_person(self):
        self.__psrv.add_person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86')
        self.__psrv.add_person(615649, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly, nr.65')
        p1 = self.__psrv.find_person(465415)
        self.assertTrue(p1 == Person(465415, 'John', 'Doe', 'Cluj-Napoca, str. Teodor Mihaly, nr.86'))
        self.assertRaises(ValueError, self.__psrv.find_person, 323232)


class TestCaseEventsService(unittest.TestCase):
    def setUp(self) -> None:
        self.__erepo = EventsRepository()
        self.__evali = EventValidator()
        self.__esrv = EventService(self.__erepo, self.__evali)

    def test_add_event(self):
        self.__esrv.add_event(2548, '9/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        self.assertTrue(len(self.__esrv.get_all_events()) == 1)
        self.assertRaises(ValueError, self.__esrv.add_event, 5515, '9.11.2021', '18:30', 'Gala oamenilor de treabă, ...')
        self.assertRaises(ValueError, self.__esrv.add_event, 5648, '9/11/2021', '18', 'Gala oamenilor de treabă, ...')

    def test_get_all_events(self):
        e_list = self.__esrv.get_all_events()
        self.assertTrue(e_list == [])
        self.assertTrue(len(e_list) == 0)
        self.__esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        e_list = self.__esrv.get_all_events()
        self.assertTrue(len(e_list) == 1)
        self.__esrv.add_event(5654, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
        self.__esrv.add_event(2176, '14/11/2021', '14:30', 'Sesiune de relaxare cu soare, ...')
        e_list = self.__esrv.get_all_events()
        self.assertTrue(len(e_list) == 3)

    def test_delete_event(self):
        self.__esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        self.__esrv.add_event(5654, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
        self.__esrv.add_event(2176, '14/11/2021', '14:30', 'Sesiune de relaxare cu soare, ...')
        e_list = self.__esrv.get_all_events()
        self.assertTrue(len(e_list) == 3)
        self.__esrv.delete_event(2176)
        e_list = self.__esrv.get_all_events()
        self.assertTrue(len(e_list) == 2)
        self.__esrv.delete_event(5654)
        self.__esrv.delete_event(2548)
        e_list = self.__esrv.get_all_events()
        self.assertTrue(len(e_list) == 0)

    def test_modify_event(self):
        self.__esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        e_list = self.__esrv.get_all_events()
        self.assertTrue(e_list[0].getEID() == 2548)
        self.assertTrue(e_list[0].getDate() == '12/11/2021')
        self.assertTrue(e_list[0].getTime() == '18:30')
        self.assertTrue(e_list[0].getDescription() == 'Gala oamenilor de treabă, ...')
        self.__esrv.modify_event(2548, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
        e_list = self.__esrv.get_all_events()
        self.assertTrue(e_list[0].getEID() == 2548)
        self.assertTrue(e_list[0].getDate() == '18/11/2021')
        self.assertTrue(e_list[0].getTime() == '12:00')
        self.assertTrue(e_list[0].getDescription() == 'Prânz și muzică bună, ...')

    def test_find_event(self):
        self.__esrv.add_event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        self.__esrv.add_event(5654, '18/11/2021', '12:00', 'Prânz și muzică bună, ...')
        e1 = self.__esrv.find_event(2548)
        self.assertTrue(e1 == Event(2548, '12/11/2021', '18:30', 'Gala oamenilor de treabă, ...'))
        self.assertRaises(ValueError, self.__esrv.find_event, 323232)


class TestCaseSignUpService(unittest.TestCase):
    def setUp(self) -> None:
        self.__i_repo = SignUpRepository()
        self.__i_srv = SignUpService(self.__i_repo)
        person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        person2 = Person(9815445, 'John', 'Doe', 'oras, strada, numar')
        person3 = Person(4264817, 'John', 'Doe', 'oras, strada, numar')
        event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
        event2 = Event(4398, '01/01/2022', '13:00', 'Eveniment 1')
        event3 = Event(6213, '15/01/2022', '13:00', 'Eveniment 2')
        event4 = Event(9324, '12/12/2021', '13:00', 'Eveniment 3')
        self.__i_srv.add_signup(person1, event4)
        self.__i_srv.add_signup(person3, event4)
        self.__i_srv.add_signup(person2, event2)
        self.__i_srv.add_signup(person3, event2)
        self.__i_srv.add_signup(person2, event4)
        self.__i_srv.add_signup(person2, event3)
        self.__i_srv.add_signup(person2, event1)

    def test_get_all(self):
        su_list = self.__i_srv.get_all_signups()
        self.assertTrue(len(su_list) != 0)
        self.assertEqual(len(su_list), 7)
        self.assertTrue(su_list[0].getPerson().getPID() == 1531235)
        self.assertTrue(su_list[0].getEvent().getEID() == 9324)
        self.assertTrue(su_list[6].getPerson().getPID() == 9815445)
        self.assertTrue(su_list[6].getEvent().getEID() == 1243)

    def test_add_sign_up(self):
        initial_lenght = len(self.__i_srv.get_all_signups())
        self.assertTrue(initial_lenght == 7)
        person = Person(9995412, 'Ion', 'Pop', 'Pripas, str. Principala, nr. 13')
        event = Event(1920, '14/06/2022', '17:00', 'Hora în sat, ...')
        self.__i_srv.add_signup(person, event)
        su_list = self.__i_srv.get_all_signups()
        self.assertTrue(len(su_list) != initial_lenght)
        self.assertEqual(len(su_list), initial_lenght + 1)
        self.assertEqual(su_list[-1].getPerson(), person)
        self.assertEqual(su_list[-1].getEvent(), event)
        self.assertRaises(AlreadySignedUpError, self.__i_srv.add_signup, person, event)

    def test_remove_by_person(self):
        initial_lenght = len(self.__i_srv.get_all_signups())
        self.assertTrue(initial_lenght == 7)
        self.__i_srv.remove_by_person(9815445)
        su_list = self.__i_srv.get_all_signups()
        self.assertTrue(len(su_list) != initial_lenght)
        self.assertEqual(len(su_list), initial_lenght - 4)

    def test_remove_by_event(self):
        initial_lenght = len(self.__i_srv.get_all_signups())
        self.assertTrue(initial_lenght == 7)
        self.__i_srv.remove_by_event(9324)
        su_list = self.__i_srv.get_all_signups()
        self.assertTrue(len(su_list) != initial_lenght)
        self.assertEqual(len(su_list), initial_lenght - 3)

    def test_report_events_for_person_by_date(self):
        events_list = self.__i_srv.report_events_for_person_by_date(9815445)
        self.assertEqual(len(events_list), 4)
        self.assertTrue(events_list[0].getEID() == 1243)
        self.assertTrue(events_list[1].getEID() == 9324)
        self.assertTrue(events_list[2].getEID() == 4398)
        self.assertTrue(events_list[3].getEID() == 6213)
        self.assertRaises(PersonNotFoundException, self.__i_srv.report_events_for_person_by_date, 32323232)

    def test_report_events_for_person_by_desc(self):
        events_list = self.__i_srv.report_events_for_person_by_desc(9815445)
        self.assertEqual(len(events_list), 4)
        self.assertTrue(events_list[0].getEID() == 4398)
        self.assertTrue(events_list[1].getEID() == 6213)
        self.assertTrue(events_list[2].getEID() == 9324)
        self.assertTrue(events_list[3].getEID() == 1243)
        self.assertRaises(PersonNotFoundException, self.__i_srv.report_events_for_person_by_desc, 32323232)

    def test_report_busy_people(self):
        person1 = Person(1531235, 'John', 'Doe', 'oras, strada, numar')
        person2 = Person(9815445, 'Oli', 'Vendunk', 'oras, strada, numar')
        person3 = Person(4264817, 'Angelo', 'Rules', 'oras, strada, numar')
        busy_people = self.__i_srv.report_busy_people([person1, person2, person3])
        self.assertTrue(len(busy_people) == 3)
        self.assertTrue(busy_people[0][0] == 9815445)
        self.assertTrue(busy_people[0][1] == 4)
        self.assertTrue(busy_people[1][0] == 4264817)
        self.assertTrue(busy_people[1][1] == 2)
        self.assertTrue(busy_people[2][0] == 1531235)
        self.assertTrue(busy_people[2][1] == 1)

    def test_report_succesful_events(self):
        event1 = Event(1243, '25/11/2021', '20:00', 'Gală caritabilă')
        event2 = Event(4398, '01/01/2022', '13:00', 'Eveniment 1')
        event3 = Event(6213, '15/01/2022', '13:00', 'Eveniment 2')
        event4 = Event(9324, '12/12/2021', '13:00', 'Eveniment 3')
        succesful_events = self.__i_srv.report_succesful_events([event1, event2, event3, event4])
        self.assertEqual(len(succesful_events), 4)
        self.assertTrue(succesful_events[0][0] == 9324)
        self.assertTrue(succesful_events[0][1] == 3)
        self.assertTrue(succesful_events[1][0] == 4398)
        self.assertTrue(succesful_events[1][1] == 2)
        self.assertTrue(succesful_events[2][0] == 6213 or succesful_events[2][0] == 1243)
        self.assertTrue(succesful_events[2][1] == 1)
        self.assertTrue(succesful_events[3][0] == 1243 or succesful_events[3][0] == 6213)
        self.assertTrue(succesful_events[3][1] == 1)
