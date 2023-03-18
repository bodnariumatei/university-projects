public delegate Object FileParser(string line);
public class FileRepo<IDT, ElemType>: IRepository<IDT, ElemType> where ElemType:Entity<IDT>  {
    private string filename;
    private FileParser fileParser;
    private List<ElemType> enitities = new List<ElemType>();

    public FileRepo(string filename, FileParser fileParser){
        this.filename = filename;
        this.fileParser = fileParser;
        loadFromFile();
    }

    private void loadFromFile(){
        if(File.Exists(filename)){
            string[] lines = File.ReadAllLines(filename);  
            foreach (string line in lines){
                ElemType e = (ElemType) fileParser(line);
                enitities.Add(e);
            }
        } else {
            Console.WriteLine("Fisierul "+ filename + " nu exista");
        }
    }

    public ElemType? getOne(IDT id)
    {
        foreach(ElemType e in this.enitities){
            if(Object.Equals( e.Id, id)){
                return e;
            }
        }
        return null;
    }

    public IEnumerable<ElemType> getAll()
    {
        return this.enitities;
    }
}