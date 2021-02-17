def correct_sequence(dna):
    for i in dna:
        if i!= "A" and i!= "C" and i!= "G" and i!= "T":
            return False
    return True
def count_dna(dna):
    a, c, g, t =0, 0, 0, 0
    for i in dna:
        if i=="C":
            c+=1
        elif i=="G":
            g+=1
        elif i=="A":
            a+=1
        else:
            t+=1
    return c, g, t, a


our_dna=input("What is you DNA sequence")
if correct_sequence(our_dna):
    print("Total length", len(our_dna))
    c, g, t, a = count_dna(our_dna)
    print("A:", a)
    print("G:", g)
    print("C:", c)
    print("T:", t)
else:
    print("Incorrect program")
