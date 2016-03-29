import sqlite3
import re

conn=sqlite3.connect('emaildb1.sqlite')
cur=conn.cursor()

cur.execute('drop table if exists Counts')
cur.execute('create table Counts (org TEXT, count INTEGER)')

fname=raw_input('Enter a file name:')
if (len(fname)<1):
	fname='mbox.txt'
fhand=open(fname)
for line in fhand:
	line=line.strip()
	org=re.findall('^From .*@([^ ]+)', line)
	if(len(org)>0):
		# print org
		org=org[0]
		cur.execute('select count from Counts where org=?',(org,))
		row=cur.fetchone()
		if row is None:
			cur.execute('insert into Counts (org,count) values (?,1)',(org,))
		else :
			cur.execute('update Counts set count=count+1 where org=?',(org,))
	else:
		continue
conn.commit()
sqlstr='select org,count from Counts order by count desc limit 10'
for row in cur.execute(sqlstr):
	print str(row[0]),row[1]
cur.close()


	

