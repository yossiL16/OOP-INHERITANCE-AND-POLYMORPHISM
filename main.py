from classes.Mission import Mission
from classes.Agent import Agent

agent1 = Agent("yossi", 10)
mission1 = Mission("barzel", "gaza")
mission1.get_assigned_agent(agent1.code_name)
mission1.brif()
