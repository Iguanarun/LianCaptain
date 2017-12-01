f = open("a.txt") 
s = f.readlines()

f = open("b.txt","w")
f.write("asd")

f = open("b.txt","r")
s += f.readlines()
f.close
print(s)

