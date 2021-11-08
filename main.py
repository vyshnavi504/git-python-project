def palindrome(str):
   if str[::-1]==str:
     return True
   return False
str=input()
if palindrome(str)==True:
  print("is palindrome")
else:
  print("not palindrome")