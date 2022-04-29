#!py -2.7
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print ("Start:"), problem.getStartState()
    borda = util.Stack()                        # Borda onde os nos / estados serao avaliados
    Caminho = []                                # Vetor que armazena as direcoes
    Visitados = []                              # Locais Visitados
    borda.push(problem.getStartState())         # Coloca o no / estado inicial na fila LIFO
    CaminhoAtual = util.Stack()                 # direcao atual
    Estado = borda.pop()

    while problem.isGoalState(Estado) != True:          # Loop ate encontrar a comida

        if Estado not in Visitados:                     # Verifica se o proximo estado nao foi visitado, senao:
            Visitados.append(Estado)                    # Adiciona o estado ao vetor Visitados
            sucessors = problem.getSuccessors(Estado)   # Chama uma funcao que devolve o proximo estado, dando uma lista com(NoFilho, acao, custo) 
            for no_filho, acao, custo in sucessors:        # Chama as variaveis do estado atual
                borda.push(no_filho)                    # Acrescenta na fila LIFO o No Filho que sera expandido
                CaminhoAtual.push(Caminho + [acao])     # Entao o caminho atual que o agente vai seguir
        Estado = borda.pop()                            # Pega o no mais fundo da borda
        Caminho = CaminhoAtual.pop()                    # vai para o proximo estado
    return Caminho                                      # retorna o estado
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    borda = util.Queue()                        # Borda onde os nos / estados serao avaliados, mas de maneira diferente, utilizando a fila FIFO
    Caminho = []                                # Vetor que armazena as direcoes
    Visitados = []                              # Locais Visitados
    borda.push(problem.getStartState())         # Coloca o no / estado inicial na fila LIFO
    CaminhoAtual = util.Queue()                 # direcao atual
    Estado = borda.pop()
    while problem.isGoalState(Estado) != True:          # Loop ate encontrar a comida

        if Estado not in Visitados:                     # Verifica se o proximo estado nao foi visitado, senao:
            Visitados.append(Estado)                    # Adiciona o estado ao vetor Visitados
            sucessors = problem.getSuccessors(Estado)   # Chama uma funcao que devolve o proximo estado, dando uma lista com(NoFilho, acao, custo) 
            for no_filho, acao, custo in sucessors:     # Chama as variaveis do estado atual
                borda.push(no_filho)                    # Acrescenta na fila FIFO o No Filho que sera expandido
                CaminhoAtual.push(Caminho + [acao])     # Entao o caminho atual que o agente vai seguir
        Estado = borda.pop()                            # Pega o no mais fundo da borda
        Caminho = CaminhoAtual.pop()                    # vai para o proximo estado
    print(len(Caminho))
    return Caminho                                      # retorna o estado

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    borda = util.PriorityQueue()                # Borda onde os nos tem certa prioridade referente ao seu custo de execucao
    Caminho = []                                # Vetor que armazena as direcoes
    Visitados = []                              # Locais Visitados
    borda.push(problem.getStartState(),0)       # Coloca o no / estado inicial em um filha de prioridade com custo 0
    CaminhoAtual = util.PriorityQueue()         # direcao atual
    Estado = borda.pop()
    

    while problem.isGoalState(Estado) != True:                                  # Loop ate encontrar a comida

        if Estado not in Visitados:                                             # Verifica se o proximo estado nao foi visitado, senao:
            Visitados.append(Estado)                                                # Adiciona o estado ao vetor Visitados
            sucessors = problem.getSuccessors(Estado)                           # Chama uma funcao que devolve o proximo estado, dando uma lista com(NoFilho, acao, custo) 
            for no_filho, acao, custo in sucessors:                             # Chama as variaveis do estado atual
                CustoParaAcao = problem.getCostOfActions(Caminho + [acao])      # O custo para um possivel caminho
                if no_filho not in Visitados:                           
                    borda.push(no_filho, CustoParaAcao)                         # e colocado o proximo no e o custo para tal acao
                    CaminhoAtual.push(Caminho + [acao], CustoParaAcao)          # Entao o caminho atual que o agente vai seguir baseado no menor custo
        Estado = borda.pop()                            # Pega o no mais fundo da borda
        Caminho = CaminhoAtual.pop()                    # vai para o proximo estado
    return Caminho                                      # retorna o estado
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    borda = util.PriorityQueue()                # Borda onde os nos tem certa prioridade referente ao seu custo de execucao
    Caminho = []                                # Vetor que armazena as direcoes
    Visitados = []                              # Locais Visitados
    borda.push(problem.getStartState(),0)       # Coloca o no / estado inicial em um filha de prioridade com custo 0
    CaminhoAtual = util.PriorityQueue()         # direcao atual
    Estado = borda.pop()
    

    while problem.isGoalState(Estado) != True:                                  # Loop ate encontrar a comida
        if Estado not in Visitados:                                             # Verifica se o proximo estado nao foi visitado, senao:
            Visitados.append(Estado)                                            # Adiciona o estado ao vetor Visitados
            sucessors = problem.getSuccessors(Estado)                           # Chama uma funcao que devolve o proximo estado, dando uma lista com(NoFilho, acao, custo) 
            for no_filho, acao, custo in sucessors:                             # Chama as variaveis do estado atual
                CustoParaAcao = problem.getCostOfActions(Caminho + [acao]) + heuristic(no_filho, problem)      # O custo para um possivel caminho + uma funcao heuristica que estima o custo futuro
                if no_filho not in Visitados:                           
                    borda.push(no_filho, CustoParaAcao)                         # e colocado o proximo no e o custo para tal acao
                    CaminhoAtual.push(Caminho + [acao], CustoParaAcao)          # Entao o caminho atual que o agente vai seguir baseado no menor custo
        Estado = borda.pop()                            # Pega o no mais fundo da borda
        Caminho = CaminhoAtual.pop()                    # vai para o proximo estado
    return Caminho                                      # retorna o estado
    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


