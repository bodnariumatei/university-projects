package com.sn.socialnetwork;

import com.sn.socialnetwork.repository.database.ConversationDbRepository;
import com.sn.socialnetwork.repository.database.FriendshipDbRepository;
import com.sn.socialnetwork.repository.database.MessagesDbRepository;
import com.sn.socialnetwork.repository.database.UsersDbRepository;
import com.sn.socialnetwork.service.SocialNetworkService;
import com.sn.socialnetwork.ui.gui.LoginController;
import com.sn.socialnetwork.validators.FriendshipValidator;
import com.sn.socialnetwork.validators.UserValidator;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loginLoader = new FXMLLoader(Main.class.getResource("/com/sn/socialnetwork/ui/gui/loginScene.fxml"));
        Parent root = loginLoader.load();
        SocialNetworkService srv = prepareService();

        LoginController loginController = loginLoader.getController();
        loginController.setService(srv);

        Scene loginScene = new Scene(root, 650, 450);
        stage.setTitle("Social Network");
        stage.setScene(loginScene);
        stage.setMinHeight(450);
        stage.setMinWidth(650);
        Image icon = new Image("/logo-01.jpg");
        stage.getIcons().add(icon);
        stage.show();
    }

    private static SocialNetworkService prepareService(){
        UserValidator userValidator = new UserValidator();
        FriendshipValidator friendshipValidator = new FriendshipValidator();
        UsersDbRepository usersRepo = new UsersDbRepository(
                "jdbc:postgresql://localhost:5432/socialnetwork","postgres", "postgres", userValidator);
        FriendshipDbRepository friendshipsRepo = new FriendshipDbRepository(
                "jdbc:postgresql://localhost:5432/socialnetwork","postgres", "postgres", friendshipValidator);
        ConversationDbRepository converstionsRepo = new ConversationDbRepository(
                "jdbc:postgresql://localhost:5432/socialnetwork","postgres", "postgres");
        MessagesDbRepository messagesRepo = new MessagesDbRepository(
                "jdbc:postgresql://localhost:5432/socialnetwork","postgres", "postgres");
        SocialNetworkService srv = new SocialNetworkService(usersRepo, friendshipsRepo, converstionsRepo, messagesRepo);
        return srv;
    }

    public static void main(String[] args){
        launch();
    }
}