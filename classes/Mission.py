from classes.Agent import *

class Mission:

    def __init__(self, mission_name:str, target_location:str):
        self.mission_name = mission_name
        self.target_location =target_location
        self.assigned_agent = None

    def get_assigned_agent(self, agent: Agent):
        self.assigned_agent = agent

    def brif(self):
        print(f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent}")