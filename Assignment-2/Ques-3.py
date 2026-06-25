p="/home/harry/Internship - ibm"
with open(p+"/attendance.txt", "w+") as s:
    s.write("Rahul:A \n Anjali:A \n Harry:P \n")
    s.seek(0)
    content = s.read()
    print(content)
    a=0
    p=0
    for l in content.splitlines():
        name, at = l.split(":")
        if((at.strip()) == 'A'):
             print(name, "is absent")
             a=a+1
        else:
                p=p+1
                print(name, "is present")
    print("Number of absent employees: ", a)
    print("Number of present employees: ", p)