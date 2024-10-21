# Define the predicates
def is_batsman(person):
    return person == "Sachin"

def is_cricketer(batsman):
    return batsman == "batsman"

# Deriving the conclusion
def derive_cricketer(person):
    if is_batsman(person) and is_cricketer("batsman"):
        return f"{person} is a cricketer"
    return f"{person} is not a cricketer"

# Test the derivation
sachin = "Sachin"
result = derive_cricketer(sachin)
print(result)
