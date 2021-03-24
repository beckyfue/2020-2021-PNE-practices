import termcolor


def is_valid_sequence(strbases):
    for c in strbases:
        if c!= "A" and c!= "C" and c!= "T" and c!= "G":
            return False
    return True


class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        if is_valid_sequence(strbases):
            print("New sequence created")
        else:
            self.strbases = "Error"
            print("INCORRECT Sequence detected")

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c!= "A" and c!= "C" and c!= "T" and c!= "G":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (Length: " +str(list_sequences[i].len()), ")" + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)



def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i+1)))
    return list_seq
