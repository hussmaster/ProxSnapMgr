from proxmoxer import ProxmoxAPI
from snapProps import getSnaps
from prompts import removeSnapChoice
import time

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

        snapChoice = removeSnapChoice(vmName, snaps)
        #Extract snap choice from dict
        snapChoice = (list(snapChoice.values())[0])
        if vmType == 'qemu':
            try:
                proxHost.nodes(proxNode).qemu(vmID).snapshot(snapChoice).delete()
                #Loop to check when snapshot has been removed
                while snapChoice in snaps:
                    print(f"Removing '{snapChoice}' from {vmName}...")
                    time.sleep(2)
                    snaps = getSnaps(proxHost, vmID, vmType, proxNode)
                    #Remove 'current' snapshot name, not a valid snapshot
                    snaps.remove('current')
                print(f"Removed snapshot '{snapChoice}' from {vmName}")
            except Exception as e:
                print(f"Failed to remove snapshot for: {e}")
        elif vmType == 'lxc':
            try:
                proxHost.nodes(proxNode).lxc(vmID).snapshot(snapChoice).delete()
                #Loop to check when snapshot has been removed
                while snapChoice in snaps:
                    print(f"Removing '{snapChoice}' from {vmName}...")
                    time.sleep(2)
                    snaps = getSnaps(proxHost, vmID, vmType, proxNode)
                    #Remove 'current' snapshot name, not a valid snapshot
                    snaps.remove('current')
                print(f"Removed snapshot '{snapChoice}' from {vmName}")
            except Exception as e:
                print(f"Failed to remove snapshot for: {e}")

