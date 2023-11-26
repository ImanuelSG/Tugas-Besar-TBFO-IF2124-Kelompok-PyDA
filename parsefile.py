def extract_input_symbols(productions):
    input_symbols = set()
    for state, transitions in productions.items():
        for transition in transitions:
            read_symbol = transition[0]
            if read_symbol not in input_symbols:
                input_symbols.add(read_symbol)

    return input_symbols

def extract_stack_symbols(productions):
    stack_symbols = set()
    for state, transitions in productions.items():
        for transition in transitions:
            take_from_stack = transition[1]
            if take_from_stack.startswith('<') and take_from_stack.endswith('>'):
                stack_symbols.add(take_from_stack)
    return stack_symbols

def extract_states(productions):
    states = set()
    for state, transitions in productions.items():
        states.add(state)


    return states

def parse_file(filename):
    global productions
    global start_state
    global input_symbols
    global stack_symbols
    global start_stack
    global accepting_states
    global accept_condition

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

    # Extract information from lines
    total_states, input_symbols, stack_symbols = map(str.split, lines[:3])
    start_state, start_stack, accepting_states, accept_condition = map(str.strip, lines[3:7])

    # Initialize productions dictionary
    productions = {}

    # Add production rules
    for line in lines[7:]:
        parts = line.split()
        current_state, read_symbol, take_stack, next_state, add_stack = parts
        production = (read_symbol, take_stack, next_state, add_stack)

        if current_state not in productions:
            productions[current_state] = []

        productions[current_state].append(production)

    extracted_input_symbols = extract_input_symbols(productions)
    extracted_stack_symbols = extract_stack_symbols(productions)
    extracted_states = extract_states(productions)
    
    print("Total States:", extracted_states)
    print("Input Word Symbols:", extracted_input_symbols)
    print("Stack Symbols:", extracted_stack_symbols)
    print("Starting State:", start_state)
    print("Starting Stack:", start_stack)
    print("Accepting States:", accepting_states)
    print("Accept Condition:", accept_condition)

    print("//nProductions:")
    for key, value in productions.items():
        print(f"{key}:", value)

    return 1
