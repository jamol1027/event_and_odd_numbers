#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".

a = 2846
b = (a//1000+1)%2+(a//100%10+1)%2+(a//10%10+1)%2+(a%10+1)%2
print(b)