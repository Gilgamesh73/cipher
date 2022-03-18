sen=input("input something to encrypt:")
senl=sen.lower()
key=input("input the key:")
key=key.lower()
alpha="abcdefghijklmnopqrstuvwxyza"
chars="+×÷=/_€£¥₩!@#$%^&*-?<>|\\0123456789 "
ciph=""
keymod=(len(sen)//len(key))*key+key[0:len(sen)%len(key)]
n=0
for i in senl:
    if i in chars:
        ciph+=i
        continue
    m=(alpha.index(i)+alpha.index(keymod[n]))
    if m>25:
        m=m%25-1
    ciph=ciph+alpha[m]
    n+=1
ciphmod=""
l=0
for i in ciph:
    if sen[l].isupper():
        ciphmod=ciphmod+i.upper()
    else:
        ciphmod=ciphmod+i
    l+=1
print(ciphmod)
