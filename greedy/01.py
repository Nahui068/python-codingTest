n = int(input()) # 거스름돈
coin = [500,100,50,10] # 코인의 형태
m = 0 

for i in coin:
  m += n//i # 동전 최소 갯수
  n = n%i # 나머지 돈

print(m)