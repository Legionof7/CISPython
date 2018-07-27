import sqlite3

def SQL():
    fmidList = [1234, 1235, 1236]
    marketList = ["Corn", "Cotton", "Hay"]
    profitList = [36, 45, 45]
    cur.execute('CREATE TABLE IF NOT EXISTS fmarket ( fmid INTEGER, \
             market TEXT, profit INT)')
    for i in range(len(fmidList)):
        cur.execute('INSERT INTO fmarket VALUES (?, ?, ?)',
                (fmidList[i], marketList[i], profitList[i]))
    con.commit()
    
SQL()

##########################
#Run
#
#[('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562)]
##########################  