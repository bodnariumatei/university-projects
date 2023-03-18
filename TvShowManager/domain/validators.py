from exceptions.exceptions import ShowValidationException


class ShowValidator:
    def validate_show(self, show):
        """
        Verifică dacă datele transmise pentru atributele unui show sunt corespunzătoare
        :param show: type TvShow, show-ul pentru care se validează datele
        :return: -
        :raise: ShowValidationException(err_str) dacă există date invalide
                err_str - lista de erori apărute
        """
        err_list = []
        if len(show.get_title()) < 2:
            err_list.append('Titlul este prea scurt.')
        if len(show.get_genre()) < 2:
            err_list.append('Genul este invalid.')
        if show.get_no_eps() < 2:
            err_list.append('Număr de episoade prea mic.')

        if err_list != []:
            err_str = '\n'.join(err_list)
            raise ShowValidationException(err_str)