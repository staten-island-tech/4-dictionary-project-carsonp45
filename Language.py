""" Speech = "The red cat sat on the mat.Why are you so sad cat? Don't ask that."
language = None
def dialect(N,s,S,t,T):
    N(0<N<10,000)
    t = 0
    T = 0
    s = 0
    S = 0
    for i in range(N):
        if t:
            t + t+1
        if T:
            T = T+1
        if s:
            s = s+1
        if S:
            S = S+1
        if s and S > t and T:
            print("French")
        if t and T > s and S:
            print("English")
        if s and S == t and T:
            print("Probably French") """

def language(sentence):
    s= 0
    t= 0
    for i in sentence:
        if i == "s" or i == "S":
            s +=1
        elif i == "t" or i == "T":
            t+=1
    if s>= t:
        print("French")
    else:
        print("english")
    language("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")