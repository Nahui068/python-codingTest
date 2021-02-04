n,m,k = map(int,input().split())
num = list(map(int,input().split()))
count = 0

num.sort()
first = num[n-1]
second = num[n-2]

# 가장 큰 수가 더해지는 횟수
count = int(m/(k+1)) * k
count += m%(k+1) 

sum = 0
sum += count * first # 가장 큰 수 더하기
sum += (m-count)*second # 두번째로 큰 수 더하기

print(sum)
