# for i in range(6,-1,-3):  -- range from 6 to 0 with the step of -3
#     for j in range(1,4):  -- range from 1 to 3 with the step of 1
#         print(f' {i+j}',end='')
#  print()


i = 6
j = 1
while i >= 0:
    """
    First iteration: i = 6, j = 1,2,3 printing 6+1, 6+2, 6+3
    Second iteration: i = 3, j = 1,2,3 printing 3+1 3+2 3+3
    Last iteration: i = 0, j = 1,2,3 printing 0+1 0+2 0+3
    """
    while j < 4:
        print(f" {i+j}", end="")
        j+=1
    print()
    j = 1
    i -= 3
    
