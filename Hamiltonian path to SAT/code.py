clauses = []
C = 1
mymap = {}
n = 0
def varnum(i, j):
    global n
    x =  i * n + j
    global C
    if not x in mymap:
        mymap[x] = C
        C += 1
    return x



n, m = map(int, input().split())

nodes = range(1, n + 1)

mymap = {}

for i in nodes:
    for j in nodes:
        if i != j:
            mymap[(i, j)] = 0

#each node j must appear in the path
for j in nodes:
    clauses.append([varnum(i, j) for i in nodes])

#no node j appears twice in the path
for i in nodes:
    for k in nodes:
        if i < k:
            for j in nodes:
                clauses.append([-varnum(i, j), -varnum(k, j)])


#every position i on the path must be occupied
for i in nodes:
    clauses.append([varnum(i, j) for j in nodes])


#no two nodes j and k occupy the same postion in the path
for j in nodes:
    for k in nodes:
        if j < k:
            for i in nodes:
                clauses.append([-varnum(i, j), -varnum(i, k)])



for _ in range(m):
    u, v = map(int, input().split())
    mymap[(u, v)] = 1
    mymap[(v, u)] = 1

for i in nodes:
    for j in nodes:
        if (i, j) in mymap:
            if mymap[(i, j)] == 0:
                for k in range(1, n):
                    clauses.append([-varnum(k, i), -varnum(k + 1, j)])

print (len(clauses), C - 1)
for x in clauses:
    for y in x:
        p = mymap[abs(y)]
        if y < 0:
            p *= -1
        print (p , end = " ")
    print (0)
