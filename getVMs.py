from prompts import vmChoice
from lxcCheck import checkMPLXC

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
        vmNode = {vm['node']}.pop()
        if templateStatus != 1:
            #Append tuple of each VM to the VM list
            vmTup = (vmID, vmName, vmType, vmStatus, vmNode)
            vmlist.append(vmTup)
    return vmlist
            
#Function to get list of resources to work with
def listVMChoice(vmList, proxHost):
    print("What resources are we working with?")
    selectedVMs = vmChoice(vmList)
    #Removes any LXCs with invalid mount points
    validVMs = checkMPLXC(selectedVMs, proxHost)
    print("Selected...")
    for vm in validVMs:
        print(f"{vm[0]} {vm[1]}")
    return validVMs