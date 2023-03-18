public class Entity<IDT>{
    private IDT id;

    public Entity(IDT id){
        this.id = id;
    }
    public IDT Id{
        get{return this.id;}
    }
}