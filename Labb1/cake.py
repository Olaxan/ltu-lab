import math

def newline(lines=1):
    for i in range(0, lines):
        print()

def recept(antal):
    print(math.ceil(3/4 * antal), "st ägg")
    print(3/4 * antal, "dl strösocker")
    print(2/4 * antal, "tsk vaniljsocker")
    print(2/4 * antal, "tsk bakpulver")
    print(3/4 * antal, "dl vetemjöl")
    print(75/4 * antal, "g smör")
    print(1/4 * antal, "l vatten")

def tidBlanda(antal):
    return 10 + antal

def tidGradda(antal):
    return 30 + antal * 3

def sockerkaka(antal):
    print('Sockerkaka för', antal, 'personer:')
    newline()
    recept(antal)
    newline()
    print('Tid att blanda:', tidBlanda(antal), 'min')
    print('Tid att grädda:', tidGradda(antal), 'min')
    newline()


sockerkaka(4)
sockerkaka(7)
