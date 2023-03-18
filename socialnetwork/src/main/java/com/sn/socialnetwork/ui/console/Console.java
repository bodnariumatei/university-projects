package com.sn.socialnetwork.ui.console;

import com.sn.socialnetwork.service.SocialNetworkService;
import com.sn.socialnetwork.validators.ValidationException;

import java.util.Scanner;

public class Console {
    private SocialNetworkService srv;

    public Console(SocialNetworkService srv) {
        this.srv = srv;
    }

    public void startUI(){
        //populate();
        Scanner scanner = new Scanner(System.in);
        while(true){
            int cmd;
            System.out.println("MENU:");
            System.out.println("\t0 -> close app");
            System.out.println("\t1 -> add user");
            System.out.println("\t2 -> delete user");
            System.out.println("\t3 -> add friendship");
            System.out.println("\t4 -> delete friendship");
            System.out.println("\t5 -> print all users");
            System.out.println("\t6 -> print all friendships");
            System.out.println();

            System.out.print("Command: ");
            cmd = scanner.nextInt();

            if(cmd == 1){
                console_add_user();
            } else if (cmd == 2) {
                console_delete_user();
            } else if (cmd == 3) {
                console_add_friendship();
            } else if (cmd == 4) {
                console_delete_friendship();
            } else if (cmd == 5) {
                console_print_all_users();
            } else if (cmd == 6) {
                console_print_all_friendships();
            } else if (cmd == 0) {
                System.out.println("Closing app...");
                break;
            } else{
                System.out.println("WRONG COMMAND!\n Must be a number from the list above!");
            }
        }
    }

//    private void populate(){
//        srv.add_user("John", "Graves", "johnny_walks_on_graves@gmail.com");
//        srv.add_user("Maria", "Ioana", "maria_ioana@campiona.com");
//        srv.add_user("Johnny", "Test", "test_mail@gmail.com");
//        srv.add_user("Millie", "Bobbins", "bobbinaround@yahoo.com");
//        srv.add_user("Matei", "Bodnariu", "my_mail_here@yahoo.com");
//        srv.add_user("Who", "Doctor", "paranormal@phonebooth.com");
//
//        srv.add_friendship(1L, 3L);
//        srv.add_friendship(1L, 4L);
//        srv.add_friendship(2L, 6L);
//        srv.add_friendship(3L, 6L);
//    }
    private void console_print_all_users() {
        srv.get_all_users().forEach(System.out::println);
    }

    private void console_add_user() {
        Scanner user_scanner = new Scanner(System.in);
        System.out.print("First name: ");
        String firstname = user_scanner.nextLine();
        System.out.print("Last name: ");
        String lastname = user_scanner.nextLine();
        System.out.print("Email: ");
        String email = user_scanner.nextLine();
        System.out.print("Username: ");
        String username = user_scanner.nextLine();
        System.out.print("Password: ");
        String password = user_scanner.nextLine();
        try{
            srv.add_user(firstname, lastname, email,username, password);
        } catch (ValidationException | IllegalArgumentException exc){
            System.out.println(exc.getMessage());
        } finally {
            //System.out.println("ERROARE!");
        }

    }

    private void console_delete_user() {
        Scanner user_scanner = new Scanner(System.in);
        System.out.print("Id of the user to be deleted: ");
        Long id = user_scanner.nextLong();
        try{
            srv.delete_user(id);
        } catch (ValidationException | IllegalArgumentException exc){
            System.out.println(exc.getMessage());
        } finally {
            //System.out.println("ERROARE!");
        }
    }

    private void console_print_all_friendships() {
        srv.get_all_friendships().forEach(System.out::println);
    }

    private void console_add_friendship() {
        Scanner friendship_scanner = new Scanner(System.in);
        System.out.print("ID of first user: ");
        long uid1 = friendship_scanner.nextLong();
        System.out.print("ID of second user: ");
        long uid2 = friendship_scanner.nextLong();
        try{
            srv.add_friendship(uid1, uid2);
        } catch (ValidationException | IllegalArgumentException exc){
            System.out.println(exc.getMessage());
        } finally {
            //System.out.println("ERROARE!");
        }
    }

    private void console_delete_friendship() {
        Scanner friendship_scanner = new Scanner(System.in);
        System.out.print("ID of first user: ");
        long uid1 = friendship_scanner.nextLong();
        System.out.print("ID of second user: ");
        long uid2 = friendship_scanner.nextLong();
        try{
            srv.delete_friendship(uid1, uid2);
        } catch (ValidationException | IllegalArgumentException exc){
            System.out.println(exc.getMessage());
        } finally {
            //System.out.println("ERROARE!");
        }
    }
}
