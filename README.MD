# Proxmox Snapshot Manager

This will utilize the python package **proxmoxer**. This is a community maintained package but it is on the official API Proxmox wiki.

The primary functionality of this project is the ability to manage snapshots of resources. Snapshotting multiple VMs/LXCs quickly as well as snapshot removal. When doing maintenance in my homelab I like to do updates on multiple machines at once so I wanted a way to quickly do this rather than go through the GUI one at a time. I also wanted the ability to only remove snapshots from certain VMs after updating. 

## Requirements

```
pip install -r requirements.txt
```

Or pip install the following

- dotenv
- inquirer
- proxmoxer

You will also need to proxmox API key 
[Create API Token](https://kenwardtown.com/2024/06/25/create-an-api-token-for-proxmox-ve/)

.env file with 

```
API_TOKEN = "<api token>"
HOST = "<host ip>"
API_USER = "<username@pve>"
TOKEN_NAME = "<token name>"
```

## Installation

To setup and use this project:

1. Clone the repository:

```
git clone https://github.com/hussmaster/ProxSnapMgr
```

2. Navigate to the project directory:

```
cd ProxSnapMgr
```

3. Create a .env file in the root of the directory. Use the .env.example file as a guide. 

## Running the program

After cloning the repository, installing the required python packages, and editing the .env file. You can run the program in two ways

1. Make main.sh exectuable and run the main.sh script
```
chmod +x main.sh
./main.sh
```
2. Or you can run the python program directly
```
python3 src/main.py
```

## Screenshots

Selection Screen

![Selection Screen](/screenshots/selections.png)

Resource selection

![Resource Selection](/screenshots/snapshot.png)

Snapshot creation

![Snapshot Name](/screenshots/snapshotname.png)

Removing snapshot

![Remove Snapshot](/screenshots/removesnap.png)


