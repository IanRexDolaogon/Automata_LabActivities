def run_moore_machine(input_string):

    state_outputs = {
        'A': 'A',
        'B': 'B',
        'C_A': 'A',  # State C when arrived via output 'A'
        'C_C': 'C',  # State C when arrived via output 'C'
        'D_B': 'B',  # State D when arrived via output 'B'
        'D_C': 'C',  # State D when arrived via output 'C'
        'E': 'C'
    }
    
    transitions = {
        'A':   {'0': 'A',   '1': 'B'},
        'B':   {'0': 'C_A', '1': 'D_B'},
        'C_A': {'0': 'D_C', '1': 'B'},
        'C_C': {'0': 'D_C', '1': 'B'},
        'D_B': {'0': 'B',   '1': 'C_C'},
        'D_C': {'0': 'B',   '1': 'C_C'},
        'E':   {'0': 'D_C', '1': 'E'}
    }
    
    
    start_state = 'A'
    current_state = start_state
    
    output_string = state_outputs[current_state]
    
    for char in input_string:
        if char not in transitions[current_state]:
            return "Error: Invalid input character"
            
        current_state = transitions[current_state][char]
        
        output_string += state_outputs[current_state]
        
    return output_string

inputs_to_process = [
    "00110",
    "11001",
    "1010110",
    "101111"
]

print("Processing inputs with converted Moore Machine:")
print("-" * 40)

for input_str in inputs_to_process:
    result = run_moore_machine(input_str)
    print(f"Input:  {input_str}")
    print(f"Output: {result}\n")