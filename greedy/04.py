import time

n,k = map(int,input().split())
count = 0

start_time = time.time()
while True:
  if(n%k==0):
    n = n//k
    count+=1
  if(n==1): break
  if(n%k!=0):
    n -= 1
    count+=1
end_time = time.time()
print(count)
print('성능측정:',end_time-start_time)

