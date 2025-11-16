from proxmoxer import ProxmoxAPI
from snapProps import getSnaps
from prompts import removeSnapChoice

#TODO
#Setup remove snapshot logic
#Implement 
#Maybe use this? # Get the list of snapshots for the VM
#snapshots = proxmox.nodes('node_name').qemu(vm_id).snapshot.get()
#This works ^ just need to pass in node name, vm ID

#Removes snapshot
def removeSnap(VMList, proxHost):

    for vm in VMList:
        vmID = vm[0]
        vmName = vm[1]
        vmType = vm[2]
        proxNode = vm[4]

        snaps = getSnaps(proxHost, vmID, vmType, proxNode)
        #Remove 'current' snapshot name, not a valid snapshot
        snaps.remove('current')
        #Prompt displaying all snaps for current VM
        #implement logic, maybe while loop, to wait for snapshot name
        #to be gone from snapshot list. Can't delete two snaps at the 
        # same time
        snapChoice = removeSnapChoice(vmName, snaps)
        print(snapChoice)