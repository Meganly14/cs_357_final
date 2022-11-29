import numpy as np
import json

#returns false if :
# 1. accept states are not a subset of the states
# 2. if there are no states
# 3. if there is an empty alphabet
# 4. the start state is not one of the states
def isValidNFA(input):
    subset_checker = np.isin(accept_states,states)
    if False in subset_checker or len(states) == 0 or len(alphabet) == 0 or start_state not in states:
        print("This is not a valid DFA or NFA.")
        return False    
    return True

#adds in a new start state q_start that epsilon transitions to the old start state
#adds in epsilon transitions to acccept states to loop back
#writes the updated JSON object to file "output.json"
def constructStarNFA(input):
    if isValidNFA(input):
        for states in raw_states:
            if states.get("state") in accept_states:
                states["ε"] = start_state
        raw_states.append({"state": "q_start", "ε":start_state})
        data["start-state"]  = "q_start"
        output = open('output.json','w')
        json.dump(data,output)
        print("The NFA that recognizes the star of the input language can be found in output.json")
        output.close()
    else: 
        exit()

#Attempts to open the file, will exit the program if:
# 1. file is not found in the same directory
# 2. file is not able to be opened
# 3. file is not a JSON file.
# NOTE: the loads() function can recognize many other types
filename = input("Enter your input file name (inlcuding extension): ")
with open(filename,"r") as input:
    try:
        str_input = input.read()
        # DATA - containts the JSON object, as a dictionary
        data = json.loads(str_input)
        input.close()
        #error catching file I/O    
    except ValueError:
        print("The input is not a valid JSON object.")
        exit()

#define some global variables for use in the functions
raw_states = data["states"]
#print(raw_states)
#array of the state names
states = np.array(list((i.get("state") for i in data["states"])))
#array of the accept state names
accept_states = np.array(list(i.get("state") for i in data["accept-states"]))
#array of the DFA alphabet
alphabet = np.array(data.get("alphabet"))
#the start state
start_state = data.get("start-state")

constructStarNFA(data)
