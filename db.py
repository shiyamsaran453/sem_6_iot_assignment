import sqlite3
con=sqlite3.connect('ultrasonic_dist_db.db')
cur=con.cursor()
cur.execute(''' CREATE TABLE DISTANCE_DATA_BASE(DISTANCE FLOAT,STATUS VARCHAR(10))''')
con.commit()
print("table is created")
con.close()


