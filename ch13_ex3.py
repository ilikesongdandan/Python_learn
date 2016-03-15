import json
input_='''
[
	{"id":"001",
   	"x":"2",
   	"name":"chuck"
	},
	{	"id":"009",
	"x":"7",
	"name":"Brent"
}
]'''
info=json.loads(input_)
print 'User count:',len(info)
for item in info:
	print 'Name:',item['name']
	print 'id:',item['id']
	print 'attribute:',item['x']