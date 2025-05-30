import sqlite3
from debt import CreditCard

def initiateDB():
    with sqlite3.connect("debt_tracker.db") as con:
        cur = con.cursor()
        if cur.execute("SELECT name FROM sqlite_master").fetchone() is None:
            cur.executescript("""
                    BEGIN;
                    CREATE TABLE creditcard(name CHAR(20),balance FLOAT,apr FLOAT,due_date INTEGER(2));
                    CREATE TABLE loan(name CHAR(20),balance FLOAT,apr FLOAT,due_date INTEGER(2),min_payment FLOAT);
                    COMMIT;
                      """)
    
def save_debts(debt):
    if debt is None:
        return
    

    con = sqlite3.connect("debt_tracker.db")
    cur = con.cursor()
    
    match debt[0]:
        case "CREDIT":
            name,balance,apr,due_date = debt[1:]
            print(name,balance,apr,due_date)
            cur.execute("INSERT INTO creditcard (name, balance, apr, due_date) VALUES (?,?,?,?);",(str(name),float(balance),float(apr),int(due_date)))
        case "LOAN":
            pass

    con.commit()
    con.close()

chase = CreditCard("chase",200,28,23)

save_debts(chase.storage_helper())