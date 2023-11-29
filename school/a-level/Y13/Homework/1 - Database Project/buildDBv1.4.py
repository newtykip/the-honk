"""based on code at http://pythonschool.net/category/databases.html
check understanding of SQL, tuples and the format() method"""
import sqlite3

def createTable(sql, tableName, dbName):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name =?",(tableName,))
        result = cursor.fetchall()
        keepTable = True
        if len(result)== 1:
            response = input ("The table {0} already exists, do you wish to recreate it (y/n)? ".format(tableName))
            if response=="y":
                keepTable=False
                print("The table {0} will be recreated - all existing data will be lost".format(tableName))
                cursor.execute("drop table if exists {0}".format(tableName))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keepTable = False
        if not keepTable:
            cursor.execute(sql)
            db.commit()
    #end function

if __name__=="__main__":
    dbName = "histQuiz.db"
    tableName = "tblQuestion"
    sql = """create table {0}
            (QuestionID integer,
            Question text,
            Difficulty integer,
            primary key (QuestionID))""".format(tableName)
    createTable(sql,tableName,dbName)
    tableName = "tblAnswer"
    sql = """create table {0}
            (AnswerID integer,
            Answer text,
            QuestionID integer,
            primary key (AnswerID),
            foreign key (QuestionID) references tblQuestion(QuestionID))""".format(tableName)
    createTable(sql,tableName,dbName)
    tableName = "tblPlayer"
    sql = """create table {0}
            (PlayerID integer,
            Username text,
            Password text,
            primary key (PlayerID))""".format(tableName)
    createTable(sql,tableName,dbName)
    tableName = "tblGame"
    sql = """create table {0}
            (GameID integer,
            PlayerID text,
            DateTime text,
            Score integer,
            D1Question text,
            D2Question text,
            D3Question text,
            primary key (GameID),
            foreign key (PlayerID) references tblPlayer(PlayerID),
            foreign key (D1Question,D2Question,D3Question) references tblQuestion(QuestionID,QuestionID,QuestionID))""".format(tableName)
    createTable(sql,tableName,dbName)