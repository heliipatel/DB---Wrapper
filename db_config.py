#-*- coding: utf8 -*-
import MySQLdb,sqlite3,psycopg2

# Mysql database
def createdb_mysql():
    con = MySQLdb.connect("localhost","testuser","test623","mysqldb" )
    cursor = con.cursor()
    print "Connected with mysql database"
    return con

# Sqlite database    
def createdb_sqlite():
    con = None
    try:
        con = sqlite3.connect('sqlite.db')
        cursor = con.cursor()
        print("Connected with sqlite database")
        return con
    except sqlite3.Error as e:
        print(e)
 
# Postgresql database    
def createdb_postgresql():

    try:         
        con = psycopg2.connect(database='postgredb', user='heli') 
        cursor = con.cursor()
        print "Connected with postgresql database"  
        return con 
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
       