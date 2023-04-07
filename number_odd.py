#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
a = 5664
b = (a//1000)%2+(a//100)%2+(a//10)%2+a%2
print(b)