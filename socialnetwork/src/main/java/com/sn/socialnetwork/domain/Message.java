package com.sn.socialnetwork.domain;

import java.time.LocalDateTime;

public class Message extends Entity<Long>{
    private Long senderId, receiverId, convoId;
    private String text;
    private LocalDateTime timeOfSending;

    public Message(Long msgId, Long senderId, Long receiverId, Long convoId, String text, LocalDateTime timeOfSending) {
        super(msgId);
        this.senderId = senderId;
        this.receiverId = receiverId;
        this.convoId = convoId;
        this.text = text;
        this.timeOfSending = timeOfSending;
    }

    public Long getReceiverId() {
        return receiverId;
    }

    public Long getSenderId() {
        return senderId;
    }

    public String getText() {
        return text;
    }

    public LocalDateTime getTimeOfSending() {
        return timeOfSending;
    }

    public Long getConvoId() {
        return convoId;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(!(obj instanceof Message)) return false;
        Message o = (Message) obj;
        return getId().equals(o.getId());
    }
}
