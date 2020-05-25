count = 0
rangeA = 0   #0-29
rangeB = 0   #30-39
rangeC = 0   #40-69
rangeD = 0   #70-100
total = 0
print("Histrogram for Exam Marks")
print("To exit the process, enter a negative number")

mark = int(input("Enter marks:"))
while mark >= 0:
        if mark > 69 and mark <= 100:
            rangeD += 1
        elif mark > 39 and mark <= 69:
            rangeC += 1
        elif mark > 29 and mark <= 39:
            rangeB += 1
        elif mark >= 0 and mark <= 29:
            rangeA += 1
        if mark >= 0 and mark <= 100:        
           count += 1
           total = total + mark
           mark = int(input("Enter marks:"))
   
print("0-29  ="  ,'*' * rangeA,end='\n')
print("30-39 ="  ,'*' * rangeB,end='\n')
print("40-69 ="  ,'*' * rangeC,end='\n')
print("70-100="  ,'*' * rangeD,end='\n')
print("a) Number of students: ",count)
