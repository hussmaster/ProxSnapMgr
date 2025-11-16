from proxmoxer import ProxmoxAPI

#Retrieves existing snapshot name
def checkSnap(vmID, vmType, proxNode, proxHost, snapName):
    value = 0
    if vmType == 'qemu':
        snapshots = proxHost.nodes(proxNode).qemu(vmID).snapshot.get()
        for snap in snapshots:
            #If the snapshot name already exists set value to 1
            if snap['name'] == snapName:
                value = 1
    elif vmType == 'lxc':
        snapshots = proxHost.nodes(proxNode).lxc(vmID).snapshot.get()
        for snap in snapshots:
            if snap['name'] == snapName:
                value = 1
    return value