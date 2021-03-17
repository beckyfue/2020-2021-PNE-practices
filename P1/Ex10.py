from P1.Seq1 import Seq


GENE_FOLDER = "./PROJECT/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Practice 1, Exercise 10 |------")
for gene in gene_list:
    sequence = Seq()
    sequence.read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene, "Most frequent Base: ", sequence.frequent_base())