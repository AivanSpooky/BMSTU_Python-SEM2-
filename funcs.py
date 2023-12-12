# Функции

# Функция для вычисления математических операций (+ и -)
def mathoperations(l):
    if len(l) <= 1:
        return
    dig = ""
    sp = []
    op = []
    for i in range(len(l)):
        if l[i].isdigit() or l[i] == "." or i == 0:
            dig += l[i]
        else:
            op.append(l[i])
            sp.append(dig)
            dig = ""
    sp.append(dig)
    for i in op:
        #print(sp, op)
        if i == "+":
            sp = [sum(sp[0], sp[1])] + sp[2:]
        elif i == "-":
            sp = [diff(sp[0], sp[1])] + sp[2:]
    return sp[0]

# +
def sum(a, b):
    minus = False
    if float(a) < 0 and float(b) < 0:
        minus = True
    elif float(a) < 0 and float(b) >= 0:
        return diff(b, str(abs(float(a))))
    
    a = a.split(".")
    b = b.split(".")
    s = ""
    if len(a) == 1:
        a.append("0")
    if len(b) == 1:
        b.append("0")
    if len(a[0]) > len(b[0]):
        b[0] = "0" * (len(a[0]) - len(b[0])) + b[0]
    elif len(b[0]) > len(a[0]):
        a[0] = "0" * (len(b[0]) - len(a[0])) + a[0]
    if len(a[1])>len(b[1]):
        b[1] = b[1] + "0"*(len(a[1])-len(b[1]))
    elif len(b[1])>len(a[1]):
        a[1] = a[1] + "0"*(len(b[1])-len(a[1]))
    a[0] = a[0][::-1]
    a[1] = a[1][::-1]
    b[0] = b[0][::-1]
    b[1] = b[1][::-1]
    add = 0
    for i in range(len(b[-1])):
        s += str((int(a[-1][i]) + int(b[-1][i]) + add)%8)
        if (int(a[-1][i]) + int(b[-1][i]) + add) >= 8:
            add = (int(a[-1][i]) + int(b[-1][i]) + add) // 8
        else:
            add = 0
    s += "."

    for i in range(len(b[0])):
        s += str((int(a[0][i]) + int(b[0][i]) + add)%8)
        if (int(a[0][i]) + int(b[0][i]) + add) >= 8:
            add = (int(a[0][i]) + int(b[0][i]) + add) // 8
        else:
            add = 0
    if add != 0:
        s += str(add)
    if minus:
        s += "-"
    return s[::-1].rstrip("0").strip(".")

# -
def diff(a, b):
    if float(a) < 0 and float(b) < 0:
        return sum(str(abs(float(b))), a)
    s = ""
    minus = False
    if float(a) < float(b):
        minus = True
        a, b = b, a
    a = a.split(".")
    b = b.split(".")
    if len(a) == 1:
        a.append("0")
    if len(b) == 1:
        b.append("0")
    if len(a[0]) > len(b[0]):
        b[0] = "0" * (len(a[0]) - len(b[0])) + b[0]
    elif len(b[0]) > len(a[0]):
        a[0] = "0" * (len(b[0]) - len(a[0])) + a[0]
    if len(a[1])>len(b[1]):
        b[1] = b[1] + "0"*(len(a[1])-len(b[1]))
    elif len(b[1])>len(a[1]):
        a[1] = a[1] + "0"*(len(b[1])-len(a[1]))
    a[0] = a[0][::-1]
    a[1] = a[1][::-1]
    b[0] = b[0][::-1]
    b[1] = b[1][::-1]

    # Дробная часть
    add = 8
    for i in range(len(b[-1])):
        s += str((add + int(a[-1][i]) - int(b[-1][i]))%8)
        if (add + int(a[-1][i]) - int(b[-1][i])) < 8:
            add = 7
        else:
            add = 8
    s += "."

    # Целая часть
    for i in range(len(b[0])):
        s += str((add + int(a[0][i]) - int(b[0][i]))%8)
        if (add + int(a[0][i]) - int(b[0][i])) < 8:
            add = 7
        else:
            add = 8
    if minus:
        s += "-"
    if len(s) >= 2 and s[-1] == "0" and s[-2] != ".":
        return s[::-1].strip("0").strip(".")
    return s[::-1].rstrip("0").strip(".")
                
    

#print(mathoperations("0.888-1.25+1.25"))
