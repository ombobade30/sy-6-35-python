def line(func):
    def wrapper(*args):
        print("=" * 40)
        func(*args)
        print("=" * 40)
    return wrapper


class Report:
    templates = {"Default": "******** STUDENT REPORT ********"}
    count = 0

    def __init__(self, report_id, department, name, title, content):
        self.report_id = report_id
        self.department = department
        self.name = name
        self.title = title
        self.content = content
        Report.count += 1

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, name):
        print("\n" + Report.get_template(name))
        print(self)

    @line
    def display(self):
        print("Report ID     :", self.report_id)
        print("Department    :", self.department)
        print("Name          :", self.name)
        print("Report Title  :", self.title)
        print("Report Content:", self.content)

    def __str__(self):
        return (
            f"Report ID: {self.report_id}\n"
            f"Department: {self.department}\n"
            f"Name: {self.name}\n"
            f"Report Title: {self.title}\n"
            f"Report Content: {self.content}"
        )

    @classmethod
    def total_reports(cls):
        print("\nTotal Reports Generated:", cls.count)


n = int(input("Enter the number of reports: "))
reports = []

for i in range(n):
    print(f"\nEnter details for Report {i + 1}")
    report_id = input("Report ID: ")
    department = input("Department: ")
    name = input("Student Name: ")
    title = input("Report Title: ")
    content = input("Report Content: ")

    r = Report(report_id, department, name, title, content)
    reports.append(r)

print("\n******** STUDENT REPORTS ********")

for r in reports:
    r.display()

Report.total_reports()  