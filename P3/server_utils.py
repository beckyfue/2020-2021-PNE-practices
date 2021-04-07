def print_colours(message, colour):
    import termcolor
    print(termcolor.colored((message, colour)))

def format_command(command):
    return command.replace("\n", "").replace("\r", " ")

def ping():
    print_colours("PING command!", "green")
