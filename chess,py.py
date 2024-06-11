'''chess'''
e_r="2468"
o_r="1357"

e_a="bdfh"
o_a="aceg"

s=input()

if s[0] in e_a:
    if s[1] in e_r:
        print("Black")
    else:
        print("White")
else:
    if s[1] in e_r:
        print("White")
    else:
        print("Black")