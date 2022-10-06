from collections import defaultdict
def fun(A):
  d = defaultdict(lambda:0)
  for i in A:
    d[i]+=1
  ans=0
  
  for k,v in d.items():
    ans+=1
    if v>=2:
      print(int(str(k)[::-1]))
      if d[int(str(k)[::-1])] ==0:
        ans+=1
  print(ans)


A = [15,50,17,17,50]

fun(A)


def fun1(N)
  s = str(N)
  d = [[]]*10
  for i,ch in enumerate(str(N)):
    d[ord(ch) - ord('0')].append(i)
  swapI=0
  for i in range(9,-1,-1):s
    if len(d[i])==1:
      if swapI != d[i][0]:
        swapJ = d[i][0]
        return int(s[:swapI]+s[swapI:swapJ][::-1]+s[swapJ:])
      else:
        swapI+=1
    else:
      lis = d[i]
      cnt = 0
      while(len(lis)!=1):
        #subtract 1 from list
        newLis = []
        for val in lis:
          if val-1>swapI:
            newLis.append(val-1)
        maxVal = ord(s[newLis[0]])
        for j in newLis:
          if int(s[j])>maxVal:
            maxVal = int(s[j])
         
        lis = newLis
        newLis = []
        for j in lis:
          if int(s[j])==maxVal:
            newLis.append(j)
        lis = newLis
        cnt+=1
      swapJ = lis[0]+cnt
      return int(s[:swapI]+s[swapI:swapJ][::-1]+s[swapJ:])
        
