# Proxmox Snapshot Manager

Mostly writing this to get comfy with Python. This will utilize the python package **proxmoxer**. This is a community maintained package but it is on the official API Proxmox wiki.

I'd like to utilize this package to create an interface to be able to select X number of VMs or LXCs and snapshot them all with the same name. And then have the ability to remove X number of those snapshots. Could be all, could just be one.


### Requirements

```
pip install -r requirements.txt
```

Also need a proxmox API key 
[Create API Token](https://kenwardtown.com/2024/06/25/create-an-api-token-for-proxmox-ve/)

.env file with 

```
API_TOKEN = "<api token>"
HOST = "<host ip>"
API_USER = "<username@pve>"
TOKEN_NAME = "<token name>"
```
