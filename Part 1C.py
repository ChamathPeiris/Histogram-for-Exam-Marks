count = 0
rangeA = 0  #0-29
rangeB = 0  #30-39
rangeC = 0  #40-69
rangeD = 0  #70-100
total = 0
avg_of_marks = 0
highest_mark = 0
lowest_mark = 0
print("Histrogram for Student's Exam Marks")
print("To exit the process, enter a negative number")
 
while True:
          try:
                 mark = int(input("Enter marks:"))
                 
                 if mark < 0:
                     break
                 lowest_mark = mark

                 while mark >= 0:
                          
                         if mark > highest_mark and mark <= 100:
                                 highest_mark = mark
                         
                         if mark < lowest_mark and mark <= 100:
                                 lowest_mark = mark
                                 
                         if mark > 100:
                                 print("This mark is not valid,Try again.")       
                                 
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
                                 avg_of_marks = (total / count)
                                 
                         mark = int(input("Enter marks:"))
                         
                 break
             
          except ValueError:
                 print("Invalid mark entered, please try again")
             
                 continue
             
print("0-29  ="  ,'*' * rangeA,end='\n')
print("30-39 ="  ,'*' * rangeB,end='\n')
print("40-69 ="  ,'*' * rangeC,end='\n')
print("70-100="  ,'*' * rangeD,end='\n')
print("a) Average of students: ",avg_of_marks)
print("b) Number of students: ",count)
print("c) Number of students above the pass mark: ",rangeC + rangeD)
print("d) The highst mark: ",highest_mark)
print("e) The lowest mark:",lowest_mark)
