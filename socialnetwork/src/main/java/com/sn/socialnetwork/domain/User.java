package com.sn.socialnetwork.domain;

public class User extends Entity<Long>{
    private String firstname;
    private String lastname;
    private String email;
    //private static AtomicLong ID_GENERATOR = new AtomicLong(1);
    private String username;
    private String password;

    public User(Long uid, String firstname, String lastname, String email, String username, String password) {
        super(uid);
        this.firstname = firstname;
        this.lastname = lastname;
        this.email = email;
        this.username = username;
        this.password = password;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Utilizator cu id "+ this.getId() +": - nume: " + firstname + " "
                + lastname + " - email: " + email + " - username: " + username;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(!(obj instanceof User)) return false;
        User o = (User) obj;
//        return getId().equals(o.getId());
        return this.firstname.equals(o.getFirstname()) &&
                this.lastname.equals(o.getLastname()) &&
                this.email.equals(o.getEmail());
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
