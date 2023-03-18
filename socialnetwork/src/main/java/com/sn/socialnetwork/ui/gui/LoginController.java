package com.sn.socialnetwork.ui.gui;

import com.sn.socialnetwork.domain.User;
import com.sn.socialnetwork.service.SocialNetworkService;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class LoginController {
    private SocialNetworkService srv;

    @FXML
    private Button loginButton;
    @FXML
    private TextField usernameTextField;
    @FXML
    private PasswordField passwordField;

    @FXML
    private Label errorLabel;

    @FXML
    public void login() throws IOException {
        if(usernameTextField.getText() == "" || passwordField.getText() == "") {
            errorLabel.setText("Username and password can't be empty!");
            return;
        }
        User user = srv.get_user_by_username(usernameTextField.getText());
        if (user == null) {
            errorLabel.setText("Wrong username/passoword!");
            return;
        } else if (!(user.getPassword().equals(passwordField.getText()))) {
            errorLabel.setText("Wrong username/passoword!");
            return;
        }

        FXMLLoader loader = new FXMLLoader(getClass().getResource("mainAppScene.fxml"));
        Parent root = loader.load();

        MainAppController mainAppController = loader.getController();
        srv.setCurrentUser(user);
        mainAppController.setService(srv);
        mainAppController.loadAppScene();

        Stage stage = (Stage) loginButton.getScene().getWindow();
        Scene scene = new Scene(root);
        stage.setScene(scene);
    }

    public void setService(SocialNetworkService newSrv){
        this.srv = newSrv;
    }
}