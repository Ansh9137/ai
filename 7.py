from simpleai.search import CspProblem, backtrack, min_conflicts
from simpleai.search.viewers import ConsoleViewer
from simpleai.search.csp import (
    MOST_CONSTRAINED_VARIABLE,
    HIGHEST_DEGREE_VARIABLE,
    LEAST_CONSTRAINING_VALUE
)

# Variables: The regions in the map
variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')

# Domain: The possible colors for each region
domains = dict((v, ['red', 'green', 'blue']) for v in variables)

# Constraints function: Neighbors must have different colors
def const_different(variables, values):
    return values[0] != values[1]  # Neighbors must have different values (colors)

# Constraints: Define which regions are adjacent (neighbors)
constraints = [
    (('WA', 'NT'), const_different),
    (('WA', 'SA'), const_different),
    (('NT', 'SA'), const_different),
    (('SA', 'Q'), const_different),
    (('NT', 'Q'), const_different),
    (('SA', 'NSW'), const_different),
    (('Q', 'NSW'), const_different),
    (('SA', 'V'), const_different),
    (('NSW', 'V'), const_different),
]

# Create the CSP problem
my_problem = CspProblem(variables, domains, constraints)

# Solve using different heuristics and print the results

# 1. Default backtracking
print("Solution with default backtracking:")
print(backtrack(my_problem))

# 2. Backtracking with Most Constrained Variable heuristic
print("\nSolution with Most Constrained Variable heuristic:")
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))

# 3. Backtracking with Highest Degree Variable heuristic
print("\nSolution with Highest Degree Variable heuristic:")
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))

# 4. Backtracking with Least Constraining Value heuristic
print("\nSolution with Least Constraining Value heuristic:")
print(backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE))

# 5. Backtracking with Most Constrained Variable and Least Constraining Value heuristic
print("\nSolution with Most Constrained Variable and Least Constraining Value heuristic:")
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE,
               value_heuristic=LEAST_CONSTRAINING_VALUE))

# 6. Backtracking with Highest Degree Variable and Least Constraining Value heuristic
print("\nSolution with Highest Degree Variable and Least Constraining Value heuristic:")
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE,
               value_heuristic=LEAST_CONSTRAINING_VALUE))

# 7. Min-conflicts heuristic
print("\nSolution with min-conflicts heuristic:")
print(min_conflicts(my_problem))
