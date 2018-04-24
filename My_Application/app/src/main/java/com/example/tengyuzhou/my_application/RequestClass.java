package com.example.tengyuzhou.my_application;

public class RequestClass {
    String firstName;
    String lastName;
    String phone1;
    String phone2;

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public RequestClass(String firstName, String lastName, String phone1, String phone2) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone1 = phone1;
        this.phone2 = phone2;
    }

    public RequestClass() {
    }
}