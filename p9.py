file=open("p2.py")
lines=file.readlines()
file.close()
for line in (lines):
    print(line[::-1])

    
