from sympy import *

def get(lines):
    terms = []
    for i in lines:
        i = i.strip()
        i = i.replace("^", "**")
        if i[0] == 'x':
            i = '1*' + i
        if "x**" not in i:
            if not i.endswith("x"):
                i = i.replace('x','x**',1)
        for c in range(1, len(i)):
            if i[c] == 'x' and i[c-1].isdigit():
                i = i[:c] + '*' + i[c:]
                break
        terms.append(i)
    return terms

def calculate():
    exprsf = [sympify(s) for s in final]
    exprsd = [sympify(s) for s in divisor]
    f = sum(exprsf)
    d = sum(exprsd)
    q, r = div(f, d)
    out = str(q).replace("**", "^")
    if r != 0:
        out += " + " + str(r).replace("**", "^") + "/(" + str(d).replace("**", "^") + ")"
    with open("/workspaces/C/api/output.txt", "w") as f2:
        f2.write(out)

def main():
    
    global final
    global divisor
    with open("/workspaces/C/api/input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    split = lines.index("")
    final = get(lines[:split])
    divisor = get(lines[split+1:])
    calculate()

main()