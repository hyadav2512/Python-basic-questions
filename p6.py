with open('p4.py', 'r') as reader:
    line = reader.readline()
    while line != '':
         print(line, end='')
         line = reader.readline()
