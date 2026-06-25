p="/home/harry/Internship - ibm"
with open(p+"/marks.txt", "w+") as f4:
    f4.write("Anjali, 99 \n Rohit, 95 \n Priya, 8 \n")
    f4.seek(0)
    content = f4.read()
    print(content)
    c=0
    f=0
    for l in content.splitlines():
        name, marks = l.split(",")
        if int(marks) >= 45:
            print(name, "has passed the exam with marks:", marks)
            c=c+1
        else:
             f=f+1
             print(name, "has failed the exam with marks:", marks)
    print("Number of students who passed: ", c)
    print("Number of students who failed: ", f)
       
