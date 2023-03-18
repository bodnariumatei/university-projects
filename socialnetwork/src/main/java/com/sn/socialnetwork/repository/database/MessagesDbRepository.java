package com.sn.socialnetwork.repository.database;

import com.sn.socialnetwork.domain.Message;
import com.sn.socialnetwork.repository.Repository;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

public class MessagesDbRepository implements Repository<Long, Message> {
    private String url;
    private String username;
    private String password;

    public MessagesDbRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Message findOne(Long msgId) {
        String sql = "SELECT * FROM messages WHERE mid = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setLong(1, msgId);
            ResultSet resultSet = statement.executeQuery();

            Long mid = resultSet.getLong("mid");
            Long senderId =  resultSet.getLong("sender_id");
            Long receiverId =  resultSet.getLong("receiver_id");
            Long convo_id = resultSet.getLong("convo_id");
            String text = resultSet.getString("text");
            LocalDateTime timeOfSending = resultSet.getTimestamp("time_of_sending").toLocalDateTime();
            return new Message(mid, senderId, receiverId, convo_id, text, timeOfSending);
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }
    @Override
    public Iterable<Message> getAll() {
        Set<Message> messages = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from messages");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long mid = resultSet.getLong("mid");
                Long senderId =  resultSet.getLong("sender_id");
                Long receiverId =  resultSet.getLong("receiver_id");
                Long convoId = resultSet.getLong("convo_id");
                String text = resultSet.getString("text");
                LocalDateTime timeOfSending = resultSet.getTimestamp("time_of_sending").toLocalDateTime();

                Message msg = new Message(mid, senderId, receiverId, convoId, text, timeOfSending);
                messages.add(msg);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return messages;
    }
    @Override
    public Message store(Message entity) {
        String sql = "insert into messages (sender_id, receiver_id, convo_id, text, time_of_sending) values (?, ?, ?, ?, ?)";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setLong(1, entity.getSenderId());
            ps.setLong(2, entity.getReceiverId());
            ps.setLong(3, entity.getConvoId());
            ps.setString(4, entity.getText());
            ps.setTimestamp(5, Timestamp.valueOf(entity.getTimeOfSending()));

            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
            return entity;
        }
        return null;
    }
    @Override
    public Message delete(Long msgId) {
        String sql = "delete from messages where mid = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {
            Message msg = findOne(msgId);
            ps.setLong(1, msgId);
            ps.executeUpdate();
            return msg;
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }
    @Override
    public Message update(Message entity) {
        return null;
    }

    public Iterable<Message> getAllInConversation(Long convoId){
        Set<Message> messages = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from messages WHERE convo_id = ?")) {
            statement.setLong(1, convoId);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                Long mid = resultSet.getLong("mid");
                Long senderId =  resultSet.getLong("sender_id");
                Long receiverId =  resultSet.getLong("receiver_id");
                Long cId = resultSet.getLong("convo_id");
                String text = resultSet.getString("text");
                LocalDateTime timeOfSending = resultSet.getTimestamp("time_of_sending").toLocalDateTime();

                Message msg = new Message(mid, senderId, receiverId, cId, text, timeOfSending);
                messages.add(msg);
            }
        } catch (SQLException e) {
            //e.printStackTrace();
        }
        return messages.stream().sorted(new Comparator<Message>() {
            @Override
            public int compare(Message o1, Message o2) {
                return (int) (o2.getId()-o1.getId());
            }
        }).toList();
    }

    public void deleteAllFromConversation(Long convoId){
        String sql = "delete from messages where convo_id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setLong(1, convoId);
            ps.executeUpdate();
        } catch (SQLException e) {
            //e.printStackTrace();
        }
    }
}
