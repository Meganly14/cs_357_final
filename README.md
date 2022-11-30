# cs_357_final
# By alex and megan

This program converts the input DFA to a * version of the input. 
First the program checks to make sure the input JSON file is in correct format, if not, the program will reject the file and exit the program. 
If the file is in correect format the program will add a new start state woth an epsilon transition to the previous start state. 
After doing so it will then add an epsilon transition from the accept state to the previous sart state. 
After adding the appropriate transitions to the DFA, the newly converted NFA will be in the output file. 

1. Use or Create a JSON file 
2. Feed into program with user input 
3. If file and format is accepted a * version of the DFA input will be created in output.JSON
