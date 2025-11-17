from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI
import os, sys
from getVMs import get_VMs, listVMChoice
from prompts import proxActions
from snapshotVM import snapshotVM
from removeSnapshotVM import removeSnap

load_dotenv()
#Set variables from .env file
apiTok = os.environ.get("API_TOKEN")
hostIP = os.environ.get("HOST")
apiUser = os.environ.get("API_USER")
tokName = os.environ.get("TOKEN_NAME")



def main():
    #Connect to proxmox
    proxHost = ProxmoxAPI(hostIP, user=apiUser, token_name=tokName, token_value=apiTok, verify_ssl=False)
    #Get proxmox nodes
    nodes = proxHost.nodes.get()
    #Loop through nodes
    vmList = []
    for node in nodes:
        VMs = proxHost.cluster.resources.get(type='vm')
        #Get list of all VMs
        returnVMList = get_VMs(VMs)
        #Append to the list above
        vmList.extend(returnVMList)

    action = "run"
    #Loop to keep program running until user selects Exit or quits out manually
    while action != "Exit":
        action = proxActions()
        #Extract value out of returned dict
        action = (list(action.values())[0])
        if action == "Snapshot":
            validVMs = listVMChoice(vmList, proxHost)
            snapshotVM(validVMs, proxHost)
        elif action == "Delete Snapshot":
            validVMs = listVMChoice(vmList, proxHost)
            removeSnap(validVMs, proxHost)
        elif action == "Exit":
            sys.exit()

if __name__ == "__main__":
    main()