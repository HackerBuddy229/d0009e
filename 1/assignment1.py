# import loan calculator module
from loanCalculator import kostnad
import os

# define variables
loan = int(os.environ["loan"])
rate = float(os.environ["rate"])
years = int(os.environ["years"])

# calculate cost
cost = kostnad(loan, rate, years)

# prints cost in the format "Den totala kostnaden efter X år är Y kr"
print("Den totala kostnaden efter", years, "år är", int(cost), "kr.")
