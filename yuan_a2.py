# 以下のプログラムは整数 x の3乗根を２分探索で求める手続きを10回繰り返す．

# x=random.randint(10)
# eps=0.01

# low=1.0
# high=x
# sol=(low+high)/2.0

# for i in range(10) :
#     if(sol**3<x) :
#         low=sol
#     else :
#         high=sol
#     sol=(low+high)/2.0    
#     print(i,"近似値",sol,"復元誤差",abs(x-sol**3))
# 近似解が求められるよう，プログラムを修正しなさい．
# 繰り返しの回数が平均でどの程度か計測し，その理由を考察しなさい
import random

# x = random.randint(1, 10)
# eps = 0.01

# low = 1.0
# high = x
# sol = (low+high)/2.0    #5.5
sum = 0
t = 10001
do = 25
if24 = 0
for x in range(1, t):
    eps = 0.00001
    low = 1.0
    high = x
    sol = (low+high)/2.0    #5.5
    for i in range(do) :
        if i == 24:
            if24 += 1
        if(abs(x - sol**3) > eps) :
            if  sol**3 < x:
                temp = sol
                sol = (sol + high)/2
                low = temp
            else:
                temp = sol
                sol = (sol + low)/2
                high = temp
        else:
            break
    
    print(x,"近似値",sol,"復元誤差",abs(x-sol**3))
    print("Total Run:" + str(i) + "times")
    print("--------------------")
    sum += i

print(f"avg = {sum/(t-1)} times")
print(f"{if24=}")