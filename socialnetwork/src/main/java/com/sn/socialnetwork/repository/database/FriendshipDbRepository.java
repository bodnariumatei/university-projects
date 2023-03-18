package com.sn.socialnetwork.repository.database;

import com.sn.socialnetwork.domain.Friendship;
import com.sn.socialnetwork.utils.FriendshipStatus;
import com.sn.socialnetwork.repository.Repository;
import com.sn.socialnetwork.utils.Pair;
import com.sn.socialnetwork.validators.Validator;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

public class FriendshipDbRepository implements Repository<Pair<Long, Long>, Friendship> {
    private String url;
    private String username;
    private String password;
    private Validator<Friendship> validator;

    public FriendshipDbRepository(String url, String username, String password, Validator<Friendship> validator) {
        this.url = url;
        this.username = username;
        this.password = password;
        this.validator = validator;
    }

    @Override
    public Friendship findOne(Pair<Long, Long> friendshipId) {
        Iterable<Friendship> allFs = getAll();
        for (Friendship f : allFs){
            if(f.getId().equals(friendshipId))
                return f;
        }
        return null;
    }

    @Override
    public Iterable<Friendship> getAll() {
        Set<Friendship> friendships = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from friendships");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long first_user_id = resultSet.getLong("first_user_id");
                Long second_user_id = resultSet.getLong("second_user_id");
                LocalDateTime date = resultSet.getTimestamp("date").toLocalDateTime();
                FriendshipStatus status = FriendshipStatus.valueOf(resultSet.getString("status"));

                friendships.add(new Friendship(new Pair<>(first_user_id, second_user_id), date, status));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return friendships;
    }

    @Override
    public Friendship store(Friendship entity) {
        validator.validate(entity);
        String sql = "insert into friendships (first_user_id, second_user_id, date, status) values (?, ?, ?, ?)";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setLong(1, entity.getFirstID());
            ps.setLong(2, entity.getSecondID());
            ps.setTimestamp(3,Timestamp.valueOf(entity.getDate()));
            ps.setString(4, entity.getStatus().toString());

            ps.executeUpdate();
        } catch (SQLException e) {
            //e.printStackTrace();
            return entity;
        }
        return null;
    }

    @Override
    public Friendship delete(Pair<Long, Long> friendshipId) {
        String sql = "DELETE FROM friendships WHERE first_user_id = ? AND second_user_id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {
            Friendship friendship = findOne(friendshipId);
            ps.setLong(1, friendship.getFirstID());
            ps.setLong(2, friendship.getSecondID());
            ps.executeUpdate();
            return friendship;
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }

    @Override
    public Friendship update(Friendship newFriendship) {
        String sql = "UPDATE friendships SET date = ?, status = ? WHERE (first_user_id = ? AND second_user_id = ?)" +
                "OR (first_user_id = ? AND second_user_id = ?)";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setTimestamp(1, Timestamp.valueOf(newFriendship.getDate()));
            ps.setString(2, newFriendship.getStatus().toString());
            ps.setLong(3, newFriendship.getFirstID());
            ps.setLong(4, newFriendship.getSecondID());
            ps.setLong(5, newFriendship.getSecondID());
            ps.setLong(6, newFriendship.getFirstID());

            ps.executeUpdate();
            return null;

        } catch (SQLException e) {
            //e.printStackTrace();
            return newFriendship;
        }
    }
}
