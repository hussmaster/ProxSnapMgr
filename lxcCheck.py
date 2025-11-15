from proxmoxer import ProxmoxAPI

#Ingests list and checks if it's an lxc
#If lxc, check if it has a mount point
def checkMPLXC(VMlist, proxHost):
    returnList = []

    for vm in VMlist:
        print(vm)
        if vm[2] == 'qemu':
            returnList.append(vm)
        else:
            # Fetch the configuration of the LXC container
            config = proxHost.nodes(vm[4]).lxc(vm[0]).config.get()
            print(config)
            input()
            #Iterate over config dict and check if 'mp' is a key
    print(returnList)
    input()