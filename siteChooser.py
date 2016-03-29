import random
s=["A","B"]
f = []
for i in range(0,15):
    f+=random.choice(s)
print(f)
for ss in f:
    print(ss)
    input(":")
