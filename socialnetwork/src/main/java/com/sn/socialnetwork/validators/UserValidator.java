package com.sn.socialnetwork.validators;

import com.sn.socialnetwork.domain.User;

public class UserValidator implements Validator<User>{

    @Override
    public void validate(User entity) throws ValidationException {
        if(entity.getFirstname().isEmpty() || entity.getLastname().isEmpty())
            throw new ValidationException("Firstname and Lastname can't be null");
        String[] mail_provider = entity.getEmail().split("@");
        if(mail_provider.length != 2){
            throw new ValidationException("Mail has to respect format: 'mail@provider.domain'");
        }
        String[] provider_domain = mail_provider[1].split("\\.");
        if (provider_domain.length != 2){
            throw new ValidationException("Mail has to respect format: 'mail@provider.domain'");
        }
    }

//    @Override
//    public void validate_unique(Iterable<User> allUsers, User newUser){
//        for(User u : allUsers){
//            if (newUser.equals(u)){
//                throw new ValidationException("This user already registered.");
//            }
//        }
//    }
}
