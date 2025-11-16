from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI
import os, sys
from getVMs import *
from prompts import *
from snapshotVM import *
from removeSnapshotVM import removeSnap
from lxcCheck import checkMPLXC

load_dotenv()

apiTok = os.environ.get("API_TOKEN")
hostIP = os.environ.get("HOST")
apiUser = os.environ.get("API_USER")
tokName = os.environ.get("TOKEN_NAME")


#TODO
#Setup ENV with proxmox api key - done
#Verify connectivity with Proxmox - done
#Try and pull some details from a VM - done
#NEED to check if a VM is an LXC, if so, check if it has a mountpoint, remove from the list - done
#Come up with selection for actions ie. snapshotting VMs, deleting snapshots, powering down
#Need to error check if snapshot has the same name as existing snapshot - done


def main():
    #Connect to proxmox
    proxHost = ProxmoxAPI(hostIP, user=apiUser, token_name=tokName, token_value=apiTok, verify_ssl=False)
    #Get proxmox nodes
    nodes = proxHost.nodes.get()
    #Loop through nodes
    vmList = []
    for node in nodes:
        node_name = node['node']
        VMs = proxHost.cluster.resources.get(type='vm')
        #Get list of all VMs
        returnVMList = get_VMs(VMs)
        #Append to the list above
        vmList.extend(returnVMList)

    #Get selected VMs
    print("What VMs are we working with?")
    selectedVMs = vmChoice(vmList)
    validVMs = checkMPLXC(selectedVMs, proxHost)
    print("Selected...")
    for vm in validVMs:
        print(f"{vm[0]} {vm[1]}")
    action = proxActions()
    #Extract value out of returned dict
    action = (list(action.values())[0])
    if action == "Snapshot":
        snapshotVM(validVMs, proxHost)
    elif action == "Delete Snapshot":
        removeSnap(validVMs, proxHost)
    elif action == "Exit":
        sys.exit()










if __name__ == "__main__":
    main()