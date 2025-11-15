import inquirer

def vmChoice(vmList):
    #List to return
    vmChoiceList = []
    #Setup question prompt
    questions = [
        inquirer.Checkbox('VMs',
                          message="VM list",
                          choices=vmList                          
                          )
    ]
    #Execute prompt
    vmAnswers = inquirer.prompt(questions)
    #Iterate through dict to get values
    for k, v in vmAnswers.items():
        for item in v:
            vmChoiceList.append(item)
    #Return list of tuples(ID, Name, type, status)
    return vmChoiceList