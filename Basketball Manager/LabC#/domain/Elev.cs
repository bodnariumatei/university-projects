public class Elev: Entity<int>{
    private string nume;
    private string scoala;
    public Elev(int id, string nume, string scoala): base(id){
        this.nume = nume;
        this.scoala = scoala;
    }

    public string Nume{
        get{return this.nume;}
        set{this.nume = value;}
    }
    public string Scoala{
        get{return this.scoala;}
        set{this.scoala=value;}
    }

    public override bool Equals(object? obj)
    {
        if(obj == null)
            return false;
        Elev e = (Elev) obj;
        return this.Id == e.Id;
    }

    public override int GetHashCode()
    {
        throw new NotImplementedException();
    }
}