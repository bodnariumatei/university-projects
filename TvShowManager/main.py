from domain.validators import ShowValidator
from repository.show_file_repo import ShowFileRepo
from service.show_service import ShowService
from ui.console_ui import ConsoleUI

show_repo = ShowFileRepo('data/shows.txt')
show_val = ShowValidator()
show_srv = ShowService(show_repo, show_val)

con_ui = ConsoleUI(show_srv)

con_ui.start_ui()
