n,m,k = map(int,input().split())
num = list(map(int,input().split()))

num.sort() # 오름차순 정렬
first = num[n-1] # 가장 큰 수 저장
second = num[n-2] # 두번째로 큰 수 저장
sum = 0

while True:
  for i in range(k):
    if(m<=0): 
      break
    sum+=first
    m-=1
  if(m<=0):
    break  
  sum+=second
  m-=1
print(sum)