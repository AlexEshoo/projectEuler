with open("resources/p079_keylog.txt", 'r') as f:
    logins = f.read().strip().split('\n')

unique = set()
for l in logins:
    for c in l:
        unique.update(c)

unique_digits = sorted(list(unique))

predecessors = dict([(n, set()) for n in unique_digits])
successors = dict([(n, set()) for n in unique_digits])

for l in logins:
    predecessors[l[1]].update([l[0]])
    predecessors[l[2]].update(l[:2])
    successors[l[0]].update(l[1:])
    successors[l[1]].update([l[2]])

pass_code = [None] * len(unique_digits)

for d in predecessors:
    index = len(predecessors[d])
    pass_code[index] = d

print("".join(pass_code))
