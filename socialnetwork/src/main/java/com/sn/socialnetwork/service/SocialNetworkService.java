package com.sn.socialnetwork.service;

import com.sn.socialnetwork.domain.Conversation;
import com.sn.socialnetwork.domain.Friendship;
import com.sn.socialnetwork.domain.Message;
import com.sn.socialnetwork.domain.User;
import com.sn.socialnetwork.repository.Repository;
import com.sn.socialnetwork.repository.database.ConversationDbRepository;
import com.sn.socialnetwork.repository.database.MessagesDbRepository;
import com.sn.socialnetwork.utils.FriendshipStatus;
import com.sn.socialnetwork.utils.Pair;
import com.sn.socialnetwork.validators.ValidationException;

import java.time.LocalDateTime;
import java.util.ArrayList;

public class SocialNetworkService {
    private Repository<Long, User> usersRepo;
    private Repository<Pair<Long, Long>, Friendship> friendshipsRepo;
    private ConversationDbRepository converstionsRepo;
    private MessagesDbRepository messagesRepo;

    private User currentUser;

    public SocialNetworkService(Repository<Long, User> usersRepoN,
                                Repository<Pair<Long, Long>, Friendship> friendshipsRepoN, ConversationDbRepository converstionsRepo, MessagesDbRepository messagesRepo) {
        usersRepo = usersRepoN;
        friendshipsRepo = friendshipsRepoN;
        this.converstionsRepo = converstionsRepo;
        this.messagesRepo = messagesRepo;
    }

    /**
     * Adds a new user in the social network
     * @param firstname - firstname of the user to be added
     * @param lastname - lastname of the user to be added
     * @param email - email of the user to be added
     *
     * @throws ValidationException if data is invalid
     * @throws IllegalArgumentException if the entity to be added is null
     */
    public void add_user(String firstname, String lastname, String email, String username, String password){
        User newUser = new User((long) -1, firstname, lastname, email, username, password);
        usersRepo.store(newUser);
    }

    /**
     * Deletes a user from the social network
     * @param id - the id of the user to be deleted
     *           - must not be null
     * @throws IllegalArgumentException if given id is null
     */
    public void delete_user(Long id){
        usersRepo.delete(id);
        ArrayList<Long> userIds = new ArrayList<>();
        for (Friendship f: friendshipsRepo.getAll()) {
            if(f.getFirstID().equals(id)){
                userIds.add(f.getSecondID());
            }
            if(f.getSecondID().equals(id)){
                userIds.add(f.getFirstID());
            }
        }
        for (Long uid: userIds ) {
            Pair<Long, Long> pair = new Pair<>(id, uid);
            Friendship f = friendshipsRepo.delete(pair);
        }
    }

    public Iterable<User> get_all_users(){
        return usersRepo.getAll();
    }

    /**
     * Adds a friendship in the social network
     * @param id1 - id of one of the users
     * @param id2 - id of the other user
     *
     * @throws ValidationException if the given id-s are the same
     * @throws IllegalArgumentException if the entity to be added is null
     */
    public void add_friendship(Long id1, Long id2){
        Pair<Long, Long> pair = new Pair<>(id1, id2);
        LocalDateTime data = LocalDateTime.now();
        Friendship friendship = new Friendship(pair, data, FriendshipStatus.pending);
        friendshipsRepo.store(friendship);
    }

    /**
     * Deletes a friendship from the social network
     * @param uid1 - id of one of the users
     * @param uid2 - id of the other user
     *
     * @throws ValidationException if the given id-s are the same
     * @throws IllegalArgumentException if the entity to be added is null
     */
    public void delete_friendship(Long uid1, Long uid2){
        Pair<Long, Long> pair = new Pair<>(uid1, uid2);
        friendshipsRepo.delete(pair);
        Conversation convo = converstionsRepo.findOneByUserIds(uid1, uid2);
        if(convo != null) {
            converstionsRepo.delete(convo.getId());
            messagesRepo.deleteAllFromConversation(convo.getId());
        }
    }

    public Iterable<Friendship> get_all_friendships(){
        return friendshipsRepo.getAll();
    }

    public User get_user_by_id(Long uid){
        Iterable<User> allUsers = usersRepo.getAll();
        for(User u: allUsers){
            if (u.getId().equals(uid)){
                return u;
            }
        }
        return null;
    }

    public Iterable<User> get_unrelated_users(Long userId){
        ArrayList<User> unrelated_users = new ArrayList<User>();
        for (User x : usersRepo.getAll()) {
            if (friendshipsRepo.findOne(new Pair<>(x.getId(),userId)) == null && !(x.getId().equals(userId))){
                unrelated_users.add(x);
            }
        }
        return unrelated_users;
    }

    public User get_user_by_username(String username){
        Iterable<User> allUsers = usersRepo.getAll();
        for(User u: allUsers){
            if (u.getUsername().equals(username)){
                return u;
            }
        }
        return null;
    }

    public User getCurrentUser() {
        return currentUser;
    }

    public void setCurrentUser(User currentUser) {
        this.currentUser = currentUser;
    }

    public void update_friendship_status(Long uid1, Long uid2, FriendshipStatus status){
        Pair<Long, Long> pair = new Pair<>(uid1, uid2);
        LocalDateTime data = LocalDateTime.now();
        Friendship friendship = new Friendship(pair, data, status);
        friendshipsRepo.update(friendship);
        if(status.equals(FriendshipStatus.accepted)){
            converstionsRepo.store(new Conversation((long) -1, uid1, uid2));
        }
    }

    public void send_message(Long sender_id, Long receiver_id, String text){
        Conversation convo = converstionsRepo.findOneByUserIds(sender_id, receiver_id);
        LocalDateTime timeOfSending = LocalDateTime.now();
        if(text != null){
            messagesRepo.store(new Message((long) -1, sender_id, receiver_id, convo.getId(), text, timeOfSending));
        }
    }
    public Iterable<Message> getAllFromConversation(Long uid1, Long uid2){
        Conversation convo = converstionsRepo.findOneByUserIds(uid1, uid2);
        ///System.out.printf("Id-ul conversatiei frate: " + convo.getId().toString());
        return messagesRepo.getAllInConversation(convo.getId());
    }
}
