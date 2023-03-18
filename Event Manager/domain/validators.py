from domain.entities import Person, Event


class PersonValidator:
    def validate_person(self, person):
        errors = []
        if len(person.getLastname()) < 2 or len(person.getFirstname()) < 2:
            errors.append('Numele și prenumele nu pot fi mai scurte de 2 litere.')
        adress_string = person.getAdress().split(",")
        if len(adress_string) < 3:
            errors.append('Adresa trebuie să aibă cel puțin 3 elemente: oraș, stradă, număr separate prin \',\'.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


class EventValidator:
    def validate_event(self, event):
        errors = []
        date_string = event.getDate().split("/")
        if len(date_string) != 3:
            errors.append('Data trebuie să conțină ziua, luna și anul.')
        else:
            try:
                day = int(date_string[0])
                month = int(date_string[1])
                year = int(date_string[2])
                if day < 1 or day > 31:
                    errors.append('Ziua trebuie să fie un număr cuprins între 1 și 31.')
                if month < 1 or month > 12:
                    errors.append('Luna trebuie să fie un număr cuprins între 1 și 12.')
                if year < 2021:
                    errors.append('Anul trebuie să fie mai mare sau egal cu anul curent.')
            except ValueError:
                errors.append('Ziua, luna și anul trebuie să fie numere naturale.')
        time_string = event.getTime().split(':')
        if len(time_string) != 2:
            errors.append('Ora evenimentuilui trebuie să conțină ora și minutul.')
        else:
            try:
                hour = int(time_string[0])
                minute = int(time_string[1])
                if hour < 0 or hour > 23:
                    errors.append('Ora trebuie să fie cuprinsă între 0 și 23.')
                if minute < 0 or minute > 59:
                    errors.append('Minutul trebuie să fie cuprins între 0 și 59.')
            except ValueError:
                errors.append('Ora și minutul trebuie să fie numere naturale.')
        if len(event.getDescription()) < 5:
            errors.append('Descriere invalidă.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


def test_person_validator():
    personValidator = PersonValidator()
    person1 = Person(48521, 'John', 'Doe', 'Suceava, str. Mihai Eminescu, nr.38')
    personValidator.validate_person(person1)
    person2 = Person(59632, 'O', '', 'Cluj-Napoca, str. Teodor Mihaly, nr.83')
    try:
        personValidator.validate_person(person2)
        assert False
    except ValueError:
        assert True
    person3 = Person(59632, 'Oliver', 'Twist', 'Cluj-Napoca, str. Teodor Mihaly')
    try:
        personValidator.validate_person(person3)
        assert False
    except ValueError:
        assert True


def test_event_validator():
    eventValidator = EventValidator()
    event1 = Event(198347, '15/11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    eventValidator.validate_event(event1)
    event2 = Event(198347, '11/2021', '18:30', 'Gala oamenilor de treabă, ...')
    try:
        eventValidator.validate_event(event2)
        assert False
    except ValueError:
        assert True

    event3 = Event(198347, '15/11/2021', '18', 'Gala oamenilor de treabă, ...')
    try:
        eventValidator.validate_event(event3)
        assert False
    except ValueError:
        assert True

    event4 = Event(198347, '40/13/2021', '25:78', 'Gala oamenilor de treabă, ...')
    try:
        eventValidator.validate_event(event4)
        assert False
    except ValueError:
        assert True


test_person_validator()
test_event_validator()
