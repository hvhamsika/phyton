word = "Funwith"
n = len(word)

for i in range(1, n+1):
    print(word[:i])

for i in range(n-1, 0, -1):
    print(word[:i])


n = len(word)


for i in range(1, n+1):
    print(" "*(n-i) + word[:i])

for i in range(n-1, 0, -1):
    print(" "*(n-i)+word[:i])

    
n = len(word)

for i in range(1, n+1):
    
    line = " ".join(word[:i])
    print(" "*(n-i) + line)
    

for i in range(n-1, 0, -1):
    line = " ".join(word[:i])
    print(" "*(n-i)+line)

