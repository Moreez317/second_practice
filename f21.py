def f21(x):

    if x[1] == 'opa':
        return 9

    elif x[1] == 'edn':
        if x[2] == 2006:
            return 2
        elif x[2] == 2016:
            if x[4] == 1972:
                return 0
            elif x[4] == 1989:
                return 1

    elif x[1] == 'terra':
        if x[0] == 2003:
            if x[3] == 1983:
                return 5
            elif x[3] == 2010:
                if x[4] == 1972:
                    return 3
                elif x[4] == 1989:
                    return 4

        elif x[0] == 2001:
            if x[4] == 1972:
                return 6
            elif x[4] == 1989:
                if x[2] == 2016:
                    return 7
                elif x[2] == 2006:
                    return 8

#print(f21([2001, 'terra', 2016, 2010, 1972]))

#f([2003, 'terra', 2016, 1983, 1989]) = 5

