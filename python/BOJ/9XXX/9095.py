'''
9095번 1, 2, 3 더하기 실버3
브루트포스, 다이나믹 프로그래밍
다이나믹 프로그래밍
'''
tc = int(input())
dp = [1] * (11)
dp[2] = 2
for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(tc):
    num = int(input())
    print(dp[num])
