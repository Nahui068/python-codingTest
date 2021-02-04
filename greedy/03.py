n,m = map(int,input().split())
res = 0

# 한 행씩 입력받음
for i in range(n):
  num = list(map(int,input().split()))
  m = min(num) # 가장 작은 수 찾기
  res = max(res,m) # 가장 작은 수 중에서 가장 큰 수 찾기
print(res)