# MCSS (MineCraft Server Setup)
How to create a server very easy without following tutorials? This is **MCSS**.
Works with Python on Linux (but will be expended on every platforms), create a Minecraft server for you and your friends!

## Install
### Dependencies
* Git (`sudo apt install git`)
* Root Access
* Linux (for the moment)
* [Atom Editor](https://atom.io)

### Installation
#### Ubuntu derivative / Debian derivative
Just run the following commands:
```
git clone https://github.com/chopin2712/MCSS
cd MCSS
chmod +x install.sh
sudo sh install.sh
```

## Usage
To use it just run the command: `MCSS`

## Contribute
Of course you can contribute to this project, to make this just read the **CONTRIBUTING.md** file.

## Update
This is how to update your server to the latest version of MCSS:
```
git clone https://github.com/chopin2712/MCSS
cd MCSS
sudo sh install.sh
cd ..
sudo rm -r MCSS
```
If you already installed a server using `MCSS` you can start this last command:
```
sudo cp /opt/MCSS/start.py .
```

## LICENSE
This project is run by GNU public license, see **LICENSE.md** to learn more about it...
