

def get_VMs(VMs):
    vmlist = []
    for vm in VMs:
        #Iterate through VMs
        #Pop each value so it's out of it's 'set'
        vmStatus = {vm['status']}.pop()
        vmType = {vm['type']}.pop()
        vmID = {vm['vmid']}.pop()
        vmName = {vm['name']}.pop()
        templateStatus = {vm['template']}.pop()
        print(vm)
        if templateStatus != 1:
            #Append tuple of each VM to the VM list
            vmTup = (vmID, vmName, vmType, vmStatus)
            vmlist.append(vmTup)
    return vmlist
            