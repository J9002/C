from sympy import *
def get(text):
    print(text)
    x = int(input())
    terms = []
    while x != 0:
        i = input()
        if i[0] == 'x':
            i = ('1*' + i) if i[:1] == 'x' else i
        if not i.endswith("x"):
            i = i.replace('x','x**',1)
        for c in range(1, len(i)):
            if i[c] == 'x' and i[c-1].isdigit():
                i = i[:c] + '*' + i[c:]
                break
        terms.append(i)
        x -= 1
    return terms

def calculate():
    exprsf = [sympify(s) for s in final]
    exprsd = [sympify(s) for s in divisor]
    f = sum(exprsf)
    d = sum(exprsd)
    q, r = div(f, d)
    print(f"\nResult:\n{str(q).replace("**", "^")}")

def main():
    global final 
    global divisor
    final = get("Final terms")
    divisor = get("Divisor terms")
    print(f"{final}\n{divisor}")
    calculate()

main()