class employees:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class supervisors(employees):  
    def __init__(self, first_name, last_name, password):
        super().__init__(first_name, last_name)
        self.password = password

class chefs(employees):
    def leave_requests(self, days):
        return "May I take a leave for " + str(days) + " days."

adrian = supervisors("Adrian", "A", "apple")
print(adrian.first_name)
print(adrian.password)

print()

emily = chefs("Emily", "E")
print(emily.first_name)
print(emily.leave_requests(3))