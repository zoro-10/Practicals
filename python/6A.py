f=open('dummy.txt','w+')
f.write("Hello Everyone")
f.seek(0)
t=f.read()
print(t)
f.close()