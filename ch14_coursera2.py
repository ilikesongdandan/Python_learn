import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('track.sqlite')
cur=conn.cursor()

cur.executescript('''
drop table if exists Artist;
drop table if exists Genre;
drop table if exists Album;
drop table if exists Track;
			
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname=raw_input('Enter a file name:')
if len(fname)<1:fname='Library.xml'

def lookup(d,key):
	found=False
	for child in d:
		if found :return child.text
		if child.tag=='key' and child.text==key:
			found=True
	return None


	# pass

stuff=ET.parse(fname)
all=stuff.findall('dict/dict/dict')
print 'Dict Count:',len(all)

for entry in all:
	if (lookup(entry,'Track ID') is None): continue

	SongName=lookup(entry, 'Name')
	ArtistName=lookup(entry, 'Artist')
	Genre=lookup(entry, 'Genre')
	Album=lookup(entry, 'Album')
	length=lookup(entry, 'Total Time')
	rating=lookup(entry, 'Rating')
	count=lookup(entry, 'Play Count')
	if SongName is None or ArtistName is None or Album is None or Genre is None:
		continue
	print SongName,ArtistName,Genre,Album,length,rating,count

	cur.execute('insert or ignore into Artist (name) values (?)',(ArtistName,))
	cur.execute('insert or ignore into Genre (name) values (?)',(Genre,))
	cur.execute('select id from Artist where name=?',(ArtistName,))
	artist_id=cur.fetchone()[0]

	cur.execute('insert or ignore into Album (title,artist_id) values (?,?)',(Album,artist_id,))
	cur.execute('select id from Album where title=?',(Album,))
	album_id=cur.fetchone()[0]

	cur.execute('select id from Genre where name=?',(Genre,))
	genre_id=cur.fetchone()[0]

	cur.execute('''insert or replace into Track 
		(title,album_id,genre_id,len,rating,count) values (?,?,?,?,?,?)''',
		(SongName,album_id,genre_id,length,rating,count))

	conn.commit()



