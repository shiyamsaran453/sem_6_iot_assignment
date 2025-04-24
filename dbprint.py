
import sqlite3
import datetime
import pandas as pd
con=sqlite3.connect('ultrasonic_dist_db.db')
cursor=con.cursor()
query=cursor.execute('''select * from 'DISTANCE_DATA_BASE' ''')
COLS=[column[0] for column in query.description]
result=pd.DataFrame.from_records(data=query.fetchall(),columns=COLS)
print(result)
con.commit()
con.close()