package com.sn.socialnetwork.domain;

public class Conversation extends Entity<Long>{
    private Long firstUserId, secondUserId;
    public Conversation(Long convoId, Long firstUserId, Long secondUserId) {
        super(convoId);
        this.firstUserId = firstUserId;
        this.secondUserId = secondUserId;
    }

    public Long getFirstUserId() {
        return firstUserId;
    }
    public void setFirstUserId(Long firstUserId) {
        this.firstUserId = firstUserId;
    }
    public Long getSecondUserId() {
        return secondUserId;
    }
    public void setSecondUserId(Long secondUserId) {
        this.secondUserId = secondUserId;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(!(obj instanceof Conversation)) return false;
        Conversation o = (Conversation) obj;
        return (firstUserId.equals(o.getFirstUserId()) && secondUserId.equals(o.getSecondUserId()))
                || (firstUserId.equals(o.getSecondUserId()) && secondUserId.equals(o.getFirstUserId()));
    }
}
