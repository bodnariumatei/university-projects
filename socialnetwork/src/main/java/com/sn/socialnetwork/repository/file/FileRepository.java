package com.sn.socialnetwork.repository.file;

import com.sn.socialnetwork.domain.Entity;
import com.sn.socialnetwork.repository.memory.InMemoryRepository;
import com.sn.socialnetwork.validators.Validator;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public abstract class FileRepository<ID, ElemType extends Entity<ID>> extends InMemoryRepository<ID, ElemType> {
    private String filename;

    public FileRepository(Validator<ElemType> validator, String filename) {
        super(validator);
        this.filename = filename;
        load_from_file();
    }

    private void load_from_file() {
        File file = new File(filename);
        try {
            Scanner filesc = new Scanner(file);
            while(filesc.hasNextLine()){
                String line = filesc.nextLine();
                ElemType ent = string_to_entity(line);
                super.store(ent);
            }
            filesc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Eroare la citire din fisier!");
        }
    }

    private void save_to_file(){
        try {
            FileWriter fWriter = new FileWriter(filename);
            Iterable<ElemType> allEnts = super.getAll();
            for(ElemType ent:allEnts) {
                String text = entity_to_string(ent);
                fWriter.write(text);
            }
            fWriter.close();
        } catch (IOException e) {
            System.out.println("Eroare la scriere in fisier!");
        }
    }

    @Override
    public ElemType store(ElemType entity) {
        ElemType ent = super.store(entity);
        save_to_file();
        return ent;
    }

    @Override
    public ElemType delete(ID id) {
        ElemType ent = super.delete(id);
        save_to_file();
        return ent;
    }

    @Override
    public ElemType update(ElemType entity) {
        ElemType ent = super.update(entity);
        save_to_file();
        return ent;
    }

    protected abstract String entity_to_string(ElemType ent);

    protected abstract ElemType string_to_entity(String line);
}
