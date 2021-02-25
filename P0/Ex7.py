import Seq0

ID = "U5.txt"

FOLDER = "./sequences/"
ID = "U5.txt"
U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)

print("-----| Exercise 7 |------")
print("Gene U5: ")
appropiate_sequence = U5_Seq[0:20]
print("Frag:", appropiate_sequence)
print("Comp:", Seq0.seq_complement(appropiate_sequence))