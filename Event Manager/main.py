from domain.validators import PersonValidator, EventValidator
from repository.fileRepos import FilePeopleRepo, FileEventsRepo
# from repository.repos import PeopleRepository, EventsRepository
from repository.fileSignupRepo import FileSignUpRepo
# from repository.signupRepo import SignUpRepository
from service.services import PeopleService, EventService
from service.signupService import SignUpService
from ui.console import Console

# prepo = PeopleRepository()
prepo = FilePeopleRepo('data/people.txt')
pvali = PersonValidator()
psrv = PeopleService(prepo, pvali)

# erepo = EventsRepository()
erepo = FileEventsRepo('data/events.txt')
evali = EventValidator()
esrv = EventService(erepo, evali)

# irepo = SignUpRepository()
irepo = FileSignUpRepo('data/signups.txt', prepo, erepo)
isrv = SignUpService(irepo)

ui = Console(psrv, esrv, isrv)

ui.startui()
