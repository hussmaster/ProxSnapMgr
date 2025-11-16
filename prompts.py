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

#Function to get snapshot name
def snapName():
    questions = [
        inquirer.Text("SnapName", message="Name for snapshot?", default="updates")
    ]

    snapAnswer = inquirer.prompt(questions)
    return snapAnswer

#Function to select what to do, snapshot, remove snapshot etc
def proxActions():
    questions = [
        inquirer.List("action", message="What do you want to do?", choices=["Snapshot","Delete Snapshot", "Exit"])
    ]

    actionAnswer = inquirer.prompt(questions)
    return actionAnswer

#Prompts user to select which snapshot to remove
def removeSnapChoice(vmName, snapList):
    questions = [
        inquirer.List("snap", message=f"Snapshots for {vmName}, which to remove?", choices=snapList)
    ]

    removeAnswer = inquirer.prompt(questions)
    return removeAnswer

#Keeps user in the delete snapshot loop
def removeLoop():
    questions = [
        inquirer.List("action", message="Keep deleting snaps?", choices=["yes", "no"])
    ]

    actionAnswer = inquirer.prompt(questions)
    return actionAnswer