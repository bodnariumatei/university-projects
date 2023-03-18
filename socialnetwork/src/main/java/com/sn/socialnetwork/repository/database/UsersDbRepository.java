package com.sn.socialnetwork.repository.database;

import com.sn.socialnetwork.domain.User;
import com.sn.socialnetwork.repository.Repository;
import com.sn.socialnetwork.validators.Validator;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;

public class UsersDbRepository implements Repository<Long, User> {
    private String url;
    private String username;
    private String password;
    private Validator<User> validator;

    public UsersDbRepository(String url, String username, String password, Validator<User> validator) {
        this.url = url;
        this.username = username;
        this.password = password;
        this.validator = validator;
    }
    @Override
    public User findOne(Long userId) {
        String sql = "SELECT * FROM users WHERE id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setLong(1, userId);
            ResultSet resultSet = statement.executeQuery();

            Long id = resultSet.getLong("id");
            String firstName = resultSet.getString("first_name");
            String lastName = resultSet.getString("last_name");
            String email = resultSet.getString("email");
            String userUsername = resultSet.getString("username");
            String userPassword = resultSet.getString("password");
            return new User(id, firstName, lastName, email, userUsername, userPassword);
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }

    @Override
    public Iterable<User> getAll() {
        Set<User> users = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from users");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String firstName = resultSet.getString("first_name");
                String lastName = resultSet.getString("last_name");
                String email = resultSet.getString("email");
                String userUsername = resultSet.getString("username");
                String userPassword = resultSet.getString("password");

                User utilizator = new User(id, firstName, lastName, email, userUsername, userPassword);
                users.add(utilizator);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }

    @Override
    public User store(User entity) {
        String sql = "insert into users (first_name, last_name, email, username, password) values (?, ?, ?, ?, ?)";
        validator.validate(entity);
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, entity.getFirstname());
            ps.setString(2, entity.getLastname());
            ps.setString(3, entity.getEmail());
            ps.setString(4, entity.getUsername());
            ps.setString(5, entity.getPassword());

            ps.executeUpdate();
        } catch (SQLException e) {
            //e.printStackTrace();
            return entity;
        }
        return null;
    }

    @Override
    public User delete(Long userId) {
        String sql = "delete from users where id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {
            User user = findOne(userId);
            ps.setLong(1, userId);
            ps.executeUpdate();
            return user;
        } catch (SQLException e) {
            //e.printStackTrace();
            return null;
        }
    }

    @Override
    public User update(User newUser) {
        String sql = "UPDATE users SET first_name = ?, last_name = ?, email = ?, username = ?, password = ? WHERE id = ?";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, newUser.getFirstname());
            ps.setString(2, newUser.getLastname());
            ps.setString(3, newUser.getEmail());
            ps.setString(4, newUser.getEmail());
            ps.setString(5, newUser.getEmail());
            ps.setLong(6, newUser.getId());

            ps.executeUpdate();
            return null;
        } catch (SQLException e) {
            //e.printStackTrace();
            return newUser;
        }
    }
}
