package com.sn.socialnetwork.repository.memory;

import com.sn.socialnetwork.domain.Entity;
import com.sn.socialnetwork.repository.Repository;
import com.sn.socialnetwork.validators.Validator;
import java.util.ArrayList;


public class InMemoryRepository<ID, ElemType extends Entity<ID>> implements Repository<ID, ElemType> {
    ArrayList<ElemType> entities;
    private Validator<ElemType> validator;

    public InMemoryRepository(Validator<ElemType> validator){
        this.validator = validator;
        entities = new ArrayList<ElemType>();
    }

    @Override
    public ElemType findOne(ID id) {
        if(id == null)
            throw new IllegalArgumentException("Id-ul trebuie sa nu fie null");
        for(ElemType e :entities){
            if(e.getId().equals(id)){
                return e;
            }
        }
        return null;
    }

    @Override
    public Iterable<ElemType> getAll() {
        return entities;
    }

    @Override
    public ElemType store(ElemType entity) {
        if(entity == null){
            throw new IllegalArgumentException("Entitatea nu trebuie sa fie null.");
        }
        validator.validate(entity);
        if(findOne(entity.getId()) != null){
            return entity;
        } else {
            entities.add(entity);
            return null;
        }
    }

    @Override
    public ElemType delete(ID id) {
        if(id == null)
            throw new IllegalArgumentException("Id-ul trebuie sa nu fie null");
        ElemType e = findOne(id);
        if(e == null){
            return null;
        } else {
            entities.remove(e);
            return e;
        }
    }

    @Override
    public ElemType update(ElemType entity) {
        if(entity == null)
            throw new IllegalArgumentException("Id-ul trebuie sa nu fie null");
        validator.validate(entity);
        ElemType e = findOne(entity.getId());
        if(e == null){
            return entity;
        } else {
            int i = entities.indexOf(e);
            entities.set(i, entity);
            return null;
        }
    }
}
