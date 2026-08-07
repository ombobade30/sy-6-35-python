# Decorator
def line(func):
    def wrapper(*args):
        print("=" * 40)
        func(*args)
        print("=" * 40)
    return wrapper


class Report:

    templates = {"Default": "******** STUDENT REPORT ********"}
    count = 0

    def __init__(self, report_id, department, name):
        self.report_id = report_id
        self.department = department
        self.name = name
        Report.count += 1

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, name):
        print("\n" + Report.get_template(name))
        print(self)

    @line
    def display(self):
        print("Report ID  :", self.report_id)
        print("Department :", self.department)
        print("Name       :", self.name)

    def __str__(self):
        return f"Report ID: {self.report_id}\nDepartment: {self.department}\nName: {self.name}"

    @classmethod
    def total_reports(cls):
        print("\nTotal Reports Generated:", cls.count)


n = int(input("Enter the number of reports: "))
reports = []

for i in range(n):
    print(f"\nEnter details for Report {i+1}")
    report = Report(
        input("Enter Report ID: "),
        input("Enter Department: "),
        input("Enter Name: ")
    )
    reports.append(report)

print("\n===== REPORT DETAILS =====")

for report in reports:
    report.display()
    report("Default")

Report.total_reports()