package com.sn.socialnetwork.repository;

import com.sn.socialnetwork.validators.ValidationException;

public interface Repository<ID, ElemType> {
    /**
     * Finds an entity with given ID
     * @param id - the id of the element to be found
     *           - must not be null
     * @return  - the entity with the given id if it exists
     *          - null if the entity does not exist
     * @throws IllegalArgumentException if id is null
     */
    ElemType findOne(ID id);

    /**
     * @return the list with all the entries
     */
    Iterable<ElemType> getAll();

    /**
     * Adds an entity to the entries
     * @param entity: - the entry to be stored
     *                - must not be null
     * @return null if entity successfully stored
     *          the entity if it already exists in the entries
     * @throws ValidationException if the entity is not valid
     * @throws IllegalArgumentException if the given entity is null.
     */
    ElemType store(ElemType entity);

    /**
     * Removes the entity with the specified id
     * @param id
     *      id must be not null
     * @return the removed entity or null if there is no entity with the given id
     * @throws IllegalArgumentException
     *                   if the given id is null.
     */
    ElemType delete(ID id);

    /**
     * Updates an entity
     * @param entity
     *          entity must not be null
     * @return null - if the entity is updated,
     *                otherwise  returns the entity  - (e.g id does not exist).
     * @throws IllegalArgumentException
     *             if the given entity is null.
     * @throws ValidationException
     *             if the entity is not valid.
     */
    ElemType update(ElemType entity);
}
