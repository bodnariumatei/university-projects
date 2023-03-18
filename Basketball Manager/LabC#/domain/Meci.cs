public class Meci: Entity<int>{
    private int idEchipaGazda;
    private int idEchipaOaspete;
    private DateTime dataMeci;

    public Meci(int id, int idGazda, int idOaspete, DateTime data):base(id){
        this.idEchipaGazda = idGazda;
        this.idEchipaOaspete = idOaspete;
        this.dataMeci = data;
    }

    public int IdEchipaGazda{
        get{ return this.idEchipaGazda; }
        set{ this.idEchipaGazda = value;}
    }

    public int IdEchipaOaspete{
        get{ return this.idEchipaOaspete; }
        set{ this.idEchipaOaspete = value; }
    }

    public DateTime DataMeci{
        get{ return this.dataMeci; }
        set{ this.dataMeci = value; }
    }
}