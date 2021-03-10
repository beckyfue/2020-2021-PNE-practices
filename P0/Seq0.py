from pathlib import Path

def seq_ping():
    print("OK")


def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())



def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    a, c, g, t, = 0, 0, 0, 0
    for d in seq:
        if d == "A":
            a += 1
        elif d == "C":
            c += 1
        elif d == "G":
            g += 1
        else:
            t += 1
    return {"A": a, "C": c, "G":g, "T": t}

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    printed = " "
    for letter in seq:
        if letter == "A":
            printed += "T"
        elif letter == "C":
            printed += "G"
        elif letter == "T":
            printed += "A"
        else:
            printed += "C"
    return printed

def most_frequent(seq):
    all_freq = {}
    for character in seq:
        if character in all_freq:
            all_freq[character] += 1
        else:
            all_freq[character] = 1
    return max(all_freq, key = all_freq.get)







