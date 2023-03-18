from domain.entities import SignUp
from repository.signupRepo import SignUpRepository


class FileSignUpRepo(SignUpRepository):
    def __init__(self, file_name, p_repo, e_repo):
        """
        Inițializează repozitorul cu fișier
        file_name - str, numele fișierului care conține date despre înscrieri
        p_repo - PeopleRepository
        e_repo - EventsRepository
        :post: datele din fișier sunt încarcate în program
        """
        SignUpRepository.__init__(self)
        self.__file_name = file_name
        self.__prepo = p_repo
        self.__erepo = e_repo
        # Încarcarea datelor din fișier în program
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca in program datele despre înscrieri din fișier.
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
            ids = line.split('-')
            person = self.__prepo.find(int(ids[0].strip()))
            event = self.__erepo.find(int(ids[1].strip()))
            sign_up = SignUp(person, event)
            SignUpRepository.store(self, sign_up)
            line = f.readline().strip()
        f.close()

    def __store_to_file(self):
        """
        Stochează toate înscrierile în fișier
        :raises: CorruptedFileException dacă nu poate stoca
        """
        # open file (rewrite file)
        f = open(self.__file_name, "w")
        sign_ups = SignUpRepository.get_all(self)
        for su in sign_ups:
            suf = str(su.getPerson().getPID()) + ' - ' + str(su.getEvent().getEID())
            suf = suf + "\n"
            f.write(suf)
        f.close()

    def store(self, sign_up):
        """
        Stochează înscrierea în fișier
        -- Overwrite store
        sign_up - înscriere
        :post: înscrierea e stocată în fișier
        """
        SignUpRepository.store(self, sign_up)
        self.__store_to_file()

    def remove_for_person(self, pid):
        """
        Șterge toate înscrierile pentru o persoană
        pid - int, id-ul persoanei pentru care se șterge
        """
        SignUpRepository.remove_for_person(self, pid)
        self.__store_to_file()

    def remove_for_event(self, eid):
        """
        Șterge toate înscrierile pentru un eveniment
        eid - int, id-ul evenimentului pentru care se șterge
        """
        SignUpRepository.remove_for_event(self, eid)
        self.__store_to_file()

    def remove_all(self):
        SignUpRepository.remove_all(self)
        self.__store_to_file()
