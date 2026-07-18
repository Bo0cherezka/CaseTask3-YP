def max_power(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for dragon in range(1, min(7, i) + 1):
            dp[i] = max(dp[i], dragon * dp[i - dragon])

    return dp[n]


N = int(input("Введите общее количество голов: "))
print("Максимальная сила стаи =", max_power(N))