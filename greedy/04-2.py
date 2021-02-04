import time

n,k = map(int,input().split())
result = 0

start_time = time.time()
while n >= k:
  while n%k != 0: # n이 k로 나누어 떨어지지 않을 경우
    n-=1
    result+=1
  n //= k # n이 k로 나누어 떨어지는 경우
  result+=1

while n > 1 : # 마지막으로 남은 수에 대해서 1빼기
  n-=1
  result+=1
end_time = time.time()  
print(result)
print('성능측정:',end_time-start_time)