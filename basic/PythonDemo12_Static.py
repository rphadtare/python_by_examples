class Employee:
    org_name = "Wipro Ltd"

    def __init__(self, emp_id, name, sal):
        self.emp_id = emp_id
        self.name = name
        self.sal = sal

    def __str__(self):
        return f"Employee[id={self.emp_id}, name={self.name}, " \
               f"sal={self.sal}, Company_name = {Employee.org_name}]"

    @staticmethod
    def get_org_name():
        return Employee.org_name


def main():
    e1 = Employee(1, "Pooja", 9000)
    e2 = Employee(2, "Rohit", 6000)
    e3 = Employee(3, "Rushi", 5000)

    for e in (e1, e2, e3):
        print(e)
        print("*" * 50)

    print(f"Updating org_name via obj for {e1.name}")
    e1.org_name = "ABC Steels"

    print(f"Updating org_name via class")
    Employee.org_name = "UBS"

    print("Organization name post completion of update")
    print("-" * 50)
    for e in (e1, e2, e3):
        print(f"[Accessing using object] organization "
              f"of {e.name}: {e.org_name}")

        print(f"[Accessing using static method] organization "
              f"of {e.name}: {e.get_org_name()}")

        print("*" * 50)

    print("[Accessing static method using class name] "
          "org value:", Employee.get_org_name())

if __name__ == "__main__":
    main()
else:
    print(__name__)
    pass
