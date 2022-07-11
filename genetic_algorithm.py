import random
from sympy import Symbol
import textwrap

import genetic_algorithm_error


class GeneticAlgorithm(object):
    def __init__( self, dimension, populations = 100, generations = 100, problem_type = 'min', var_type = 'bin'):
        self.dimension = dimension
        self.populations = populations
        self.generations = generations
        self._selectRate = 0.5
        self._crossOverRate = 0.49
        self._mutateRate = 0.01
        if problem_type != 'min' and problem_type != 'max':
            raise genetic_algorithm_error.ProblemTypeError("set 'min' or 'max'")
        if var_type != 'bin' and var_type != 'float':
            raise genetic_algorithm_error.VariableTypeError("set 'bin' or 'float'")
        self.problem_type = problem_type
        self.var_type = var_type


    def __str__(self ):
        output_str = textwrap.dedent(f"""\
        dimension : {self.dimension}
        populations : {self.populations}
        generations : {self.generations}
        problem type : {self.problem_type}
        variable type : {self.var_type}\
        """)
        return output_str


    def getVariable(self):
        x = [Symbol('x_{}'.format(i)) for i in range(self.dimension)]
        self.x = x
        return x


    def setFitness(self, fitness):
        if self.problem_type == 'min':
            self.fitness =  fitness * (-1)
        elif self.problem_type == 'max':
            self.fitness = fitness


    def evaluateFitness(self, individuals):
        results = []
        for individual in individuals:
            result = self.fitness.subs([(k, v) for k, v in zip(self.x, individual)])
            results.append([individual, result])
        return results


    def resolve(self, select_method = 'roulette', crossOver_method = 'one'):
        if self.var_type == 'bin':
            individuals = [[random.randint(0,1) for _ in range(self.dimension)] for _ in range(self.populations)]
        elif self.var_type == 'float':
            pass
        for i in range(self.generations):
            results = self.evaluateFitness(individuals=individuals)
            sort_results = sorted(results, key=lambda x:x[1], reverse = True)
            fitnessMin = sort_results[-1][1]
            if fitnessMin < 0:
                sort_results = [[sort_result[0], sort_result[1] - (fitnessMin - 1)] for sort_result in sort_results]
            next_individuals = self.geneticOperate(sort_results)
            

    def geneticOperate(self, sort_results):
        next_individuals=[]
        while True:
            operationSelector = random.random()
            if 0.0 < operationSelector <= self._selectRate:
                self.select(self)
            elif self._selectRate < operationSelector <= self._selectRate + self._crossOverRate:
                self.crossOver(self)
            elif self._selectRate + self._crossOverRate < operationSelector < self._selectRate + self._crossOverRate + self._mutateRate
                self.matate(self)



    def select(self, sort_results, method='roulette'):
        pass


    def crossOver(self):
        pass


    def matate(self):
        pass


def main():
    ga = GeneticAlgorithm(
        dimension = 3,
        populations = 100,
        generations = 100,
        problem_type = 'max',
        var_type = 'bin'
    )
    print(ga)
    x = ga.getVariable()
    print(x)
    f = (x[0] + x[1] + x[2]) * -1
    ga.setFitness(f)
    print(ga.fitness)
    ga.resolve()



if __name__ == '__main__':
    main()