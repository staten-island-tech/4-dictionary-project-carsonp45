def gambling(total, a, b, c):
    plays=0
    machine=0
    while total>0 and total<1000:
        plays +=1
        total -=1
        if machine == 0:
            a+=1
            if a == 35:
                total +=30
                a=0
                machine+=1
        if machine == 1:
            b+=1
            if b == 100:
                total +=60
                b=0
                machine +=1
        if machine ==2:
            c+=1
            if c==10:
                total+=9
                c==0
                machine -=2
        print(f"Martha plays, {plays}, times before going broke")
gambling(77, 5, 99, 3)
            