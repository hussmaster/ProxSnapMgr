from proxmoxer import ProxmoxAPI
from prompts import snapName
import time

def snapshotVM(VMlist, proxNode):
    snapShotName = snapName()
    #Extract snapshot name from returned dict
    snapShotName = (list(snapShotName.values())[0])
    for vm in VMlist:
        #Check if it's a vm or lxc
        if vm[2] == 'qemu':
            try:
                proxNode.nodes(vm[4]).qemu(vm[0]).snapshot.post(snapname=snapShotName, vmstate=1)
                print(f"Snapshot {snapShotName} created successfully on {vm[1]}")
            except Exception as e:
                print(f"Failed to create snapshot for: {e}")
        elif vm[2] == 'lxc':
            try:
                proxNode.nodes(vm[4]).lxc(vm[0]).snapshot.post(snapname=snapShotName)
                print(f"Snapshot {snapShotName} created successfully on {vm[1]}")
            except Exception as e:
                print(f"Failed to create snapshot for: {e}")
        #Used to slow for storage
        time.sleep(2)