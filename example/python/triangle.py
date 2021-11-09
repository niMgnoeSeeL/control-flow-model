NOTATRIANGLE = 0
SCALENE = 1
ISOSCELES = 2
EQUILATERAL = 3

def triangle(s):
    if len(s) != 3:
        result = NOTATRIANGLE
    else:
        a = int(s[0])
        b = int(s[1])
        c = int(s[2])
        if a == b:
            if b == c:
                result = EQUILATERAL
            else:
                result = ISOSCELES
        else:
            if b == c:
                result = ISOSCELES
            else:
                if a == c:
                    result = ISOSCELES
                else:
                    result = SCALENE
    return result