for i in range(1, 8):
    couponNum = i
    for j in range(1, 8):
        if(j == 1):
            print(f" {i}", end="")
        else:
            couponNum += 7
            print(f" {couponNum}", end="")
    print()