import time
import MySQLdb as mdb
import datetime

global count1,count2,ts
ts = 0
count1=count2=1

global db1_alt,db2_alt,db3_alt,db4_alt
db1_alt=db2_alt=db3_alt=db4_alt = 0


con = mdb.connect('localhost', 'chetankj', 'chetankj123', 'AttendanceSystem');

################ First Year DB #################

def first_year_db():
    with con:
        
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS first_year_db")

        firstdb = """CREATE TABLE first_year_db(Id INT ,fs_position INT, full_name2 CHAR(20), semester CHAR(20),usn CHAR(20))"""

        cur.execute(firstdb)


def update_firstyear_db(s_id_loc, s_name, sem,us):
    s_id_loc = int(s_id_loc)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM first_year_db")
        
        cur.execute ("INSERT into first_year_db (Id,fs_position, full_name2, semester,usn) values('%s','%s',%s,%s,%s)",(s_id_loc,s_id_loc, s_name, sem,us))
                
        con.commit()
        print 'first year-',s_id_loc,s_id_loc, s_name, sem,us
        

def delete_firstyear_db(s_position):
    s_position = int(s_position)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM first_year_db")
        cur.execute("delete from first_year_db where fs_position='%s'",(s_position,))
        con.commit()
        print 'deleted'

def alter_firstyear_db():
    global count1,count2,ts
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
    ts = timestamp
    ts = str(ts)
    print ts
    with con:
        cur = con.cursor()
        cur.execute("ALTER TABLE first_year_db ADD %s CHAR(50)"%(ts))
        cur.execute("UPDATE first_year_db SET %s = 'A'"%(ts))
        con.commit()


############# Second Year DB  ################

def second_year_db():
    with con:
        
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS second_year_db")

        seconddb = """CREATE TABLE second_year_db(Id INT ,fs_position INT, full_name2 CHAR(20), semester CHAR(20),usn CHAR(20))"""

        cur.execute(seconddb)


def update_secondyear_db(s_id_loc, s_name, sem,us):
    s_id_loc = int(s_id_loc)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM second_year_db")
        
        cur.execute ("INSERT into second_year_db (Id,fs_position, full_name2, semester,usn) values('%s','%s',%s,%s,%s)",(s_id_loc,s_id_loc, s_name, sem,us))
                
        con.commit()
        print 'second year-',s_id_loc,s_id_loc, s_name, sem,us
        

def delete_secondyear_db(s_position):
    s_position = int(s_position)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM second_year_db")
        cur.execute("delete from second_year_db where fs_position='%s'",(s_position,))
        con.commit()
        print 'deleted'

def alter_secondyear_db():
    global ts
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
    ts = timestamp
    ts = str(ts)
    print ts
    with con:
        cur = con.cursor()
        cur.execute("ALTER TABLE second_year_db ADD %s CHAR(50)"%(ts))
        cur.execute("UPDATE second_year_db SET %s = 'A'"%(ts))
        con.commit()


############# Third Year DB  ################

def third_year_db():
    with con:
        
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS third_year_db")

        thirddb = """CREATE TABLE third_year_db(Id INT ,fs_position INT, full_name2 CHAR(20), semester CHAR(20),usn CHAR(20))"""

        cur.execute(thirddb)


def update_thirdyear_db(s_id_loc, s_name, sem,us):
    s_id_loc = int(s_id_loc)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM third_year_db")
        
        cur.execute ("INSERT into third_year_db (Id,fs_position, full_name2, semester,usn) values('%s','%s',%s,%s,%s)",(s_id_loc,s_id_loc, s_name, sem,us))
                
        con.commit()
        print 'Third year-',s_id_loc,s_id_loc, s_name, sem,us
        

def delete_thirdyear_db(s_position):
    s_position = int(s_position)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM third_year_db")
        cur.execute("delete from third_year_db where fs_position='%s'",(s_position,))
        con.commit()
        print 'deleted'

def alter_thirdyear_db():
    global ts
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
    ts = timestamp
    ts = str(ts)
    print ts
    with con:
        cur = con.cursor()
        cur.execute("ALTER TABLE third_year_db ADD %s CHAR(50)"%(ts))
        cur.execute("UPDATE third_year_db SET %s = 'A'"%(ts))
        con.commit()

############# Fourth Year DB  ################

def fourth_year_db():
    with con:
        
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS fourth_year_db")

        fourthdb = """CREATE TABLE fourth_year_db(Id INT ,fs_position INT, full_name2 CHAR(20), semester CHAR(20),usn CHAR(20))"""

        cur.execute(fourthdb)


def update_fourthyear_db(s_id_loc, s_name, sem,us):
    s_id_loc = int(s_id_loc)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM fourth_year_db")
        
        cur.execute ("INSERT into fourth_year_db (Id,fs_position, full_name2, semester,usn) values('%s','%s',%s,%s,%s)",(s_id_loc,s_id_loc, s_name, sem,us))
                
        con.commit()
        print 'Fourth year-',s_id_loc,s_id_loc, s_name, sem,us
        

def delete_fourthyear_db(s_position):
    s_position = int(s_position)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM fourth_year_db")
        cur.execute("delete from fourth_year_db where fs_position='%s'",(s_position,))
        con.commit()
        print 'deleted'

def alter_fourthyear_db():
    global ts
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
    ts = timestamp
    ts = str(ts)
    print ts
    with con:
        cur = con.cursor()
        cur.execute("ALTER TABLE fourth_year_db ADD %s CHAR(50)"%(ts))
        cur.execute("UPDATE fourth_year_db SET %s = 'A'"%(ts))
        con.commit()

############# Faculty DB  ################

def faculty_db():
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS lecturer_db")
        facultydb = """CREATE TABLE lecturer_db(Id INT ,fl_position INT, full_name1 CHAR(20))"""
        cur.execute(facultydb)


def update_faculty_db(f_id_loc, f_name):
    global count1,count2
    f_id_loc = int(f_id_loc)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM lecturer_db")
        cur.execute ("INSERT into lecturer_db (Id,fl_position, full_name1) values('%s','%s',%s)",(f_id_loc,f_id_loc, f_name))
        con.commit()
        print 'Faculty-',f_id_loc, f_name

def delete_faculty_db(f_position):
    f_position = int(f_position)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM lecturer_db")
        cur.execute("delete from lecturer_db where fl_position='%s'",(f_position,))
        con.commit()
        print 'deleted'


###############################################################################

def get_attendance(case,y_d,data):
    case = int(case)

    def get_first_year(inf1):
        global ts
        inf1 = int(inf1)
        mark = 'P'
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM first_year_db")
            for i in range(cur.rowcount):
                fst_yr_dd = cur.fetchone()
                s_f_p = int(fst_yr_dd[0])

                if s_f_p == inf1:
                    cur = con.cursor()
                    cur.execute ("""UPDATE first_year_db SET %s='P' WHERE Id='%s'"""%(ts,inf1))
                    return (str(s_f_p),str(s_f_p),fst_yr_dd[2],fst_yr_dd[3],fst_yr_dd[4])

            if s_f_p != inf1:
                m='no_db'
                return(m,' ',' ',' ',' ')

    def get_second_year(inf1):
        global ts
        inf1 = int(inf1)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM second_year_db")
            for i in range(cur.rowcount):
                fst_yr_dd = cur.fetchone()
                s_f_p = int(fst_yr_dd[0])

                if s_f_p == inf1:
                    print ts
                    cur = con.cursor()
                    cur.execute ("""UPDATE second_year_db SET %s='P' WHERE Id='%s'"""%(ts,s_f_p))
                    return (str(s_f_p),str(s_f_p),fst_yr_dd[2],fst_yr_dd[3],fst_yr_dd[4])

            if s_f_p != inf1:
                m='no_db'
                return(m,' ',' ',' ',' ')
        

    def get_third_year(inf1):
        global ts
        inf1 = int(inf1)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM third_year_db")
            for i in range(cur.rowcount):
                fst_yr_dd = cur.fetchone()
                s_f_p = int(fst_yr_dd[0])

                if s_f_p == inf1:
                    cur = con.cursor()
                    cur.execute ("""UPDATE third_year_db SET %s='P' WHERE Id='%s'"""%(ts,inf1))
                    return (str(s_f_p),str(s_f_p),fst_yr_dd[2],fst_yr_dd[3],fst_yr_dd[4])

            if s_f_p != inf1:
                m='no_db'
                return(m,' ',' ',' ',' ')

    def get_fourth_year(inf1):
        global ts
        inf1 = int(inf1)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM fourth_year_db")
            for i in range(cur.rowcount):
                fst_yr_dd = cur.fetchone()
                s_f_p = int(fst_yr_dd[0])

                if s_f_p == inf1:
                    cur = con.cursor()
                    cur.execute ("""UPDATE fourth_year_db SET %s='P' WHERE Id='%s'"""%(ts,inf1))
                    return (str(s_f_p),str(s_f_p),fst_yr_dd[2],fst_yr_dd[3],fst_yr_dd[4])

            if s_f_p != inf1:
                m='no_db'
                return(m,' ',' ',' ',' ')
    
    def student_db_get(inf1,y_d):
        global db1_alt,db2_alt,db3_alt,db4_alt
        inf1 = int(inf1)

        if '1' in y_d:
            if db1_alt == 0:
                alter_firstyear_db()
                print 'table altered'
                db1_alt=1
            msg1,msg2,msg3,msg4,msg5 = get_first_year(inf1)
            return(msg1,msg2,msg3,msg4,msg5)

        elif '2' in y_d:
            global db1_alt,db2_alt,db3_alt,db4_alt
            if db2_alt == 0:
                alter_secondyear_db()
                print 'table altered'
                db2_alt=1
            msg1,msg2,msg3,msg4,msg5 = get_second_year(inf1)
            return(msg1,msg2,msg3,msg4,msg5)

        elif '3' in y_d:
            global db1_alt,db2_alt,db3_alt,db4_alt
            if db3_alt == 0:
                alter_thirdyear_db()
                print 'table altered'
                db3_alt=1
            msg1,msg2,msg3,msg4,msg5 = get_third_year(inf1)
            return(msg1,msg2,msg3,msg4,msg5)

        elif '4' in y_d:
            global db1_alt,db2_alt,db3_alt,db4_alt
            if db4_alt == 0:
                alter_fourthyear_db()
                print 'table altered'
                db4_alt=1
            msg1,msg2,msg3,msg4,msg5 = get_fourth_year(inf1)
            return(msg1,msg2,msg3,msg4,msg5)

    def faculty_db_get(inf2):
        global ts
        inf2 = int(inf2)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM lecturer_db")
            for i in range(cur.rowcount):
                f_id,f_f_p,f_name = cur.fetchone()
                print f_id,f_f_p,f_name

                if f_f_p==inf2:
                    return(str(f_id),str(f_f_p),f_name,' ',' ')

                else:
                    m='no_db'
                    return(m,' ',' ',' ',' ')

    if case==0:
        print 'i am here'
        msg1,msg2,msg3,msg4,msg5=faculty_db_get(data)
        return(msg1,msg2,msg3,msg4,msg5)

    elif case==1:
        msg1,msg2,msg3,msg4,msg5=student_db_get(data,y_d)
        return(msg1,msg2,msg3,msg4,msg5)
    

def create_reset_db():
    first_year_db()
    second_year_db()
    third_year_db()
    fourth_year_db()
    faculty_db()

#create_reset_db()
#alter_firstyear_db()

'''
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM first_year_db")
    for i in range(cur.rowcount):
        f_all_data = cur.fetchone()
        print int(f_all_data[0])
        print f_all_data[2]
        print 'hi'
'''
