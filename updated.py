import random

IS_ABSENT = 0
FULL_TIME = 1
PART_TIME = 2
WORKING_FULL_DAY_HR = 8
WORKING_PART_TIME_HR = 4


class Employee:

    def __init__(self, name, emp_working_hour, emp_wage_per_hour, ):
        self.name = name
        self.emp_working_hour = emp_working_hour
        self.emp_wage_per_hour = emp_wage_per_hour
        self.company_dict = {}

    def __repr__(self):
        return "employee"

    def calculate_daily_wage(self, current_employee_hrs):
        return current_employee_hrs * self.emp_wage_per_hour

    @staticmethod
    def check_emp_working_hours(check_employee):
        emp_attendence = {
            FULL_TIME: WORKING_FULL_DAY_HR,
            PART_TIME: WORKING_PART_TIME_HR,
            IS_ABSENT: 0
        }
        return emp_attendence.get(check_employee)

    # Calculate Monthly Wages

    def calculate_wage(self, company_maximum_working_day, company_maximum_working_hrs):
        # global daily_wages
        working_days = 0
        working_hours = 0
        total_emp_wage = 0

        while working_days < company_maximum_working_day and working_hours < company_maximum_working_hrs:
            check_employee = random.randint(0, 2)
            employee_working_hours = self.check_emp_working_hours(check_employee)
            print(employee_working_hours, "hsdfhgvfeh")
            daily_wages = self.emp_wage_per_hour * employee_working_hours
            working_days += 1
            working_hours += employee_working_hours
            total_emp_wage += daily_wages
        return total_emp_wage


class Company:
    IS_ABSENT = 0
    IS_PRESENT_FULL_DAY = 1
    IS_PRESENT_PART_TIME = 2
    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4
    totalEmpWage = 0

    def __init__(self, company_name, emp_hrs=8, wage_per_hour=20):
        self.company_name = company_name
        self.emp_hrs = emp_hrs
        self.wage_per_hour = wage_per_hour
        self.employee_dict = {}

    def __repr__(self):
        return f"company   {self.company_name}"

    def set_employee(self, employee_obj):
        self.employee_dict.update({employee_obj.name: employee_obj})

    def set_total_wage(self, total_wage):
        self.total_wage = total_wage

    def get_dict(self):
        return {"company_name": self.company_name, "employee_hour": self.emp_hrs, "wage_per_hour": self.wage_per_hour,
                "employees": self.employee_dict}

    def get_employee(self, ename):
        return self.employee_dict.get(ename)


class CompanyOperation:

    def __init__(self):
        self.company_dict = {}


    def add_company(self, company_obj):
        self.company_dict.update({company_obj.company_name: company_obj})

    def display_company(self):
        return self.company_dict

    def get_company(self, company_name):
        return self.company_dict.get(company_name)


def get_company_data(company_obj, company_operation_obj: CompanyOperation):
    company = company_operation_obj.get_company(company_obj.company_name)
    print(company.get_dict())


if __name__ == "__main__":
    company_dict = {}
    # company_operation_obj = CompanyOperation()


    try:
        print("Enter 1 for adding company and employee")
        print("Enter 2 to check company details")
        choice = 0
        while choice != 3:

            choice = int(input(" Enter choice: "))
            if choice == 1:
                company_name = input("Enter the company: ")
                employee_name = input("Enter the Employee Name: ")
                company = company_dict.get(company_name)
                if not company:
                    company = Company(company_name, 8, 20)
                    employee = Employee(employee_name, 80, 22)
                    company.set_employee(employee)
                    company_dict.update({company_name: company})

            if choice == 2:
                company_name = input("Company Name: ")
                company = company_dict.get(company_name)
                print(company.get_dict())

                # print(company.employee_dict)

                # company_operation_obj.add_company(company)
                # print(CompanyOperation())

                for employee_name in company.employee_dict:
                    emp = company.employee_dict.get(employee_name)
                    print(f"Total wage of {emp.name}, {emp.calculate_wage(20, 25)}")


    except Exception as e:
        print(e)




