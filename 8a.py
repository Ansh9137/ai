def associative_law_and(A, B, C):
    # Associative Law for AND
    left_side = (A and B) and C
    right_side = A and (B and C)
    return left_side == right_side

def associative_law_or(A, B, C):
    # Associative Law for OR
    left_side = (A or B) or C
    right_side = A or (B or C)
    return left_side == right_side

# Test values
A, B, C = True, False, True

# Check Associative Law for AND
and_result = associative_law_and(A, B, C)
print(f"Associative Law for AND: (A AND B) AND C = A AND (B AND C) is {and_result}")

# Check Associative Law for OR
or_result = associative_law_or(A, B, C)
print(f"Associative Law for OR: (A OR B) OR C = A OR (B OR C) is {or_result}")
