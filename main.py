#-*- coding: utf8 -*-
import sys,db_queries

def insert():
    id = raw_input("ENter id:")
    name = raw_input("Enter name:")
    city = raw_input("Enter city")
    age = raw_input("Enter age:")
    phone = raw_input("Enter phone")
    obj.insert(id,name,city,age,phone)

def update():
    
    name = raw_input("Enter new name you want to keep:")
    id = raw_input("Enter the id you want to change the name of it:")
    obj.update(name,id)

def delete():
    id = raw_input("Enter id you want to delete:")
    obj.delete(id)
    
def opr():
    print "1.Insert \n2.Select \n3.Update \n4.Delete \n5.Show databases"
    ask = raw_input("Which operations you want to perform?")
    if ask == "1":
        insert()
        opr()
    elif ask == "2":
        obj.select()
        opr()
    elif ask == "4":
        delete()
        opr()
    elif ask == "3":
        update()
        opr()   
    elif ask == "5":
        print "1.mysql \n2.Sqlite \n3.Postgresql"
        user = raw_input("Which database you want to access?")
        obj = db_queries.a(user)
        obj.list_db()
        opr()

def choice():
    print "1.Mysql \n2.Sqlite \n3.Postgresql \n4.Quit"
    user = raw_input("Which database you want to access?")
    if user == "4":
        exit()
    elif user:
        global obj
        obj = db_queries.a(user)
        obj.create()
        opr()    


choice()