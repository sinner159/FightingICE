from final_project_code.Chromosome import Chromosome
from final_project_code.action import Action, ALL_USEFUL_ACTIONS
import numpy as np
class GAActionSelection():

    def __init__(self, filename, populationSize, chromosomeLength):
        self.populationSize = populationSize
        self.filename = filename
        self.all_actions = ALL_USEFUL_ACTIONS.copy()
        self.chromosomeLength = chromosomeLength
        self.population = []

    def initialization(self):
        for i in range(self.populationSize):
            
            chromosome = Chromosome()
            actions = self.all_actions.copy()
            for j in range(self.chromosomeLength):
                random_index = np.random.randint(0, len(actions))
                chromosome.addAction(actions.pop(random_index))

            self.population.append(chromosome)
            
    
    def selection(self):
        
        for chrm in self.population:
            chrm.fitness = self.fitness(chrm)
            
        self.population.sort(key=lambda x: x.fitness, reverse=True)

        return self.population[0:4]


    def recombination(self, newPop:list):
        self.population.clear()
        all_moves = []
        for chrom in newPop:
            all_moves += chrom.actions

        for i in range(self.populationSize):
            
            chromosome = Chromosome()
            actions = all_moves.copy()
            for j in range(self.chromosomeLength):
                random_index = np.random.randint(0, len(actions))
                chromosome.addAction(actions.pop(random_index))

            self.population.append(chromosome)
            
        

    def mutation(self):
        
        for chrm in self.population:
           i =  np.random.randint(0, 10)
           if i == 1:
               action = np.random.choice(self.all_actions,1)
               random_index = np.random.randint(0, len(chrm.actions))
               chrm.actions[random_index] = action
            

    def fitness(self, chrm: Chromosome):
        return chrm.performanceMetrics.roundData[0].hpGap
