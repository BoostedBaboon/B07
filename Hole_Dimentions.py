def CalculateHoleDiameter(Case, w, Metal):
    if Metal == True:
        if Case == 1:
            D2 = w / 5.5
        if Case == 2:
            D2 = w / 8
        if Case == 3:
            D2 = w / 5.5
    else:
        if Case == 1:
            D2 = w / 7.5
        if Case == 2:
            D2 = w / 8
        if Case == 3:
            D2 = w / 5.5
    return D2

def CalculateHoleDimensions(Case, D2, w, L, Metal):
    if Case == 1:
        ry = [w / 2 - 1.5 * D2]
        rz = [L / 2 - 1.5 * D2]
    if Case == 2:
        ry = [w / 2 - 1.5 * D2, 0]
        rz = [L / 2 - 1.5 * D2, L / 2 - 1.5 * D2]
    if Case == 3:
        ry = [w / 2 - 1.5 * D2, w / 2 - 1.5 * D2]
        if Metal is True:
            rz = [L / 2 - 1.5 * D2, L / 2 - 4 * D2]
        else:
            rz = [L / 2 - 1.5 * D2, L / 2 - 6 * D2]

    return [ry, rz]


# D21 = CalculateHoleDiameter(1, W, True)
# D22 = CalculateHoleDiameter(2, W, True)
# D23 = CalculateHoleDiameter(3, W, True)
# print(D21, D22, D23)

# X1 =
# X2 =
# X3 =
# ry1 = CalculateHoleDimensions(1, X1, W, L, True)[0]
# rz1 = CalculateHoleDimensions(1, X1, W, L, True)[1]
#
# ry2 = CalculateHoleDimensions(2, X2, W, L, True)[0]
# rz2 = CalculateHoleDimensions(2, X2, W, L, True)[1]
#
# ry3 = CalculateHoleDimensions(3, X3, W, L, True)[0]
# rz3 = CalculateHoleDimensions(3, X3, W, L, True)[1]
