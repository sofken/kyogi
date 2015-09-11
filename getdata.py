f = open('sample.txt','r')
tmpdata = []
data = []
i = 0

for line in f:
	if(len(line)==2):
		data.append(tmpdata)
		tmpdata = []
	elif(len(line)!=4):
		line = line.rstrip('\r\n')
		tmpdata.append(line)

for line2 in data:
	print(line2)
