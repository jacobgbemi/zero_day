# Vagrant Installation on Window

### Installation Steps
- Download VirtualBox from this [link](https://www.virtualbox.org/wiki/Downloads)
- Install VirtualBox
- Download Vagrant from this [link](https://www.vagrantup.com/downloads)
- Install Vagrant
- Open the Window Terminal ([Command Prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089)) and do the following:
  - Add the Ubuntu 20.04 (Focal) image to your box list: ```> vagrant box add ubuntu/focal64```
  - Many other images are available [here](https://app.vagrantup.com/boxes/search)
- Create your first virtual machine: ```> vagrant init ubuntu/focal64```
- Update to the latest version: ```> vagrant plugin install vagrant-vbguest```
- Vagrant init ubuntu/focal64: ```> vagrant up```
- Enter inside your virtual machine: ```> vagrant ssh```
- Start coding
