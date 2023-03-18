package com.sn.socialnetwork.repository.database;

import com.sn.socialnetwork.domain.Conversation;
import com.sn.socialnetwork.repository.Repository;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;

public class ConversationDbRepository implements Repository<Long, Conversation> {

    private String url;
    private String username;
    private String password;

    public ConversationDbRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Conversation findOne(Long convoId) {
        String sql = "SELECT * FROM conversations WHERE convo_id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setLong(1, convoId);
            ResultSet resultSet = statement.executeQuery();

            Long cid = resultSet.getLong("convo_id");
            Long firstUserId =  resultSet.getLong("first_user_id");
            Long secondUserId =  resultSet.getLong("second_user_id");
            return new Conversation(cid, firstUserId, secondUserId);
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }

    public Conversation findOneByUserIds(Long firstUserId, Long secondUserId) {
        Iterable<Conversation> allConvos = getAll();
        for (Conversation conv : allConvos){
            if((conv.getFirstUserId().equals(firstUserId) && conv.getSecondUserId().equals(secondUserId)) ||
                    (conv.getFirstUserId().equals(secondUserId) && conv.getSecondUserId().equals(firstUserId)))
                return conv;
        }
        return null;
    }
    @Override
    public Iterable<Conversation> getAll() {
        Set<Conversation> conversations = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from conversations");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long convoId = resultSet.getLong("convo_id");
                Long firstUserId = resultSet.getLong("first_user_id");
                Long secondUserId = resultSet.getLong("second_user_id");

                Conversation convo = new Conversation(convoId, firstUserId, secondUserId);
                conversations.add(convo);
            }
        } catch (SQLException e) {
            //e.printStackTrace();
        }
        return conversations;
    }
    @Override
    public Conversation store(Conversation entity) {
        if(findOneByUserIds(entity.getFirstUserId(), entity.getSecondUserId()) == null) {
            String sql = "insert into conversations (first_user_id, second_user_id) values (?, ?)";
            try (Connection connection = DriverManager.getConnection(url, username, password);
                 PreparedStatement ps = connection.prepareStatement(sql)) {

                ps.setLong(1, entity.getFirstUserId());
                ps.setLong(2, entity.getSecondUserId());
                ps.executeUpdate();
            } catch (SQLException e) {
                //e.printStackTrace();
                return entity;
            }
            return null;
        } else{
            return entity;
        }
    }
    @Override
    public Conversation delete(Long convoId) {
        String sql = "DELETE FROM conversations WHERE convo_id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {
            Conversation convo = findOne(convoId);
            ps.setLong(1, convoId);
            ps.executeUpdate();
            return convo;
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }
    @Override
    public Conversation update(Conversation entity) {
        return null;
    }
}
