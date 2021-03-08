import termcolor


def is_valid_sequence(strbases):
    for c in strbases:
        if c!= "A" and c!= "C" and c!= "T" and c!= "G":
            return False
    return True


class Seq:
    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL seq created")
            self.strbases=strbases
        else:
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
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0
        else:
            return len(self.strbases)