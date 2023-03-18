package com.sn.socialnetwork.domain;

import com.sn.socialnetwork.utils.FriendshipStatus;
import com.sn.socialnetwork.utils.Pair;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Friendship extends Entity<Pair<Long, Long>>{
    private LocalDateTime friendsFrom;
    private FriendshipStatus status;

    public Friendship(Pair<Long, Long> fid, LocalDateTime data, FriendshipStatus status) {
        super(fid);
        this.friendsFrom = data;
        this.status = status;
    }

    public Long getFirstID(){
        return getId().getFirstId();
    }
    public Long getSecondID(){
        return getId().getSecondId();
    }

    public LocalDateTime getDate() {
        return friendsFrom;
    }

    public boolean isInFriendship(Long uid){
        return getId().getFirstId().equals(uid) || getId().getSecondId().equals(uid);
    }

    //public Date getData() { return data; }
    public FriendshipStatus getStatus() {
        return status;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(!(obj instanceof Friendship)) return false;
        Friendship o = (Friendship) obj;
        return getId().equals(o.getId());
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        return "ID1 " + getFirstID() + " - " + "ID2 " + getSecondID() + " - " + friendsFrom.format(formatter);
    }

    public void changeStatus(FriendshipStatus status, LocalDateTime newDate){
        this.status = status;
        this.friendsFrom = newDate;
    }
}
