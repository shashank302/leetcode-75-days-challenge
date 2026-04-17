#using Sum Formula(Thisapproach is best when number is 1-n
#Sum=n(n+1)/2
       
"""def find_missing(arr,n):
  expected=n*(n+1)//2
  actual=sum(arr)
  return expected-actual"""

#using sorting
def find_missing(arr):
  arr.sort()

  for i in range(len(arr)-1):
    if arr[i+1]!=arr[i]+1:
      return arr[i]+1

if __name__=="__main__":
  arr=list(map(int, input("Enter the array element:").split()))
  n=int(input("Enter n(range 1 to n):"))
  missing=find_missing(arr,n)
  print("missing number is:",missing)