import math

def kostnad(amount, interest, years):
    k = amount + (years + 1) * amount * interest / 2
    print('Den totala kostnaden efter', years, 'år är', k, 'kr.')


    
