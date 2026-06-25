p="/home/harry/Internship - ibm"
with open(p+"/salary.txt", "w+") as s:
    s.write("Rahul, 5000 \n Anjali, 60000 \n Harry, 55000 \n")
    s.seek(0)
    content = s.read()
    print(content)
    c=0
    for l in content.splitlines():
        name, salary = l.split(",")
        if(int(salary.strip()) >= 50000):
            print(name, "has a salary of:", salary)
            c=c+1
    print("Number of employees with salary >= 50000: ", c)