public interface IRepository<IDT, ElemType>{
    /* Cauta o entitate cu un id dat
    * returneaza:
            - null daca entitatea cu id-ul dat nu exista
            - enitatea daca a fost gasita
    */
    public ElemType? getOne(IDT id);

    // Returneaza lista cu toate elementele din repo
    public IEnumerable<ElemType>? getAll();
}