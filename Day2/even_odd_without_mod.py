def even_odd_check(n):
  if((n//2)*2==n):
    print("Even")
  else:
    print("Odd")

n=int(input("Enter the number:"))
even_odd_check(n)


#using recursion

"""def check_even(n):
    if n == 0:
        return "Even"
    if n == 1:
        return "Odd"
    return check_even(n - 2)


num = int(input("Enter number: "))
print(check_even(num))"""