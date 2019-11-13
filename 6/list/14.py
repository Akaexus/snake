def replace(s, old, new):
    s = list(s)
    old = list(old)
    new = list(new)
    changed = True
    while changed:
        changed = False
        for i in range(0, len(s)):
            if s[i] == old[0]:
                correct = True
                for j in range(1, len(new)):
                    if s[i] != old[j]:
                        correct = False
                if correct:
                    s = s[0:i] + new + s[i+len(old):]
                    changed = True
    return ''.join(s)



print(replace('Mississippi', 'i', 'I'))