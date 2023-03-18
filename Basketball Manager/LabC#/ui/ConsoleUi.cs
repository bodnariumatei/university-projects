public class ConsoleUI{
    private ServiceNBA srv;
    public ConsoleUI(ServiceNBA srv){
        this.srv = srv;
    }

    private void printMenu(){
        System.Console.WriteLine("Meniu:");
        System.Console.WriteLine("\t1. toti jucatorii unei echipe data");
        System.Console.WriteLine("\t2. toti jucatorii activi ai unei echipe de la un anumit meci");
        System.Console.WriteLine("\t3. toate meciurile dintr-o anumita perioada calendaristica");
        System.Console.WriteLine("\t4. scorul de la un anumit meci");
        System.Console.WriteLine("\t5. opriti aplicatia");
        System.Console.Write("Introduceti optiunea dorita: ");
    }

    public void startUi(){
        int cmd;
        while(true){
            printMenu();
            string? strcmd = System.Console.ReadLine();
            if(strcmd != null) {
                cmd = Int32.Parse(strcmd);
                if(cmd == 1){
                    System.Console.Write("Introduceti id-ul echipei: ");
                    string? strIdEchipa = System.Console.ReadLine();
                    if(strIdEchipa != null){
                        int idEchipa = Int32.Parse(strIdEchipa);
                            foreach(Jucator j in srv.getPlayerOfTeam(idEchipa)){
                            System.Console.WriteLine(j.Nume);
                        }
                    }
                } else if(cmd == 2){
                    System.Console.Write("Introduceti id-ul echipei: ");
                    string? strIdEchipa = System.Console.ReadLine();
                    System.Console.Write("Introduceti id-ul meciului: ");
                    string? strIdMeci = System.Console.ReadLine();
                    if(strIdEchipa != null && strIdMeci != null){
                        int idEchipa = Int32.Parse(strIdEchipa);
                        int idMeci = Int32.Parse(strIdMeci);
                        foreach(Jucator j in srv.getActivePlayersOfTeamInMatch(idEchipa, idMeci)){
                            System.Console.WriteLine(j.Nume);
                        }
                    }
                } else if(cmd == 3){
                    System.Console.WriteLine("Introduceti datele in formatul zz.ll.aaaa");
                    System.Console.Write("Data de inceput: ");
                    string? strDataStart = System.Console.ReadLine();
                    System.Console.Write("Data de final: ");
                    string? strDataFinal = System.Console.ReadLine();
                    if(strDataStart != null && strDataFinal != null){
                        DateTime dataStart = DateTime.Parse(strDataStart + " 00:00:00");
                        DateTime dataFinal = DateTime.Parse(strDataFinal + " 00:00:00");
                        foreach(Meci m in srv.getMatchesInPeriod(dataStart, dataFinal)){
                            System.Console.WriteLine("Meciul: " + m.Id + " - Echipele: " + m.IdEchipaGazda + ", " + m.IdEchipaOaspete);
                        }
                    }
                } else if(cmd == 4){
                    System.Console.Write("Introduceti id-ul meciului: ");
                    string? strIdMeci = System.Console.ReadLine();
                    if(strIdMeci != null){
                        int idMeci = Int32.Parse(strIdMeci);
                        var score =  srv.getScoreFromMatch(idMeci);
                        System.Console.WriteLine(score.Item1.Item1 + ": " + score.Item1.Item2 + " - " + score.Item2.Item1 + ": " + score.Item2.Item2);
                    }
                } else if( cmd == 5){
                    break;
                }
            }
        }
    }
}