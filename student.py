def calculate_total(marks):
    t=sum(marks)
    return t
def calculate_percentage(total, num_subjects):
    p=(total/num_subjects)
    return p
def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif (percentage >= 75 and percentage < 90):
        return "B"
    elif (percentage >= 60 and percentage < 75):
        return "C"
    elif percentage >= 40 and percentage < 60:
        return "D"
    else:
        return "F"
def main():
    marks=[float(input("Enter marks for subject {}: ".format(i+1))) for i in range(5)]
    total=calculate_total(marks)
    percentage=calculate_percentage(total, 5)
    grade=assign_grade(percentage)
    print("Total marks: {}".format(total))
    print("Percentage: {}".format(percentage))
    print("Grade: {}".format(grade))

if __name__ == "__main__":
    main()