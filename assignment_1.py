# REX IAN V DOLAOGON
# ASSIGNMENT 1

class MealyState:
    def __init__(self, name):
        self.name = name
        self.transitions = {}
    
    def add_transition(self, input_symbol, next_state, output):
        self.transitions[input_symbol] = (next_state, output)

    def get_next(self, input_symbol):
        return self.transitions[input_symbol]

class MealyMachine:
    def __init__(self):
        self.A = MealyState("A")
        self.B = MealyState("B")

        self.A.add_transition("0", self.B, "b")
        self.A.add_transition("1", self.A, "a")
        self.B.add_transition("0", self.B, "b")
        self.B.add_transition("1", self.A, "a")

        self.current = self.A
    
    def process(self, input_string):
        outputs=[]
        states = [self.current.name]
        for symbol in input_string:
            next_state, output = self.current.get_next(symbol)
            outputs.append(output)
            self.current = next_state
            states.append(self.current.name)
        return states, outputs
    
# mealy = MealyMachine()
# states, outputs = mealy.process("1010")
# print("Mealy Machine")
# print("States: ","->".join(states))
# print("Ouputs:","".join(outputs))
# Mealy Machine
# States:  A->A->B->A->B
# Ouputs: abab

class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}
    
    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state
    
    def get_next(self,input_symbol):
        return self.transitions[input_symbol]

class MooreMachine:
    def __init__(self):
        self.A = MooreState("A", "a")
        self.B = MooreState("B", "b")

        self.A.add_transition("0", self.B)
        self.A.add_transition("1", self.A)
        self.B.add_transition("0", self.B)
        self.B.add_transition("1", self.A)

        self.current = self.A
    
    def process(self, input_strings):
        outputs = [self.current.output]
        states =[self.current.name]
        for symbol in input_strings:
            self.current = self.current.get_next(symbol)
            outputs.append(self.current.output)
            states.append(self.current.name)
        return states, outputs

# moore = MooreMachine()
# states, outputs = moore.process("1010")
# print("Moore Machine")
# print("States: ","->".join(states))
# print("Ouputs:","".join(outputs))
# Moore Machine
# States:  A->A->B->A->B
# Ouputs: aabab


