from command import mcmc
def readFreePar(FreeParCSV):
	l=[]
	infile = open(FreeParCSV,'r')
	free=mcmc.Scan()
	for line in infile:
		data=line.split(',')
		for i in data:
			i=eval(i)
			l.append(i)
		name = l[0]
		block=l[1]
		PDG=l[2]
		MIN=float(l[3])
		MAX=float(l[4]) 
		free.add(name,block,PDG,MIN,MAX)
		print(l)
		l=[]
	return free
