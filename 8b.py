def distributive_law_and_over_or(A, B, C):
    # Distributive Law: A AND (B OR C) = (A AND B) OR (A AND C)
    left_side = A and (B or C)
    right_side = (A and B) or (A and C)
    return left_side == right_side

def distributive_law_or_over_and(A, B, C):
    # Distributive Law: A OR (B AND C) = (A OR B) AND (A OR C)
    left_side = A or (B and C)
    right_side = (A or B) and (A or C)
    return left_side == right_side

# Test values
A, B, C = True, False, True

# Check Distributive Law for AND over OR
and_over_or_result = distributive_law_and_over_or(A, B, C)
print(f"Distributive Law: A AND (B OR C) = (A AND B) OR (A AND C) is {and_over_or_result}")

# Check Distributive Law for OR over AND
or_over_and_result = distributive_law_or_over_and(A, B, C)
print(f"Distributive Law: A OR (B AND C) = (A OR B) AND (A OR C) is {or_over_and_result}")
