//Suppose we have a list of marks and we have to find that how many students have marks less than 50. For doing this we write the code given below.

marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
length = len(marks)
i = 0
while i < length:
  if(marks[i] < 50):
    print(marks[i])
  i +=1


