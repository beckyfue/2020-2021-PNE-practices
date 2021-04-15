import Seq1 as Seq

def print_colored(message, color):
    import termcolor
    import colorama

    colorama.init(strip="False")
    print("To server: ", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command", "green")
    response = "OK!"
    cs.send(str(response).encode())
    print(response)

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(str(response).encode())

def info(cs, argument):
    print_colored("INFO", "yellow")
    sequence = Seq.Seq(argument)
    response = "Sequence: " + str(sequence) + "\nTotal length: " + str(sequence.len())
    sol_a = "\nA: " + str(sequence.count_bases()[0]) + " (" + str(sequence.percentage()[0]) + "%)\n"
    sol_c = "C: " + str(sequence.count_bases()[1]) + " (" + str(sequence.percentage()[1]) + "%)\n"
    sol_g = "G: " + str(sequence.count_bases()[2]) + " (" + str(sequence.percentage()[2]) + "%)\n"
    sol_t = "T: " + str(sequence.count_bases()[3]) + " (" + str(sequence.percentage()[3]) + "%)\n"
    answer = response + sol_a + sol_c + sol_g + sol_t
    print(answer)
    cs.send(str(answer).encode())

def comp(cs, argument):
    print_colored("COMP", "yellow")
    sequence = Seq.Seq(argument)
    response = sequence.complement()
    print(response)
    cs.send(str(response).encode())

def rev(cs, argument):
    print_colored("REV", "yellow")
    sequence = Seq.Seq(argument)
    response = sequence.reverse()
    print(response)
    cs.send(str(response).encode())

def gene(cs, argument):
    print_colored("GENE", "yellow")
    sequence = Seq.Seq()
    sequence.read_fasta(argument)
    print(sequence)
    cs.send(str(sequence).encode())
