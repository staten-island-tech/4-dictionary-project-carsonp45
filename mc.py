def Answer(A,B,C):
    correct = 0
    for i in range(A):
        if B[i] == "B":
            correct += 1
    print(correct)
Answer(13, "ABCBABCBABCCABA", "ABCCBABCABABCB")