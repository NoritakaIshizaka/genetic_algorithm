import random
from sympy import Symbol
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
        return [Symbol('x_{}'.format(i)) for i in range(self.dimension)]


    def setFitness(self, fitness):
        self.fitness = fitness


    def cal(self, select_method = 'roulette', crossOver_method = 'one'):
        if self.var_type == 'bin':
            individuals = [[random.randint(0,1) for _ in range(self.dimension)] for _ in range(self.populations)]
        elif self.var_type == 'float':
            pass
        print(individuals)


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
    ga.cal()



if __name__ == '__main__':
    main()