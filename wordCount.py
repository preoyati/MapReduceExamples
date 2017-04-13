import multiprocessing.dummy
import re
p = multiprocessing.dummy.Pool(6)
f = open("alice.txt",'r')
s = f.read()
x = re.sub('[^A-Za-z0-9\n ]','',s)
x = re.sub('\n+','\n',x)
x = re.sub(' +',' ',x)
x = re.sub('\n +','\n',x)
x = re.sub('\n+','\n',x).lower()

x=x.split('\n')

def words (line):
    return line.split(" ")

x = p.map(words,x)

def mapper(s): # string -> [(key value)]
	pairs = []
	for c in s:
		pairs.append((c,1))
	return pairs

def combiner(pairs):
	index = {}
	for (key,value) in pairs:
		if not index.has_key(key):
			index[key] = value
		else:
			index[key] = index[key] + value
	pairs = []
	for key in index:
		pairs.append((key,index[key]))
	return pairs

def reducer(data):
	index = {}
	for pairs in data:
		for (key,value) in pairs:
			if not index.has_key(key):
				index[key] = value
			else:
				index[key] = index[key] + value
	pairs = []
	for key in index:
		pairs.append((key,index[key]))
	return pairs

data = p.map(mapper , x)
data = p.map(combiner,data)
data = reducer(data)
print(data)

dict = {}

for (key,value) in data:
     dict[key]= value

var1 = sorted(dict.iteritems(), key=lambda  x:x[1],reverse=True)

l=0
print("Five Most Counted words printed below:")
for val in var1:
    print(var1[l])
    l = l+1
    if l>4:
        break

ff = open("output.txt",'w')
for key in dict.keys():
    ff.write(str((key,dict[key])))
    ff.write('\n')
