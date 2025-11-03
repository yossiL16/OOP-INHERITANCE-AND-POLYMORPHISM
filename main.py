from classes.Agent import Agent
from classes.FieldAgent import FieldAgent
from classes.CyberAgent import CyberAgent



agent_1 = Agent("yossi" ,10)
agent_2 = FieldAgent("avi", 7, "gaza")
agent_3 = CyberAgent("dani", 8, "hacking")
agents_list = [
    agent_1,
    agent_2,
    agent_3
    ]

for agent in agents_list:
    agent.report()
Agent.get_total_agents()