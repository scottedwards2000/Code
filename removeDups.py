#mypy /Users/renee/MEGA/GithubClones/Code/removeDups.py
from typing import List#, Dict

def remove_duplicates(database: List[int]) -> int:
    deduped = []
    for x in database:
        if x not in deduped:
            deduped.append(x)
    return len(deduped)

print(remove_duplicates([1,1,2]))
print(remove_duplicates([1,2,3.1]))
