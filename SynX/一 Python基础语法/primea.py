def get_primes(n):
    primes = []          # 是一个列表(数组)
    candidate = 2        # 从 2 开始挨个试
    while len(primes) < n:
#len(primes)是把当前已找到的质数个数报出来，起到改变形式的作用（因为列表和整数不能比大小）
        is_prime = True  # 先假设它是质数
        for p in primes: # 只试除已找到的质数
            if p * p > candidate:   # √n 边界
                break#说明假设正确
            #证明n是质数
            #“试除到 √n就够了”
            # 反证：n = a·b
            #且a >√n,
            #则b <√n，  所以若 ≤√n都没因子,n必是质数。
            if candidate % p == 0:  # 整除 → 不是质数
                is_prime = False
                break
        if is_prime:
        #！！！与for平行，先for再if,起到了最终审判的效果
            primes.append(candidate)
        candidate += 1
    return primes
print(get_primes(10))

import time#time()可立刻告诉你当前“秒数”，所以time是一个瞬时值
t0 = time.time()#表示现在几点，精确到小数点
#它告诉你的是从 1970 年 1 月 1 日 00:00:00 开始，到此时此刻一共过了多少秒（带小数，精确到微秒）
p = get_primes(10000)   # 先跑 1 万
t1 = time.time()
print("耗时:" ,t1-t0, "秒；最后几个:", p[-5:])#这里时间相减，可读出究竟过了多少秒
#！！！ ,t1-t0, 有逗号间隔，电脑会自动把变量先转成字符串然后再输出，如果此处没有逗号会语法报错
#此处进行运行时间计算，有助于体会用√n 来限制质数已经很有效