#-*- coding: utf8 -*-
import db_config,sys

class a:

    con = 0
    def __init__(self,user):
        if user == "1":
            self.conn = db_config.createdb_mysql()
        elif user == "2":
            self.conn = db_config.createdb_sqlite()
        elif user == "3":
            self.conn = db_config.createdb_postgresql()

    def create(self):
        cur = self.conn.cursor()
        cur.execute("DROP TABLE IF EXISTS student")
        cur.execute("CREATE TABLE student(Id INT,Name VARCHAR(25),City TEXT,Age INT,Phone INT)")
        print "New table is created"
        self.conn.commit()

    def insert(self,*args):
        cur = self.conn.cursor()
        id = args[0]
        name = args[1]
        city = args[2]
        age = args[3]
        phone = args[4]
        query = """INSERT INTO student VALUES (%s , '%s' , '%s' , %s ,%s);"""%(id,name,city,age,phone)
        cur.execute(query)
        print "Values inserted"
        self.conn.commit()

    def select(self):
        cur = self.conn.cursor()
        query = """SELECT * FROM student"""
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) == 0:
            print "No records found"
        else:
            print rows
        self.conn.commit()
            
    def delete(self,*args):
        cur = self.conn.cursor()
        id = args[0]
        query = """DELETE FROM student WHERE Id = %s;"""%(id) 
        cur.execute(query)
        print "Record deleted"
        self.conn.commit()
            
    def update(self,*args):
        cur = self.conn.cursor()
        name = args[0]
        id = args[1]
        query = """UPDATE student SET Name = '%s' WHERE Id = %s; """%(name,id)
        cur.execute(query)
        print "Record updated successfully"
        self.conn.commit()
   
# Show databses nad tables
    def list_db(self):
        user = raw_input("Enter choice")
        cur = self.conn.cursor()
        if user == "1":
            print "1.See database \n 2.See table"
            choose = raw_input("Enter choice:")
            if choose == "1":
                cur.execute('SHOW DATABASES')
                rows = cur.fetchall()
                for row in rows:
                    print row 
            elif choose == "2":
                cur.execute('SHOW TABLES')
                rows = cur.fetchall()
                for row in rows:
                    print row    
        elif user == "2":
            cur.execute('PRAGMA database_list;')
            rows = cur.fetchall()
            for row in rows:
                print row[2]