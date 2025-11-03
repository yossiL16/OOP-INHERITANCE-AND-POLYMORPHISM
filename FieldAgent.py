from classes.Agent import Agent


class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level, region):
        super().__init__(code_name, clearance_level)
        self.region = region

    def report(self):
        super().report()
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.__clearance_level}. from: {self.region}")