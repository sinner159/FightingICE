from final_project_code.Chromosome import Chromosome
from final_project_code.action import Action, ALL_USEFUL_ACTIONS
import numpy as np

class GAActionSelection():

    def __init__(self, filename, populationSize, chromosomeLength, selection_size, logger):
        self.populationSize = populationSize
        self.filename = filename
        self.all_actions = ALL_USEFUL_ACTIONS.copy()
        self.chromosomeLength = chromosomeLength
        self.population = []
        self.logger = logger
        self.selection_size = selection_size

    def initialization(self):
        for i in range(self.populationSize):
            
            chromosome = Chromosome()
            actions = self.all_actions.copy()
            for j in range(self.chromosomeLength):
                random_index = np.random.randint(0, len(actions))
                chromosome.addAction(actions.pop(random_index))

            self.population.append(chromosome)
            
    def loadFromFile(self):
        f = open(self.filename,"r")
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n","")
            chrm = Chromosome()
            actions = line.split(",")
            chrm.addActions(actions)
            self.population.append(chrm)

    def selection(self):
        
        self.logger.write(f"Selection begin")
        chrm:Chromosome
        for chrm in self.population:
            chrm.fitness = self.fitness(chrm)
        
        self.population.sort(key=lambda x: x.fitness, reverse=True)

        self.logger.write(f"Ranking")
        for chrm in self.population:
            self.logger.write(f"ID: {chrm.name} Fitness Level: {chrm.fitness}")

        self.logger.write(f"Selecting top {self.selection_size}")
        return self.population[0:self.selection_size]


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
        
        chrm:Chromosome
        for chrm in self.population:
           i =  np.random.randint(0, 10)
           if i == 1:
               self.logger.write(f"Mutating ID: {chrm.name}")
               action = np.random.choice(self.all_actions,1)[0]
               random_index = np.random.randint(0, len(chrm.actions))
               chrm.actions[random_index] = action
            

    def fitness(self, chrm: Chromosome):
        total = 0
        for round in chrm.performanceMetrics.roundData:
            total += round.hpGap


        return total / chrm.performanceMetrics.round


    def populationAsString(self):
        ret = "\n"
        for chrm in self.population:
            ret += f"{chrm}\n"
        return ret
