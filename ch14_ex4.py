import sqlite3

conn=sqlite3.connect('test.sqlite')
cur=conn.cursor()

cur.execute('INSERT INTO test VALUES ("jianglik",12,19)')
cur.execute('INSERT INTO test VALUES ("wujiang",13,19)')


conn.commit()

cur.execute('select * from test where id=9')
row=cur.fetchall()
print row

cur.execute('select * from test where id=8')
row1=cur.fetchone()
print row1

print 'test'
cur.execute('SELECT name,Id,age FROM test')
for row in cur:
	print row
# cur.execute('DELETE FROM Tracks WHERE plays<100')
conn.commit()

cur.close()