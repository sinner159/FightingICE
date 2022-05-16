from final_project_code.Actions import ALL_QUICK_ACTIONS
class Config():

    def __init__(self):
        self.c_param = 1.4
        self.eval_function = "HPDIFF"
        self.simulation_limt = 500
        self.num_simulations = 3
        self.action_set = ALL_QUICK_ACTIONS
        self.action_set_name = "ALL_QUICK_ACTIONS"


    def __str__(self):
        return f"C: {self.c_param} eval: {self.eval_function} sim_limit: {self.simulation_limt} num_simulations: {self.num_simulations} action_set: {self.action_set_name}"

    def __repr__(self):
        return str(self)