public class ServiceNBA{
    private FileRepo<int, Jucator> playersRepo;
    private FileRepo<int, Echipa> teamsRepo;
    private FileRepo<int, Meci> matchesRepo;
    private FileRepo<int, JucatorActiv> activePlayersRepo;

    public ServiceNBA(FileRepo<int, Jucator> pRepo, FileRepo<int, Echipa> tRepo, FileRepo<int, Meci> mRepo, FileRepo<int, JucatorActiv> apRepo){
        this.playersRepo = pRepo;
        this.teamsRepo = tRepo;
        this.matchesRepo = mRepo;
        this.activePlayersRepo = apRepo;
    }

    public IEnumerable<Jucator> getPlayerOfTeam(int idEchipa){
        IEnumerable<Jucator> playersOfTeam = from j in playersRepo.getAll() 
                                             where j.IdEchipa == idEchipa 
                                             select j;
        return playersOfTeam;
    }

    public IEnumerable<Jucator> getActivePlayersOfTeamInMatch(int idEchipa, int idMeci){
        IEnumerable<Jucator> playerz = playersRepo.getAll();
        IEnumerable<JucatorActiv> activePlayerz = activePlayersRepo.getAll();
        IEnumerable<Jucator> playersOfTeam = from j in playerz join ap in activePlayerz on j.Id equals ap.Id
                                             where j.IdEchipa==idEchipa && ap.IdMeci==idMeci
                                             select j;
        return playersOfTeam;
    }

    public IEnumerable<Meci> getMatchesInPeriod(DateTime startDate, DateTime endDate){
        IEnumerable<Meci> matchesInPeriod = from m in matchesRepo.getAll()
                                             where m.DataMeci > startDate && m.DataMeci < endDate
                                             select m;
        return matchesInPeriod;
    }

    public ((string, int), (string, int)) getScoreFromMatch(int idMeci){
        IEnumerable<Jucator> playerz = playersRepo.getAll();
        IEnumerable<JucatorActiv> activePlayerz = activePlayersRepo.getAll();
        var score = from j in playerz join ap in activePlayerz on j.Id equals ap.Id
                      where ap.IdMeci == idMeci
                      group ap by j.IdEchipa into g
                      select new {Echipa = g.Key, Total = g.Sum(x => x.NrPuncteInscrise)};
        Echipa? e1 = teamsRepo.getOne(score.First().Echipa);
        string numeEchipa1 = "";
        if(e1 != null)
            numeEchipa1 = e1.Nume;
        int scor1 = score.First().Total;
        Echipa? e2 = teamsRepo.getOne(score.Last().Echipa);
        string numeEchipa2 = "";
        if(e2 != null)
            numeEchipa2 = e2.Nume;
        int scor2 = score.Last().Total;
        return ((numeEchipa1, scor1), (numeEchipa2, scor2));
    }
}