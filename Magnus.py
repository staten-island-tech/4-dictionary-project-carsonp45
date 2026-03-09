def magnus(word):
    count = 0
    state = 0

    for char in word:
        if state ==0 and char.upper() == "H":
            state = 1
        elif state ==1 and char.upper() == "O":
            state = 2
        elif state ==2 and char.upper() == "N":
            state = 3
        elif state ==3 and char.upper() == "I":
            state = 0
            count += 1
    print(count)
magnus("HONOASDOINAHINAOSDOAINHONDOGNHOINHIHONHIOSNHDIOSNHIOHWASINGNIHGNGHOANOIGABGGIENROIANFIGNGENRASIDONANWWIFUYCJASOAWNODIASHUHNUGEGANSMXHONOIHONIHNIHONHINOHNINOH")