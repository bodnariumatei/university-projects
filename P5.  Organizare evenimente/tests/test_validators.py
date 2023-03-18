import unittest

from domain.entities import Person, Event
from domain.validators import PersonValidator, EventValidator


class TestCasePersonValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.__person_validator = PersonValidator()

    def test_person_validator(self):
        person1 = Person(48521, 'John', 'Doe', 'Suceava, str. Mihai Eminescu, nr.38')
        person2 = Person(59632, 'O', '', 'Cluj-Napoca, str. Teodor Mihaly, nr.83')
        person3 = Person(99541, 'Oli', 'Garey', 'Cluj-Napoca, str. Teodor Mihaly')
        person4 = Person(99541, 'J', 'H', 'Cluj-Napoca')
        self.__person_validator.validate_person(person1)
        self.assertRaises(ValueError, self.__person_validator.validate_person, person2)
        self.assertRaises(ValueError, self.__person_validator.validate_person, person3)
        self.assertRaises(ValueError, self.__person_validator.validate_person, person4)


class TestCaseEventValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.__event_validator = EventValidator()

    def test_event_validator(self):
        event1 = Event(885440, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        event2 = Event(198347, '11/2021', '18:30', 'Gala oamenilor de treabă, ...')
        event3 = Event(996258, '15/11/2021', '18', 'Gala oamenilor de treabă, ...')
        event4 = Event(22247, '40/13/2021', '25:78', 'Gala oamenilor de treabă, ...')
        event5 = Event(885412, '34/10/2021', '25:78', '.')
        event6 = Event(190007, '12/12/2021', '21:78', 'Gală, ...')
        self.__event_validator.validate_event(event1)
        self.assertRaises(ValueError, self.__event_validator.validate_event, event2)
        self.assertRaises(ValueError, self.__event_validator.validate_event, event3)
        self.assertRaises(ValueError, self.__event_validator.validate_event, event4)
        self.assertRaises(ValueError, self.__event_validator.validate_event, event5)
        self.assertRaises(ValueError, self.__event_validator.validate_event, event6)