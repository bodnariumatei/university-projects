public class Utils{
    public static Jucator parserJucator(string line){
        string[] attr = line.Split(" - ");
        int id = Int32.Parse(attr[0]);
        string nume = attr[1];
        string scoala = attr[2];
        int idEchipa = Int32.Parse(attr[3]);
        return new Jucator(id, nume, scoala, idEchipa);
    }
    public static Echipa parserEchipa(string line){
        string[] attr = line.Split(" - ");
        int id = Int32.Parse(attr[0]);
        string nume = attr[1];
        return new Echipa(id, nume);
    }
    public static Meci parserMeci(string line){
        string[] attr = line.Split(" - ");
        int id = Int32.Parse(attr[0]);
        int idGazda = Int32.Parse(attr[1]);
        int idOaspete = Int32.Parse(attr[2]);
        DateTime data = DateTime.Parse(attr[3]);
        return new Meci(id, idGazda, idOaspete, data);
    }
    public static JucatorActiv parserJucatorActiv(string line){
        string[] attr = line.Split(" - ");
        int id = Int32.Parse(attr[0]);
        int idMeci = Int32.Parse(attr[1]);
        int nrPuncteInscrise = Int32.Parse(attr[2]);
        TipJucator tip;
        if(attr[3] == "rezerva"){
            tip = TipJucator.rezerva;
        } else {
            tip = TipJucator.participant;
        }
        return new JucatorActiv(id,idMeci, nrPuncteInscrise, tip);
    }
}