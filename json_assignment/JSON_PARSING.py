class Data ():
    user = ""
    course = ""
    role =0

    def __init__(self, detail):
        self.user = detail[0]
        self.course = detail[1]
        self.role = detail[2]
