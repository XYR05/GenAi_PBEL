def calculate_hra(basic):
    return 0.2*basic

def calculate_da(basic):
    return 0.1*basic

def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = calculate_da(basic)
    net_salary = basic + hra + da
    print("net Salary: ", net_salary)

def main():
    n=str(input("Enter the employee name: "))
    basic = float(input("Enter the basic salary: "))
    calculate_net_salary(basic)
if __name__ == "__main__":
    main()
    