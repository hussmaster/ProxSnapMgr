from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI
import requests, os, inquirer
from getVMs import *
from prompts import *

load_dotenv()

apiTok = os.environ.get("API_TOKEN")
hostIP = os.environ.get("HOST")
apiUser = os.environ.get("API_USER")
tokName = os.environ.get("TOKEN_NAME")


#TODO
#Setup ENV with proxmox api key - done
#Verify connectivity with Proxmox - done
#Try and pull some details from a VM - done
#Come up with selection for actions ie. snapshotting VMs, deleting snapshots, powering down


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
        returnVMList = get_VMs(VMs)
        vmList.extend(returnVMList)

    #Get selected VMs
    selectedVMs = vmChoice(vmList)
    print(selectedVMs)
    for vm in selectedVMs:
        print(vm[0])










if __name__ == "__main__":
    main()