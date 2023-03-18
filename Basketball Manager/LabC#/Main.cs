internal partial class Program
{
    private static void Main(string[] args) {
        ServiceNBA srv = setupService();
        ConsoleUI ui = new ConsoleUI(srv);

        ui.startUi();
    }

    private static ServiceNBA setupService(){
        FileRepo<int, Jucator> pRepo = new FileRepo<int, Jucator>(
            "data\\jucatori.txt", Utils.parserJucator);
        FileRepo<int, Echipa> tRepo = new FileRepo<int, Echipa>(
            "D:\\Facultate\\Metode Avansate de Programare\\Laborator\\LabC#\\data\\echipe.txt", Utils.parserEchipa);
        FileRepo<int, Meci> mRepo = new FileRepo<int, Meci>(
            "D:\\Facultate\\Metode Avansate de Programare\\Laborator\\LabC#\\data\\meciuri.txt", Utils.parserMeci);
        FileRepo<int, JucatorActiv> apRepo = new FileRepo<int, JucatorActiv>(
            "D:\\Facultate\\Metode Avansate de Programare\\Laborator\\LabC#\\data\\jucatori_activi.txt", Utils.parserJucatorActiv);

        return new ServiceNBA(pRepo, tRepo, mRepo, apRepo);
    }
}