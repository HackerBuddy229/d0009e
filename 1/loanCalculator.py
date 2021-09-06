# Calculates total cost of loan using the formula k=P + (a+1)Pr/2

def kostnad(loan, rate, years):
    cost = loan + (years+1)*loan*rate/2
    return cost
