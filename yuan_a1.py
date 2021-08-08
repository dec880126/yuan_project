# ランダムに選択した整数の三乗根を近似的に求める手続きを考える．

# 以下のプログラムでは変数solが繰り返しによって徐々にxの三乗根に近づく．

# x=random.randint(1,10)
# eps=0.0001
# step=0.001
# sol=0
# for i in range(10) :
#     if(abs(x-sol**3)>eps) :
#         sol=sol+step
#     else :
#         break
#     print(i,"近似解",sol,"近似誤差",abs(x-sol**3))
# 以下の問いに答えなさい
# 近似解が求められるよう，プログラムを修正しなさい．
# 近似解の精度は小数点以下何桁か説明しなさい．
# 近似誤差はどの程度か説明しなさい．
# ランダムに選択した整数が入力であるとき，計算にかかる時間が平均でどの程度か見積り，その理由を説明しなさい

# version 1
import random
from timeit import timeit


def main():
    x = random.randint(1, 10)
    eps = 0.01
    step = 0.01
    sol = 0

    min = 0
    while True:
        condition = abs(x - sol ** 3)
        if condition > eps:
            sol += step
            if condition > min and min != 0:
                break
            min = condition
        else:
            break
    print(x, "近似解", sol, "近似誤差", abs(x - sol ** 3))


print(str(timeit("main()", "from __main__ import main", number=1)) + " sec")

# version 2
# import random
# from timeit import timeit

# def main():
#     x = random.randint(1,10)
#     eps=0.001
#     step=0.0001
#     sol = 0
#     while True :
#         if(abs(x - sol**3) > eps) :
#             sol = sol + step
#         else :
#             break

#     print(x, "近似解", sol, "近似誤差", abs(x-sol**3))

# print(str(timeit('main()', 'from __main__ import main', number = 1)) + " sec")
