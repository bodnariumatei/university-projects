from domain.entities import Person, Event
from repository.repos import PeopleRepository, EventsRepository


class FilePeopleRepo(PeopleRepository):
    """
    Stochează/scoate date despre persoane în/din fișier.
    """
    def __init__(self, file_name):
        """
        Initializează repozitorul în fișier pentru persoane.
        :param file_name: numele fisierului in care se afla info despre persoane
        :type  file_name: str
        post: persoanele sunt încărcate din fișier
        """
        # inițializăm clasa de bază
        PeopleRepository.__init__(self)
        self.__file_name = file_name
        # încărcăm din fișier persoanele
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca in program datele despre persoane din fișier.
        :raises: CorruptedFileException if there is an error
        when reading from the file
        """
        try:
            f = open(self.__file_name, "r")
        except IOError:
            # file not exist
            return
        line = f.readline().strip()
        while line != "":
            attrs = line.split(';')
            p = Person(int(attrs[0].strip()), attrs[1].strip(),
                       attrs[2].strip(), attrs[3].strip())
            PeopleRepository.store(self, p)
            line = f.readline().strip()
        f.close()

    def __store_to_file(self):
        """
         Stochează toate persoanele în fișier
        """
        # open file (rewrite file)
        f = open(self.__file_name, "w")
        ppl = PeopleRepository.get_all_people(self)
        for p in ppl:
            prf = str(p.getPID()) + '; ' + p.getFirstname() + '; ' + p.getLastname() + '; ' + p.getAdress()
            prf = prf+"\n"
            f.write(prf)
        f.close()

    def store(self, person):
        """
          Stochează persoana în fișier
          -- Overwrite store
          person - persoana
          :post: persoana e stocată în fișier
        """
        PeopleRepository.store(self, person)
        self.__store_to_file()

    def modify(self, pid, mod_person):
        """
          Modifică datele unei persoane.
          pid - int, id-ul persoanei care se modifică
          mod_person - Person, persoana modificată
          raises - PersonNotFoundException dacă nu există persoană cu id-ul furnizat
        """
        PeopleRepository.modify(self, pid, mod_person)
        self.__store_to_file()

    def delete(self, pid):
        """
          Șterge o persoană din fișier.
          pid - int, id-ul persoanei care trebuie ștearsă
          :post: fișierul nu mai conține persoana cu id-ul dat
          :raises: PersonNotFoundException dacă nu există persoană cu id-ul furnizat
        """
        PeopleRepository.delete(self, pid)
        self.__store_to_file()

    def remove_all(self):
        """
          Golește repozitorul
        """
        PeopleRepository.remove_all(self)
        self.__store_to_file()


class FileEventsRepo(EventsRepository):
    """
    Stochează/scoate date despre evenimente în/din fișier.
    """
    def __init__(self, file_name):
        """
        Initializează repozitorul în fișier pentru evenimente.
        :param file_name: numele fisierului in care se afla info despre evenimente
        :type  file_name: str
        post: evenimentele sunt încărcate din fișier
        """
        # inițializăm clasa de bază
        EventsRepository.__init__(self)
        self.__file_name = file_name
        # încărcăm din fișier persoanele
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca in program datele despre evenimente din fișier.
        :raises: CorruptedFileException if there is an error when reading from the file
        """
        try:
            f = open(self.__file_name, "r")
        except IOError:
            # file not exist
            return
        line = f.readline().strip()
        while line != "":
            attrs = line.split(';')
            event = Event(int(attrs[0].strip()), attrs[1].strip(),
                          attrs[2].strip(), attrs[3].strip())
            EventsRepository.store(self, event)
            line = f.readline().strip()
        f.close()

    def __store_to_file(self):
        """
         Stochează toate evenimentele în fișier
         :raises: CorruptedFileException dacă nu poate stoca
        """
        # open file (rewrite file)
        f = open(self.__file_name, "w")
        events = EventsRepository.get_all_events(self)
        for e in events:
            erf = str(e.getEID()) + '; ' + e.getDate() + '; ' + e.getTime() + '; ' + e.getDescription()
            erf = erf+"\n"
            f.write(erf)
        f.close()

    def store(self, event):
        """
          Stochează evenimentul în fișier
          -- Overwrite store
          event - evenimentul
          :post: evenimentul e stocată în fișier
        """
        EventsRepository.store(self, event)
        self.__store_to_file()

    def modify(self, eid, mod_event):
        """
          Modifică datele unui eveniment.
          eid - int, id-ul evenimentului care se modifică
          mod_event - Event, evenimentul modificat
          raises - EventNotFoundException dacă nu există persoană cu id-ul furnizat
        """
        EventsRepository.modify(self, eid, mod_event)
        self.__store_to_file()

    def delete(self, eid):
        """
          Șterge o persoană din fișier.
          pid - int, id-ul persoanei care trebuie ștearsă
          :post: fișierul nu mai conține persoana cu id-ul dat
          :raises: PersonNotFoundException dacă nu există persoană cu id-ul furnizat
        """
        EventsRepository.delete(self, eid)
        self.__store_to_file()

    def remove_all(self):
        """
          Golește repozitorul
        """
        EventsRepository.remove_all(self)
        self.__store_to_file()
