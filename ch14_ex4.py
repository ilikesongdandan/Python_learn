import sqlite3

conn=sqlite3.connect('test.sqlite')
cur=conn.cursor()


conn.commit()

print 'test'
cur.execute('SELECT name,Id,age FROM test')
for row in cur:
	print row
# cur.execute('DELETE FROM Tracks WHERE plays<100')
conn.commit()

cur.close()