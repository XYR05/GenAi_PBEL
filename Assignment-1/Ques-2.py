def calculate_total(marks):
    
    return sum(marks)


def calculate_percentage(total):
   
    return (total / 500) * 100


def assign_grade(percentage):
    """Assign grade using if-elif-else based on percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'F'


def display_student(roll, info):
    """Print student details in a simple format."""
    print('Roll No. :', roll)
    print('Name     :', info['name'])
    print('Marks    :', info['marks'])
    print('Total    :', info['total'])
    print('Percent  :', f"{info['percentage']:.2f}%")
    print('Grade    :', info['grade'])
    print('-' * 30)


def main():
    students = {}  # dictionary to store student info keyed by roll no.

    n = int(input('How many students do you want to enter? '))
    
    for i in range(n):
        print(f"\nEntering data for student {i+1}")
        roll = input('Enter Roll No.: ').strip()
        name = input('Enter Name    : ').strip()
        marks = []
        for s in range(1, 6):
             m = int(input(f'Enter mark for subject {s} (0-100): '))

        total = calculate_total(marks)
        percentage = calculate_percentage(total)
        grade = assign_grade(percentage)

        students[roll] = {
            'name': name,
            'marks': marks,
            'total': total,
            'percentage': percentage,
            'grade': grade,
        }

    print('\nAll Student Records')
    print('=' * 30)
    for roll, info in students.items():
        display_student(roll, info)

    if students:
        topper_roll = max(students, key=lambda r: students[r]['percentage'])
        print('\nTopper')
        print('=' * 30)
        display_student(topper_roll, students[topper_roll])


if __name__ == '__main__':
    main()
