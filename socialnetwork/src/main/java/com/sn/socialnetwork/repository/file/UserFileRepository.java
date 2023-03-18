package com.sn.socialnetwork.repository.file;

import com.sn.socialnetwork.domain.User;
import com.sn.socialnetwork.validators.Validator;

public class UserFileRepository extends FileRepository<Long, User> {

    public UserFileRepository(Validator<User> validator, String filename) {
        super(validator, filename);
    }

    @Override
    protected String entity_to_string(User ent) {
        return ent.getId() + "-" + ent.getFirstname() + "-" + ent.getLastname() + "-" + ent.getEmail() + "\n";
    }

    @Override
    protected User string_to_entity(String line) {
        String[] attr = line.split("-");
        return new User(Long.parseLong(attr[0]), attr[1], attr[2], attr[3], attr[4], attr[5]);
    }
}
