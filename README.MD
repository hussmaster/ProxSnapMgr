# Proxmox Snapshot Manager

This will utilize the python package **proxmoxer**. This is a community maintained package but it is on the official API Proxmox wiki.

The primary functionality of this project is the ability to manage snapshots of resources. Snapshotting multiple VMs/LXCs quickly as well as snapshot removal. 

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
