import random
s=["A","B"]
f = "Once T go to these sites: "
for i in range(0,15):
    f+=random.choice(s)+" "
print(f)
