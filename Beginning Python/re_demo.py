import re
email_pat1=re.compile(r'^[a-z.]+@[a-z.]+com$')
email_pat2=re.compile(r'^<[a-zA-Z\s]+>\s[a-z]+@[a-z.]+com$')

email1='someone@gmail.com'
email2='someone@gmail.org'
emall3='<Tom Paris> tom@voyager.com'


print re.match(email_pat1, email1)
print re.match(email_pat1, email2)
print re.match(email_pat2, emall3)

