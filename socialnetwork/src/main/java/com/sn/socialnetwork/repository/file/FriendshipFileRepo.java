package com.sn.socialnetwork.repository.file;

import com.sn.socialnetwork.domain.Friendship;
import com.sn.socialnetwork.utils.FriendshipStatus;
import com.sn.socialnetwork.utils.Pair;
import com.sn.socialnetwork.validators.Validator;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class FriendshipFileRepo extends FileRepository<Pair<Long, Long>, Friendship> {
    public FriendshipFileRepo(Validator<Friendship> validator, String filename) {
        super(validator, filename);
    }

    @Override
    protected String entity_to_string(Friendship ent) {
        LocalDateTime d = ent.getDate();
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        return ent.getFirstID()+"-"+ent.getSecondID()+"-"+formatter.format(d)+"\n";
    }


    @Override
    protected Friendship string_to_entity(String line) {
        String[] attr = line.split("-");
        Pair<Long, Long> id = new Pair<>(Long.parseLong(attr[0]), Long.parseLong(attr[1]));
        LocalDateTime date = null;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        date = LocalDateTime.parse(attr[2], formatter);
        FriendshipStatus status = FriendshipStatus.valueOf(attr[3]);
        return new Friendship(id, date, status);
    }
}
