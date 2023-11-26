def extract_states(productions): #ini cuma buat mastiin apakah states yang ditulis di txt udah semua
    states = set()
    for state, transitions in productions.items():
        realstate = state[0]
        if realstate not in states:
            states.add(realstate)

    return states

def extract_input_symbols(productions): #ini cuma buat mastiin apakah input simbol yang ditulis di txt udah semua
    inputsymbols = set()
    for state, transitions in productions.items():
        inputsymbol = state[1]
        if inputsymbol not in inputsymbols:
            inputsymbols.add(inputsymbol)
    return inputsymbols

def extract_stack_symbols(productions): #ini cuma buat mastiin apakah stack symbol yang ditulis di txt udah semua
    stacksymbols = set()
    for state, transitions in productions.items():
        stacksymbol = state[2]
        if stacksymbol not in stacksymbols:
            stacksymbols.add(stacksymbol)
    return stacksymbols