from proxmoxer import ProxmoxAPI
from prompts import snapName
from snapProps import checkSnap, getSnaps
import time

#Takes snapshot
def snapshotVM(VMlist, proxHost):
    snapShotName = snapName()
    #Extract snapshot name from returned dict
    snapShotName = (list(snapShotName.values())[0])
    for vm in VMlist:
        vmID = vm[0]
        vmName = vm[1]
        vmType = vm[2]
        proxNode = vm[4]
        #Check if it's a vm or lxc
        if vmType == 'qemu':
            #Checks to see if snapshot name already exists
            snapCheck = checkSnap(vmID, vmType, proxNode, proxHost, snapShotName)
            if snapCheck == 1:
                while snapCheck == 1:
                    print(f'Snap name "{snapShotName}" already exists on {vmName}')
                    print('Select a new snapshot name')
                    newSnapName = snapName()
                    newSnapName = (list(newSnapName.values())[0])
                    snapCheck = checkSnap(vmID, vmType, proxNode, proxHost, newSnapName)
                snap(proxHost, vmID, vmType, vmName, newSnapName, proxNode)
            else:
                snap(proxHost, vmID, vmType, vmName, snapShotName, proxNode)
        elif vmType == 'lxc':
            #Checks to see if snapshot name already exists
            snapCheck = checkSnap(vmID, vmType, proxNode, proxHost, snapShotName)
            if snapCheck == 1:
                while snapCheck == 1:
                    print(f'Snap name "{snapShotName}" already exists on {vmName}')
                    print('Select a new snapshot name')
                    newSnapName = snapName()
                    newSnapName = (list(newSnapName.values())[0])
                    snapCheck = checkSnap(vmID, vmType, proxNode, proxHost, newSnapName)
                snap(proxHost, vmID, vmType, vmName, newSnapName, proxNode)
            else:
                snap(proxHost, vmID, vmType, vmName, snapShotName, proxNode)
        #Used to slow for storage
        time.sleep(2)

#Helper function to create snapshot. 
def snap(proxHost, vmID, vmType, vmName, snapName, proxNode):
    currentSnaps = getSnaps(proxHost, vmID, vmType, proxNode)
    if vmType == 'qemu':
        try:
            proxHost.nodes(proxNode).qemu(vmID).snapshot.post(snapname=snapName, vmstate=1)
            #Loop to check when snapshot has been created
            while snapName not in currentSnaps:
                print(f"Creating '{snapName}' snapshot on {vmName}...")
                time.sleep(2)
                currentSnaps = getSnaps(proxHost, vmID, vmType, proxNode)
            print(f"Snapshot '{snapName}' created successfully on {vmName}")
        except Exception as e:
            print(f"Failed to create snapshot for: {e}")
    elif vmType == "lxc":
        try:
            proxHost.nodes(proxNode).lxc(vmID).snapshot.post(snapname=snapName)
            while snapName not in currentSnaps:
                print(f"Creating '{snapName}' snapshot on {vmName}...")
                time.sleep()
                currentSnaps = getSnaps(proxHost, vmID, vmType, proxNode)
            print(f"Snapshot '{snapName}' created successfully on {vmName}")
        except Exception as e:
            print(f"Failed to created snapshot for: {e}")
