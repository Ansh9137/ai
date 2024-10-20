# Define family members with their gender
male = {
    "John": True,
    "Michael": True,
    "David": True,
    "Robert": True,
    "Steve": True,
    "Daniel": True,
    "Tom": True,
    "Alex": True,
    "Ryan": True,
}

female = {
    "Emily": False,
    "Sarah": False,
    "Jessica": False,
    "Lisa": False,
    "Anna": False,
    "Karen": False,
    "Nancy": False,
}

# Define parent-child relationships
parents = {
    "John": ["Emily", "Michael"],  # John is the father of Emily and Michael
    "Sarah": ["Emily", "Michael"],  # Sarah is the mother of Emily and Michael
    "Michael": ["David", "Lisa"],   # Michael is the father of David and Lisa
    "Jessica": ["David", "Lisa"],   # Jessica is the mother of David and Lisa
    "Robert": ["Daniel"],             # Robert is the father of Daniel
    "Emily": ["Ryan"],                # Emily is the mother of Ryan
}

# Define rules for family relations
def is_father(name, child):
    return name in male and child in parents.get(name, [])

def is_mother(name, child):
    return name in female and child in parents.get(name, [])

def is_grandfather(grandfather, grandchild):
    return grandfather in male and any(
        is_father(grandfather, parent) and grandchild in parents.get(parent, [])
        for parent in parents
    )

def is_grandmother(grandmother, grandchild):
    return grandmother in female and any(
        is_mother(grandmother, parent) and grandchild in parents.get(parent, [])
        for parent in parents
    )

def is_brother(sibling, person):
    return sibling in male and sibling != person and any(person in parents.get(parent, []) for parent in parents if sibling in parents[parent])

def is_sister(sibling, person):
    return sibling in female and sibling != person and any(person in parents.get(parent, []) for parent in parents if sibling in parents[parent])

def is_uncle(uncle, nephew):
    return uncle in male and any(is_brother(uncle, parent) for parent in parents.get(nephew, []))

def is_aunt(aunt, niece):
    return aunt in female and any(is_sister(aunt, parent) for parent in parents.get(niece, []))

def is_nephew(nephew, uncle_or_aunt):
    return any(is_uncle(uncle_or_aunt, child) for child in parents.get(nephew, []))

def is_cousin(cousin, person):
    return any(is_brother_or_sister(parent, person) for parent in parents.get(cousin, []))

def is_brother_or_sister(sibling, person):
    return sibling != person and any(sibling in parents.get(parent, []) for parent in parents if person in parents[parent])

# Example Queries
print("Is John the father of Emily?", is_father("John", "Emily"))
print("Is Sarah the mother of Michael?", is_mother("Sarah", "Michael"))
print("Is John a grandfather of Ryan?", is_grandfather("John", "Ryan"))
print("Is Sarah a grandmother of David?", is_grandmother("Sarah", "David"))
print("Is Michael a brother of Lisa?", is_brother("Michael", "Lisa"))
print("Is Emily a sister of Michael?", is_sister("Emily", "Michael"))
print("Is John an uncle of Daniel?", is_uncle("John", "Daniel"))
print("Is Jessica an aunt of Ryan?", is_aunt("Jessica", "Ryan"))
print("Is David a cousin of Ryan?", is_cousin("David", "Ryan"))
