import argparse
from colorama import Fore, Style
from parsefile import *
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

    def simulate(self, input_string):
        stack = [self.initial_stack]  
        current_state = self.initial_state
        rowrightnow = 1
        
        for symbol in input_string:
            print (current_state)
            if symbol == "nl":
                rowrightnow += 1 
            elif (current_state, symbol, stack[-1]) in self.transitions: #ini buat mastiin apakah ada transisi yang sesuai
                next_state, push_stack = self.transitions[(current_state, symbol, stack[-1])][0]#ini buat move to the next state dan push stack
                stack.pop()
                if push_stack != "e":
                    if push_stack.startswith('<') and push_stack.endswith('>'):
                        push_stack = push_stack[1:-1]  #ini buat handle kalau dia ada dua push misal <br><body>
                        substrings = push_stack.split('><')
                        for substring in reversed(substrings):
                            stack.append('<' + substring + '>')
                    else:
                        stack.append(push_stack)
                current_state = next_state
            elif (current_state, symbol, "<%>") in self.transitions: #ini buat handle top of stack any
                next_state, push_stack = self.transitions[(current_state, symbol, "<%>")][0]
                prev = stack.pop()#simpen dia top of stacknya apa sebenernya
                if push_stack != "e":
                    if push_stack.startswith('<') and push_stack.endswith('>'):
                        push_stack = push_stack[1:-1]  
                        substrings = push_stack.split('><')
                        for substring in reversed(substrings):#push 
                            if (substring == "%"):
                                stack.append(prev)
                            else:
                                stack.append('<' + substring + '>')
                    else:
                        stack.append(prev)
                current_state = next_state
            elif (current_state, "e", stack[-1]) in self.transitions:
                next_state, push_stack = self.transitions[(current_state, "e", stack[-1])][0]
                stack.pop()
                if push_stack != "e":
                    if push_stack.startswith('<') and push_stack.endswith('>'):
                        push_stack = push_stack[1:-1]  # Remove the angle brackets
                        substrings = push_stack.split('><')
                        for substring in reversed(substrings):
                            if (substring == "%"):
                                stack.append(prev)
                            else:
                                stack.append('<' + substring + '>')
                    else:
                        stack.append(push_stack)
                current_state = next_state
                input_string.insert(0, symbol)
                
            else:
                # print (stack)
                # print (input_symbols)
                
                # if (symbol not in input_symbols):
                    
                #     rowrightnow += 1

                print()
                print(f"Oh No!, your file {Style.BRIGHT}{Fore.RED}{Fore.YELLOW}{html_file}{Style.RESET_ALL} is {Style.BRIGHT}{Fore.RED}REJECTED{Style.RESET_ALL}")
                print(f"Error: No transition found for current state = {current_state}, symbol = {symbol}, and top of stack = {stack[-1]}")
                print(f"at row {rowrightnow} - {Style.BRIGHT}{Fore.RED}{arrlines[rowrightnow-1].lstrip()}{Style.RESET_ALL}")
                return False

        print (f"Congrats! your file {Style.BRIGHT}{Fore.RED}{html_file}{Style.RESET_ALL} is {Style.BRIGHT}{Fore.GREEN}ACCEPTED{Style.RESET_ALL}")
        

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

def lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        input_str = file.readlines()
    return input_str

def main():
    parser = argparse.ArgumentParser(description='PDA Simulator')
    parser.add_argument('txt_file', help='Path to the TXT file')
    parser.add_argument('html_file', help='Path to the HTML file')
    args = parser.parse_args()

    global txt_file,html_file
    txt_file = args.txt_file
    html_file = args.html_file

    global arrlines
    arrlines = lines_from_file(html_file)

    parse_file(txt_file)
    tokens = tokenize_html_from_file(html_file)
    print (tokens)
    PDA.simulate(pda, tokens)

if __name__ == '__main__':
    main()


