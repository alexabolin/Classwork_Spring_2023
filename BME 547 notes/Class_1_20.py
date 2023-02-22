# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:06:33 2023

@author: hboli
"""
def increment_by_five(x):
    answer = x + 5
    if answer == 15:
        print("Bad input")
        return False
    return answer, True
    
y = increment_by_five(11)
print("The answer is {}".format(y))
print(y[0])
print(y[1])

# do editing in new branch
#     git branch branchname
#     git checkout branchname
#     git add
#     git commit -m 
#     git push 
# commit branch to main once it is ready
#     When to commit? Commit once per function
#     Make sure commit messages are unique: explain what was changed and why
# once committed and pushed, always remember to checkout main and git pull