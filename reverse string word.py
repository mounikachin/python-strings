s='hi hello world goodmorning'
l=s.split()
rev=''
for word in l:
    rev+=' '+word[::-1]
print(rev.strip())

s='hi hello world goodmorning'
rev=''
l=s.split()
for word in l:
    rev=word+''+rev
print(rev.strip())


