class User(object):
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name

    def __str__(self):
        return f"phone: {self.phone}, name: {self.name}"

    def is_this(self, phone):
        if self.phone == phone:
            return True
        return False
