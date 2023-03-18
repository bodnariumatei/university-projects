package com.sn.socialnetwork.validators;

public interface Validator<T> {
    void validate(T entity) throws ValidationException;
    //void validate_unique(Iterable<T> entities, T newEntity) throws ValidationException;
}
