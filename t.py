def isValid(s: str) -> bool:
    stack = []
    info = {"}": "{", ")": "(", "]": "["}

    for c in s:
        if c in ")]}":
            if not stack or stack.pop() != info[c]:
                return False
        if c in "({[":
            stack.append(c)

    return not stack


# print(isValid("aaa[bbb]cc"))


def pal(s) -> bool:
    pal = "".join(filter(str.isalpha, s)).lower()
    return pal == pal[::-1]


# print(pal("cat8tac"))

def ana(s1, s2) -> bool:
    return sorted(s1) == sorted(s2)


def rev_matrix(m) -> list:
    rm = []
    for list in m:
        rm.append(list[::-1])

    return rm


# print(rev_matrix([[1, 2, 3], [4, 5, 6]]))

a = "01223456789"

# print(a[::-1])

base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def b_to_int(n, b1) -> int:
    nb = 0
    sign = 1

    if n[0] == "-":
        n = n[1:]
        sign = -1

    for c in n:
        nb = nb * b1 + base.index(c)

    return nb * sign


def int_to_b(nb, b2) -> str:
    n = []
    sign = ""

    if nb == 0:
        return "0"

    if nb < 0:
        sign = "-"
        nb = -nb

    while nb > 0:
        n.append(base[nb % b2])
        nb //= b2

    return sign + "".join(reversed(n))


def b_to_b(n, b1, b2) -> str:
    nb = b_to_int(n, b1)
    return int_to_b(nb, b2)


print(b_to_b("1010", 2, 16))


def shift(s, i) -> str:
    ns = ""

    for c in s:
        if c.islower():
            ns += chr((ord(c) - ord("a") + i) % 26 + ord("a"))
        elif c.isupper():
            ns += chr((ord(c) - ord("A") + i) % 26 + ord("A"))
        else:
            ns += c

    return ns


print(shift("abcde", 1))
