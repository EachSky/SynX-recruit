def get_fibonacci(n):
    """返回前 n 个斐波那契数（F(0)=0）"""
    if n <= 0:
        return []               # 边界：若n不符合条件，return意为立即停机，跳过后续所有部分
    fib = [0, 1]                # 声明递推的基本条件
    while len(fib) < n:         # 继续循环的条件
        fib.append(fib[-1] + fib[-2]) #.append() → 列表方法，把新元素追加到末尾
        # fib[-1] → 负数索引，-1 表示“最后一个元素”，-2 表示“倒数第二个”
    return fib[:n]              # 切片：当 n=1 时只返回 [0]
#切片语法  fib[start : stop]  永远左闭右开
#[:n]  里 start 省略=0，stop=n，所以实际拿到  fib[0] ... fib[n-1] ，共 n 个元素
print(get_fibonacci(10))
print(get_fibonacci(100))
print(get_fibonacci(1))

import math#import后加工具箱，相当于c里的main()
phi = (1 + math.sqrt(5)) / 2#声明
#math.sqrt(5) → 调用工具箱里的平方根函数
#感受黄金比例
n = 20
approx = phi**n / math.sqrt(5)#近似值
#！！！体会斐波那契通项公式
#当 n 很大时 ψⁿ → 0，所以 F(n) ≈ φⁿ/√5
real = get_fibonacci(21)[-1]   # 第 20 项 真实值
#[-1] → 负数索引，取最后一个元素
print("近似值:", approx)
print("真实值:", real)
print("相对误差:", abs(approx - real) / real)
#abs 是“绝对值”

