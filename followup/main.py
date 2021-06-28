def getCommandList():
    print("What would you like follow ups on? (Print ALL for options)")
    all_inputs = []
    prompt = '->'
    command = input(prompt)

    all_commands = []
    if command == "ALL":
        file = open("data.txt", "r")
        for line in file:
            all_commands.append(line.split('|')[0])
        print(all_commands)
        file.close()
        exit()
    else:
        while command:
            all_inputs.append(command)
            command = input(prompt)
    print(all_inputs)
    return(all_inputs)

def printResults(all_inputs):
    followups = ""
    for command in all_inputs:
        file = open("data.txt", "r")
        for line in file:
            if(line.split('|')[0] == command):
                followups = followups + line.split('|')[0] + ": " + line.split('|')[1] + '\n' 
        file.close()

    
    if followups != "":
        print("Thanks everyone for the time earlier!  I wanted to provide a few helpful docs links we spoke about:")
        print(followups)

all_inputs = getCommandList()
printResults(all_inputs)

