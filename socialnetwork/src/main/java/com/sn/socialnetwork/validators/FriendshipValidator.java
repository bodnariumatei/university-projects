package com.sn.socialnetwork.validators;

import com.sn.socialnetwork.domain.Friendship;

public class FriendshipValidator implements Validator<Friendship> {
    @Override
    public void validate(Friendship entity) throws ValidationException {
        if(entity.getFirstID().equals(entity.getSecondID()))
            throw new ValidationException("Members of a friendship must have different ids!");
    }

//    @Override
//    public void validate_unique(Iterable<Friendship> allEntities, Friendship newEntity) throws ValidationException {
//        for(Friendship f : allEntities){
//            if(newEntity.equals(f)){
//                throw new ValidationException("Users already friends");
//            }
//        }
//    }
}
