# f=open(r'd:/a.txt')
# print f.read()

# a=f.read(7)
# print a
# for i in range(3):
# 	print (str(i)+':'+f.readline())
# print f.readlines()

# f=open(r'd:/a.txt','w')
# f.write('this\nis no\nhaiku')
# f.close()

# f=open(r'd:/a.txt')
# lines=f.readlines()
# f.close()
# lines[1]="isn't a\n"
# f=open(r'd:/a.txt','w')
# f.writelines(lines)
# f.close()

def process(string):
	print "Processing:",string

f=open(r'd:/a.txt')
while True:
	line=f.readline()
	if not line:break
	process(line)
f.close()

f=open(r'd:/a.txt')
while True:
	char=f.read(1)
	if not char:break
	process(char)
f.close()