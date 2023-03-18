public class Echipa:Entity<int>{
    private string nume;

    public Echipa(int id, string nume): base(id){
        this.nume = nume;
    }
    
    public string Nume{
        get{
            return this.nume;
        }
        set{
            this.nume = value;
        }
    }
}