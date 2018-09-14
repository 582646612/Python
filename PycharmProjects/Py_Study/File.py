f = open(r'E:\Jmeter\fee.txt','r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line.split(',')[0])
