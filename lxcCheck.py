from proxmoxer import ProxmoxAPI

#Ingests list and checks if it's an lxc
#If lxc, check if it has a mount point
def checkMPLXC(VMlist, proxHost):
    returnList = []
    for vm in VMlist:
        #If it's a standard qemu VM, keep.
        if vm[2] == 'qemu':
            returnList.append(vm)
        else:
            # Fetch the configuration of the LXC container
            config = proxHost.nodes(vm[4]).lxc(vm[0]).config.get()
            mpCount = 0
            mpValue = {}
            ##Iterate over config dict and check if 'mp' is a key
            for k, v in config.items():
                #If LXC has a mount point change the found count to 1
                if 'mp' in k:
                    mpCount += 1
                    mpValue[k] = v
            #If no mount points are found, append the LXC to the return list
            if mpCount == 0:
                returnList.append(vm)
            else:
                print(f"Removed {vm[1]} from list as it has a mount point at {(list(mpValue.values())[0])}")
                print("Cannot take snapshots of LXCs with a mount point unless you remove, snap, re-add")
    print(returnList)
    input()
    return returnList