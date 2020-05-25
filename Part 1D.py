count = 0
rangeA = 0  #0-29
rangeB = 0  #30-39
rangeC = 0  #40-69
rangeD = 0  #70-100
total = 0
method = 0
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
                          
                         if mark > highest_mark and mark <= 100: #identfy the highest mark
                                 highest_mark = mark
                         
                         if mark < lowest_mark and mark <= 100:  #identfy the lowest mark
                                 lowest_mark = mark
                                 
                         if mark > 100:
                                 print("This mark is not valid,Try again.")    #print invalid values   
                                 
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
                                 total = total + mark   #calculate total 
                                 avg_of_marks = (total / count) #calculate average of marks
                                 
                         mark = int(input("Enter marks:"))
                         
                 break
             
          except ValueError:
                 print("Invalid mark entered, please try again")
          continue
                 

                
print("\n  0-29 : 30-39 : 40-69 : 70-100 ")#print vertical histrogram
list = [rangeA, rangeB, rangeC, rangeD]
while max(list) >= method:
    if rangeA > method:
        print("    *   ",end="")
    elif rangeA <= method:
        print("        ",end="")
    if rangeB > method:
        print("    *   ",end="")
    elif rangeB <= method:
        print("        ",end="")
    if rangeC > method:
        print("    *   ",end="")
    elif rangeC <= method:
        print("        ",end="")
    if rangeD > method:
        print("    *   ",end="")
    elif rangeD <= method:
        print("        ",end="")
    method += 1
    print("\n")
             

print("a) Average of students: ",avg_of_marks)#print average of students
print("b) Number of students: ",count)#print number of students
print("c) Number of students above the pass mark: ",rangeC + rangeD)#print number of students above the pass mark
print("d) The highst mark: ",highest_mark)#print highest marks
print("e) The lowest mark:",lowest_mark)#print lowest marks
