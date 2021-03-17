from P2.Client0 import Client
from pathlib import Path
from P1.Seq1 import Seq
PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)
s = Seq()
s.read_fasta('../P2/FRAT1.txt')
count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i+10]
    count +=1
    i += 10
    print(c.talk(fragment))
