import random
from sympy import Symbol, evaluate
import textwrap

import genetic_algorithm_error


class GeneticAlgorithm(object):
    def __init__( self, dimension, populations = 1000, generations = 100, problem_type = 'min', var_type = 'bin'):
        self.dimension = dimension
        self.populations = populations
        self.generations = generations
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
        evaluateResults = []
        for individual in individuals:
            evaluateResult = self.fitness.subs([(k, v) for k, v in zip(self.x, individual)])
            evaluateResults.append([individual, evaluateResult])
        return evaluateResults


    def resolve(self, select_method = 'roulette', crossOver_method = 'one'):
        if self.var_type == 'bin':
            individuals = [[random.randint(0,1) for _ in range(self.dimension)] for _ in range(self.populations)]
        elif self.var_type == 'float':
            pass
        for i in range(self.generations):
            evaluateResults = self.evaluateFitness(individuals=individuals)
            sort_evaluateResults = sorted(evaluateResults, key=lambda x:x[1], reverse = True)


    def crossOver(self):
        pass


    def select(self):
        pass


    def maturate(self):
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
    f = x[0] + x[1] + x[2]
    ga.setFitness(f)
    print(ga.fitness)
    ga.resolve()



if __name__ == '__main__':
    main()