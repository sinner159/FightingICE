from final_project_code.action import ALL_QUICK_ACTIONS
class Config():

    def __init__(self, c_param = 1.4, 
                        eval_function = "HPDIFF", 
                        sim_limit = 500, 
                        num_simulations = 3, 
                        action_set = ALL_QUICK_ACTIONS, 
                        action_set_name = "ALL_QUICK_ACTIONS", 
                        opp_ai = "Toothless",
                        maxHP = 400,
                        rounds = 1):
        self.c_param = c_param
        self.eval_function = eval_function
        self.simulation_limt = sim_limit
        self.num_simulations = num_simulations
        self.action_set = action_set
        self.action_set_name = action_set_name
        self.opp_ai = opp_ai
        self.rounds = rounds
        self.maxHP = maxHP

    def __str__(self):
        return f"""
C: {self.c_param} 
eval: {self.eval_function} 
sim_limit: {self.simulation_limt} 
num_simulations: {self.num_simulations} 
action_set: {self.action_set_name} 
opponent_ai: {self.opp_ai} 
maxHP: {self.maxHP} 
rounds: {self.rounds}
"""

    def __repr__(self):
        return str(self)

CONFIGS = [

#c_param
Config(c_param = 5,
            eval_function = "HPDIFF", 
            sim_limit = 500, 
            num_simulations = 3, 
            action_set = ALL_QUICK_ACTIONS, 
            action_set_name = "ALL_QUICK_ACTIONS",
            opp_ai="Toothless",
            rounds=5),
Config(c_param = 6,
            eval_function = "HPDIFF", 
            sim_limit = 500, 
            num_simulations = 3, 
            action_set = ALL_QUICK_ACTIONS, 
            action_set_name = "ALL_QUICK_ACTIONS",
            opp_ai="Toothless",
            rounds=5),
Config(c_param = 7,
            eval_function = "HPDIFF", 
            sim_limit = 500, 
            num_simulations = 3, 
            action_set = ALL_QUICK_ACTIONS, 
            action_set_name = "ALL_QUICK_ACTIONS",
            opp_ai="Toothless",
            rounds=5),
]