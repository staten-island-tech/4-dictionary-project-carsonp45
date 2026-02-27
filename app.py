def occupied(N,y,z):
    1 <= N <= 100
    found = 0
    for i in range(N):
        if y[i] == "C" and z[i] == "C":
            found += 1
    print(found)
occupied(5,"CCC..", "CCCCC")