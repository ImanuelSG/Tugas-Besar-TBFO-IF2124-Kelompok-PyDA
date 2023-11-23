from tokenizer import *

class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, initial_state, initial_stack, accepting_states, accepting_type, transitions):
        self.states = set(states)
        self.input_alphabet = set(input_alphabet)
        self.stack_alphabet = set(stack_alphabet)
        self.initial_state = initial_state
        self.initial_stack = initial_stack  
        self.accepting_states = set(accepting_states)
        self.accepting_type = accepting_type
        self.transitions = transitions

    def __str__(self):
        return (
            f"States: {self.states}\n"
            f"Input Alphabet: {self.input_alphabet}\n"
            f"Stack Alphabet: {self.stack_alphabet}\n"
            f"Initial State: {self.initial_state}\n"
            f"Initial Stack: {self.initial_stack}\n"
            f"Accepting States: {self.accepting_states}\n"
            f"Accepting Type: {self.accepting_type}\n"
            f"Transitions: {self.transitions}\n"
        )

    def simulate(self, input_string, current_state=None, stack=None, rowrightnow=1):
        if current_state is None:
            current_state = self.initial_state
        if stack is None:
            stack = [self.initial_stack]  
        

        for symbol in input_string:
            if symbol == "nl":
                rowrightnow += 1
            elif (current_state, symbol, stack[-1]) in self.transitions:
                branches = self.transitions[(current_state,symbol,stack[-1])]
                for transition in branches:
                    next_state, push_stack = transition
                    prev = stack.pop()
                    new_stack = list(stack)
                    if push_stack != "e":
                        if push_stack.startswith('<') and push_stack.endswith('>'):
                            push_stack = push_stack[1:-1]  # Remove the angle brackets
                            substrings = push_stack.split('><')
                            for substring in reversed(substrings):
                                if substring == "%":
                                    new_stack.append(prev)
                                else:
                                    new_stack.append('<' + substring + '>')
                        else:
                            if push_stack == "<%>":
                                new_stack.append(prev)
                            else :
                                new_stack.append(push_stack)
                if self.simulate(input_string,next_state,new_stack,rowrightnow):
                    return True
            else:
                print(f"Error: No transition for state {current_state}, symbol {symbol}, stack {stack[-1]} at row {rowrightnow}")
                return False
        print (stack)
        print (rowrightnow)
        return current_state in self.accepting_states and not stack


def extract_states(productions): #ini cuma buat mastiin apakah states yang ditulis di txt udah semua
    states = set()
    for state, transitions in productions.items():
        states.add(state)
    return states

def extract_input_symbols(productions): #ini cuma buat mastiin apakah input simbol yang ditulis di txt udah semua
    input_symbols = set()
    for state, transitions in productions.items():
        for transition in transitions:
            read_symbol = transition[0]
            if read_symbol not in input_symbols:
                input_symbols.add(read_symbol)
    return input_symbols

def extract_stack_symbols(productions): #ini cuma buat mastiin apakah stack symbol yang ditulis di txt udah semua
    stack_symbols = set()
    for state, transitions in productions.items():
        for transition in transitions:
            take_from_stack = transition[1]
            if take_from_stack.startswith('<') and take_from_stack.endswith('>'):
                stack_symbols.add(take_from_stack)

    return stack_symbols

def parse_file(filename):
    global productions
    global start_state
    global input_symbols
    global stack_symbols
    global start_stack
    global accepting_states
    global accept_condition
    global pda
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    total_states, input_symbols, stack_symbols = map(str.split, lines[:3])
    start_state, start_stack, accepting_states, accept_condition = map(str.strip, lines[3:7])
    productions = {}

    for line in lines[7:]:
        parts = line.split()
        current_state, read_symbol, take_stack, next_state, add_stack = parts
        production = (next_state, add_stack)

        key = (current_state, read_symbol, take_stack)  # Ini biar formatnya lebih enak

        if key not in productions:
            productions[key] = []
        productions[key].append(tuple(production))

    extracted_input_symbols = extract_input_symbols(productions)
    extracted_stack_symbols = extract_stack_symbols(productions)
    extracted_states = extract_states(productions)

    pda = PDA(
        states=extracted_states,
        input_alphabet=extracted_input_symbols,
        stack_alphabet=extracted_stack_symbols,
        initial_state=start_state,
        accepting_states=accepting_states,
        transitions=productions,
        initial_stack=start_stack,
        accepting_type=accept_condition
    )

filename = "table.txt"
parse_file(filename)
tokens = tokenize_html_from_file("Test//table.html")
print (tokens)
PDA.simulate(pda, tokens)

