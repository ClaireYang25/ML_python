n = input()
m = []
p = []

if (n[0].islower() == False):
    n_0 = n[0].lower()
    #  n_lower = n[i].lower()
    p.append(n_0)

else:
    p.append(n[0])

for i in range(1, len(n)):

    if (n[i].islower()):
        m.append(n[i])

    else:
        #  if (n[0].islower() == False):
        #   #  n_0 = n[0].lower()
        #    n_lower = n[i].lower()
        #    m.append(n_lower)

        #  else:
        n_lower = n[i].lower()
        m.append("_" + n_lower)

# for i_ in m:
#     if i_=='_':
#       m.remove(i_)

# print(p+m)
q = p + m

# for char in q:
#     print(char)

z = "".join(q)

print(z)

