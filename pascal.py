
from math import factorial

def pascal(n):
  
  for i in range(n):
	  for j in range(n-i+1):

		# for left spacing
		  print(end=" ")

	  for j in range(i+1):

	  	print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	  print()
