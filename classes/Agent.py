

class Agent:

    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self.__clearance_level = clearance_level

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.__clearance_level}.", end=" ")

    def get_clearance_level(self):
        return self.__clearance_level

    def set_clearance_level(self, level):
        if (level >= 1) and (level <= 10):
            self.__clearance_level = level
        raise "You have exceeded the range."