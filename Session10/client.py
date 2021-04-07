from P2 import Client0

c = Client0.Client("127.0.0.1", 8082)
for i in range(0, 5):
    c.talk("Message" + str(i))
