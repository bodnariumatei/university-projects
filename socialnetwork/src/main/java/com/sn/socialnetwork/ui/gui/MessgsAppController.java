package com.sn.socialnetwork.ui.gui;

import com.sn.socialnetwork.domain.Message;
import com.sn.socialnetwork.domain.User;
import com.sn.socialnetwork.service.SocialNetworkService;
import com.sn.socialnetwork.utils.FriendshipStatus;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.time.format.DateTimeFormatter;
import java.util.Objects;

public class MessgsAppController {
    private SocialNetworkService srv;
    @FXML
    ListView<String> friendsListView;
    @FXML
    ListView<String> conversationMessagesListView;
    @FXML
    Button openConversationButton;
    @FXML
    Button sendMessageButton;
    @FXML
    TextField messageTextField;

    @FXML
    Label conversationTitleLabel;

    private User currentReceiverUser;

    public void setService(SocialNetworkService newSrv){
        this.srv = newSrv;
    }

    public void loadScene(){
        sendMessageButton.setDisable(true);

        friendsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        friendsListView.getItems().clear();
        srv.get_all_friendships().forEach(x -> {
            Long cuid = srv.getCurrentUser().getId();
            if (x.getFirstID().equals(cuid) && x.getStatus() == FriendshipStatus.accepted) {
                User friend = srv.get_user_by_id(x.getSecondID());
                String userinfo = friend.getId().toString() + " - " + friend.getFirstname()
                        + " " + friend.getLastname();
                friendsListView.getItems().add(userinfo);
            }
            if (x.getSecondID().equals(cuid) && x.getStatus() == FriendshipStatus.accepted) {
                User friend = srv.get_user_by_id(x.getFirstID());
                String userinfo = friend.getId().toString() + " - " + friend.getFirstname()
                        + " " + friend.getLastname();
                friendsListView.getItems().add(userinfo);
            }
        });
    }

    @FXML
    private void openConversationAction(){
        String selection = friendsListView.getSelectionModel().getSelectedItem();
        if(selection != null){
            String[] attr = selection.split(" - ");
            currentReceiverUser = srv.get_user_by_id(Long.valueOf(attr[0]));
            loadMessagesListView();
            sendMessageButton.setDisable(false);
            conversationTitleLabel.setText("Conversatie cu " + currentReceiverUser.getFirstname());
        } else {
            System.out.println("Not good amigo!");
        }
    }
    @FXML
    private void sendMessageAction(){
        String text = messageTextField.getText();
        if(!Objects.equals(text, "")) {
            Long sender_id = srv.getCurrentUser().getId();
            Long receiver_id = currentReceiverUser.getId();
            srv.send_message(sender_id, receiver_id, text);
            loadMessagesListView();
            messageTextField.setText("");
        } else {
            System.out.println("Good one hahaha");
        }
    }

    private void loadMessagesListView(){
        conversationMessagesListView.getItems().clear();
        User u1 = srv.getCurrentUser();
        User u2 = currentReceiverUser;
        Iterable<Message> messages = srv.getAllFromConversation(u1.getId(), u2.getId());
        messages.forEach(msg -> {
            if(msg.getSenderId().equals(u1.getId())){
                DateTimeFormatter customFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");;
                String timeOfSendingString = msg.getTimeOfSending().format(customFormat);
                String messageInfo = timeOfSendingString + " :\t " + msg.getText();
                conversationMessagesListView.getItems().add(messageInfo);
            } else {
                DateTimeFormatter customFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");;
                String timeOfSendingString = msg.getTimeOfSending().format(customFormat);
                String messageInfo = timeOfSendingString + " - from " + u2.getFirstname() + " : " + msg.getText();
                conversationMessagesListView.getItems().add(messageInfo);
            }
        });
    }
}
