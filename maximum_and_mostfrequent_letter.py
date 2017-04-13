import multiprocessing.dummy
import re
import collections

p = multiprocessing.dummy.Pool(6)

x = """adksfjdhglrtawjdfkslj
dfsdsgafgdgwwwdvs
jfsdjkughsdksjhfkljdh
fkjsdkfjwlghblkdjhsdf
jksdfhkjfkldjfhl
akjhalkjswfwrwfwggfsgf
lkdfjgoksdjsfhskjdf
jkdkbvsfwffjwwiueiw
ldkflnornnfowanejb
apajgjegrjrgfgfasgas
sdfdfgfdgfdgdfgsg
sdfdfsdf
sgghgfhddhdhdhfjarwffgd
ddhggehefhdfhdh
dgdhedfsfgdhdhgh
dhsgsfeshtdfdbhsghsdhsdhg
dfgdfgeefdgfdhdghdsh
dhdhshsergefhghsfh"""

x = x.split('\n')

def mapper(s):  # string -> [(key value)]
    pairs = []
    for c in s:
        pairs.append((c, 1))
    return pairs

def combiner(pairs):
    index = {}
    for (key, value) in pairs:
        if not index.has_key(key):
            index[key] = value
        else:
            index[key] = index[key] + value
    pairs = []
    for key in index:
        pairs.append((key, index[key]))
    return pairs

def reducer(data):
    index = {}
    for pairs in data:
        for (key, value) in pairs:
            if not index.has_key(key):
                index[key] = value
            else:
                index[key] = index[key] + value
    pairs = []
    for key in index:
        pairs.append((key, index[key]))
    return pairs


def mapper2(s2):
    pairs2 = []
    for c2 in s2:
        pairs2.append((c2, ord(c2)))
    return pairs2

def combiner2(pairs2):
    v2 = 0
    for (key2, value2) in pairs2:
        if v2 < value2:
            v2 = value2

    pairs2 = []
    pairs2.append((chr(v2), v2))
    return pairs2

def reducer2(pairs2):
    v2 = 0
    for var in pairs2:
        for (key2, value2) in var:
            if v2 < value2:
                v2 = value2

    pairs3 = []
    pairs3.append((chr(v2), v2))
    return pairs3

data2 = p.map(mapper2, x)
data21 = p.map(combiner2,data2)
data21 = reducer2(data21)
print('The maximum letter(closest to z) in the text:')
print(data21)

data = p.map(mapper, x)
data = p.map(combiner, data)
data = reducer(data)
var1 = max(data, key=lambda x: x[1])
print('Most frequent letter in the text is :')
print(var1)






