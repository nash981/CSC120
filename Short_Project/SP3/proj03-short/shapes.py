def shape_alpha():
    alpha = [[],[]]
    alpha[0] = [10,"abc","jkl",40]
    alpha[1] = [[1.1,-17],[123,456]]
    return alpha

def shape_bravo():
    bravo = [[],[]]
    items = ["bogus","righteous"]
    bravo[0] = [["whoa","excellent"],items]
    bravo[1] = [items,"rufus"]
    return bravo

def shape_charlie(arg1):
    charlie = [[],arg1]
    charlie[0] = [[],arg1]
    charlie[0][0] = [[],arg1]
    charlie[0][0][0] = [[],None]
    return charlie

def shape_delta(arg1,arg2):
    delta = [arg1,arg2,[],10]
    delta[2] = [arg1,[],20,arg2]
    delta[2][1] = [arg1,arg2,[arg1,arg2],30]
    return delta

def shape_echo(arg1,arg2,arg3):
    echo = [[[],arg2],arg1]
    echo[0][0] = [echo,arg3]
    return echo