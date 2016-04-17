import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python?')
print md5.hexdigest()

md6=hashlib.md5()
md6.update('how to use md5')
md6.update('in python?')
print md6.hexdigest()
