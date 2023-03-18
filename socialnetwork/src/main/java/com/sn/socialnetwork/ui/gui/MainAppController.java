package com.sn.socialnetwork.ui.gui;

import com.sn.socialnetwork.domain.User;
import com.sn.socialnetwork.service.SocialNetworkService;
import com.sn.socialnetwork.utils.FriendshipStatus;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.SelectionMode;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import java.io.IOException;


public class MainAppController {
    SocialNetworkService srv;
    @FXML
    ListView<String> friendsListView;
    @FXML
    ListView<String> sentRequestsListView;
    @FXML
    ListView<String> pendingRequestsListView;
    @FXML
    ListView<String> otherUsersListView;
    @FXML
    private Label fullNameLabel;
    @FXML
    private Label usernameLabel;
    @FXML
    private Button addFriendButton;
    @FXML
    private Button removeFriendButton;
    @FXML
    private Button unsendRequestButton;
    @FXML
    private Button acceptRequestButton;
    @FXML
    private Button rejectRequestButton;
    @FXML
    private Button openMessagesButton;

    @FXML
    public void logout(ActionEvent event) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("loginScene.fxml"));
        Parent root = loader.load();

        LoginController loginController = loader.getController();
        srv.setCurrentUser(null);
        loginController.setService(srv);

        Stage stage = (Stage) ((Node)event.getSource()).getScene().getWindow();
        Scene scene = new Scene(root);
        stage.setScene(scene);
    }

    public void setService(SocialNetworkService newSrv){
        this.srv = newSrv;
    }

    public void loadAppScene(){
        User u = srv.getCurrentUser();
        fullNameLabel.setText(u.getFirstname() + " " + u.getLastname());
        usernameLabel.setText(u.getUsername());

        friendsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        otherUsersListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        pendingRequestsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        sentRequestsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);

        loadListViews();
        loadOtherUsersListView();
    }
    private void loadListViews() {
        friendsListView.getItems().clear();
        pendingRequestsListView.getItems().clear();
        sentRequestsListView.getItems().clear();
        srv.get_all_friendships().forEach(x -> {
            Long cuid = srv.getCurrentUser().getId();
            if(x.getFirstID().equals(cuid) && x.getStatus() == FriendshipStatus.accepted){
                User friend = srv.get_user_by_id(x.getSecondID());
                String userinfo = friend.getId().toString() + " - " + friend.getFirstname()
                        + " " + friend.getLastname() + " - email: " + friend.getEmail();
                friendsListView.getItems().add(userinfo);
            }
            if(x.getSecondID().equals(cuid) && x.getStatus() == FriendshipStatus.accepted){
                User friend = srv.get_user_by_id(x.getFirstID());
                String userinfo = friend.getId().toString() + " - " + friend.getFirstname()
                        + " " + friend.getLastname() + " - email: " + friend.getEmail();
                friendsListView.getItems().add(userinfo);
            }
            if(x.getSecondID().equals(cuid) && x.getStatus() == FriendshipStatus.pending){
                User friend = srv.get_user_by_id(x.getFirstID());
                String userinfo = friend.getId().toString() + " - " + friend.getFirstname() + " " + friend.getLastname();
                pendingRequestsListView.getItems().add(userinfo);
            }
            if(x.getFirstID().equals(cuid) && x.getStatus() == FriendshipStatus.pending){
                User friend = srv.get_user_by_id(x.getSecondID());
                String userinfo = friend.getId().toString() + " - " + friend.getFirstname() + " " + friend.getLastname();
                sentRequestsListView.getItems().add(userinfo);
            }
        });
    }
    private void loadOtherUsersListView() {
        otherUsersListView.getItems().clear();
        srv.get_unrelated_users(srv.getCurrentUser().getId()).forEach(x ->{
            String userinfo = x.getId().toString() + " - " + x.getFirstname() + " " + x.getLastname();
            otherUsersListView.getItems().add(userinfo);
        });
    }

    @FXML
    private void addFriendAction(){
        String selection = otherUsersListView.getSelectionModel().getSelectedItem();
        if(selection != null){
            String[] attr = selection.split(" - ");
            User cUser = srv.getCurrentUser();
            srv.add_friendship(cUser.getId(), Long.parseLong(attr[0]));

            loadOtherUsersListView();
            loadListViews();
        } else {
            System.out.println("Not good amigo!");
        }
    }
    @FXML
    private void removeFriendAction(){
        String selection = friendsListView.getSelectionModel().getSelectedItem();
        if(selection != null){
            String[] attr = selection.split(" - ");
            User cUser = srv.getCurrentUser();
            srv.delete_friendship(cUser.getId(), Long.parseLong(attr[0]));

            loadOtherUsersListView();
            loadListViews();
        } else {
            System.out.println("Not good amigo!");
        }
    }
    @FXML
    private void acceptRequestAction(){
        String selection = pendingRequestsListView.getSelectionModel().getSelectedItem();
        if(selection != null){
            String[] attr = selection.split(" - ");
            User cUser = srv.getCurrentUser();
            srv.update_friendship_status(cUser.getId(), Long.parseLong(attr[0]), FriendshipStatus.accepted);

            loadOtherUsersListView();
            loadListViews();
        } else {
            System.out.println("Not good amigo!");
        }
    }
    @FXML
    private void rejectRequestAction(){
        String selection = pendingRequestsListView.getSelectionModel().getSelectedItem();
        if(selection != null){
            String[] attr = selection.split(" - ");
            User cUser = srv.getCurrentUser();
            srv.delete_friendship(Long.parseLong(attr[0]), cUser.getId());

            loadOtherUsersListView();
            loadListViews();
        } else {
            System.out.println("Not good amigo!");
        }
    }
    @FXML
    private void unsendRequestAction(){
        String selection = sentRequestsListView.getSelectionModel().getSelectedItem();
        if(selection != null){
            String[] attr = selection.split(" - ");
            User cUser = srv.getCurrentUser();
            srv.delete_friendship(cUser.getId(), Long.parseLong(attr[0]));

            loadOtherUsersListView();
            loadListViews();
        } else {
            System.out.println("Not good amigo!");
        }
    }
    @FXML
    private void openMessagesScene() throws IOException {
        Stage secondStage = new Stage();
        FXMLLoader loader = new FXMLLoader(getClass().getResource("messgsScene.fxml"));
        Parent root = loader.load();

        MessgsAppController messgsAppController = loader.getController();
        messgsAppController.setService(srv);
        messgsAppController.loadScene();

        secondStage.setScene(new Scene(root));
        secondStage.setTitle("MokUp Messgs");
        Image icon = new Image("/logo-01.jpg");
        secondStage.getIcons().add(icon);
        secondStage.setResizable(false);
        secondStage.show();
    }
}
