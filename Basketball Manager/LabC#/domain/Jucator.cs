public class Jucator:Elev{
    private int idEchipa;
    public Jucator(int id, string nume, string scoala, int idEchipa):base(id, nume, scoala){
        this.idEchipa = idEchipa;
    }

    public int IdEchipa{
        get{ return this.idEchipa; }
        set{ this.idEchipa = value; }
    }
}