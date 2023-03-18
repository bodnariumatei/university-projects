public enum TipJucator { rezerva, participant }

public class JucatorActiv:Entity<int>{
    private int idMeci;
    private int nrPuncteInscrise;
    private TipJucator tip;

    public JucatorActiv(int idJucator, int idMeci, int nrPuncteInscrise, TipJucator tip): base(idJucator){
        this.idMeci = idMeci;
        this.nrPuncteInscrise = nrPuncteInscrise;
        this.tip = tip;
    }

    public int IdMeci{
        get{ return this.idMeci; }
        set{ this.idMeci = value; }
    }

    public int NrPuncteInscrise{
        get{ return this.nrPuncteInscrise; }
        set{ this.nrPuncteInscrise = value; }
    }

    public TipJucator Tip{
        get {return this.tip; }
        set {this.tip = value; }
    }

}