import pymysql as p

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='ins')

def addData(t):
    con=getConnection()
    cur=con.cursor()
    query1="insert into ins_s (name,password,Age,MobileNumber,email) values (%s,%s,%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close()

def addData2(t):
    con=getConnection()
    cur=con.cursor()
    query2="insert into ins_plan (name,Age,choosefor,coverage) values (%s,%s,%s,%s)"
    cur.execute(query2,t)
    con.commit()
    con.close()

def fetchData():
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from ins_s")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def fetchData2():
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from ins_plan")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def specificdata(id):
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from ins_s where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]

def updatedata(t):
    con=getConnection()                  
    cur=con.cursor()
    query="update ins_s set name=%s,password=%s,Age=%s,MobileNumber=%s,email=%s where id=%s"
    cur.execute(query,t)
    con.commit()
    con.close()


def deletedata(id):
    con=getConnection()                  
    cur=con.cursor()
    query="delete from ins_s where id=%s"
    cur.execute(query,(id,))
    con.commit()
    con.close()