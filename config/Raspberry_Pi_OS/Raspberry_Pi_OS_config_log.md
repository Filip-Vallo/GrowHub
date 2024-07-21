# RASPBERRY PI OS CONFIGURATION LOG
(installed on **Raspberry Pi 4 B with 4GB RAM**) <br/><br/>

## 1. Installation of Raspberry Pi OS
source: https://www.raspberrypi.com/documentation/computers/os.html
1. [ ] **Download Raspberry Pi OS (64-bit) image from https://raspberrypi.com/software/operating-systems/** 
<br/> (version without recommended software) <br/><br/>
2. [ ] **Download Raspberry Pi Imager from https://www.raspberrypi.com/software/** <br/><br/>
3. [ ] **Use Raspberry Pi Imager to flash image of Raspberry Pi OS (64-bit) to microSD card** <br/><br/>
4. [ ] **Insert microSD card with Raspberry Pi OS image into Raspberry Pi microSD slot** <br/><br/>
5. [ ] **Connect monitor and peripheral devices (keyboard, mouse) to Raspberry Pi unit** <br/><br/>
6. [ ] **Connect Raspberry Pi unit to power source** <br/><br/>
7. [ ] **Turn on the Raspberry Pi unit and follow the installation instructions of Raspberry Pi OS** <br/><br/>
8. [ ] **Connect Raspberry Pi to local network (same as development workstation)** <br/><br/>
9. [ ] **Update all packages installed on Raspberry Pi to their latest versions**<br/>
`sudo apt update` <br/>
`sudo apt full-upgrade` <br/><br/>
10. [ ] **Reboot the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 2. SSH Connection to Raspberry Pi
source: https://www.raspberrypi.com/documentation/computers/remote-access.html

### 2.1 Enable the SSH server on Raspberry Pi
1. [ ] **Create an empty file named ssh in the boot partition** <br/>
`sudo touch /boot/firmware/ssh` <br/> <br/>
2. [ ] **Create folder named .ssh inside the user folder** <br/>
_<user_folder_path> = path to user folder of Raspberry Pi OS account to connect as from remote computer_ <br/>
`mkdir <user_folder_path>/.ssh ` <br/> <br/>
3. [ ] **Create empty file named authorized_keys inside the .ssh folder** <br/> 
`touch <user_folder_path>/.ssh/authorized_keys` <br/> <br/>
4. [ ] **Reboot the Raspberry Pi** <br/>
`sudo reboot`

### 2.2 Connect to Raspberry Pi's SSH server from remote computer
1. [ ] **Find the IP address of Raspberry Pi (from Raspberry Pi's terminal)** <br/>
`hostname -I` <br/><br/>
2. [ ] **Connect to Raspberry Pi (from remote computer's terminal)** <br/>
_<user_name> = user name of Raspberry Pi OS account to connect as_ <br/>
_<ip_address> = IP address of Raspberry Pi to connect to_ <br/>
`ssh <user_name>@<ip_address>` <br/>
_... type_ `yes` _when prompted with security warning_ <br/>
_... enter_ `<password>` _of Raspberry Pi OS user account to connect as, when prompted for password_

### 2.3 Configure SSH keypair of remote computer
1. [ ] **Check for existing remote user's SSH keys on remote computer  (from remote computer's terminal)** <br/>
_<user_folder_path> = path to user folder of remote user on remote computer_
   * _on Linux_: <br/>
   `ls <user_folder_path>/.ssh` <br/>
   * _on Windows 10_: <br/>
   `dir <user_folder_path>\.ssh\ ` <br/><br/>
2. [ ] **Generate new SSH keypair for remote user on remote computer (if not already generated)** <br/>
`ssh-keygen` <br/> 
_... when prompted for location, press_ `Enter` _to use the default location_ `<user_folder_path>/.ssh/id_rsa` <br/>
_... when prompted for optional keyphrase, press_ `Enter` _to use no keyphrase_ <br/><br/>
3. [ ] **Recheck for existing remote user's SSH keys on remote computer to confirm the successful generation of _id_rsa_ and _id_rsa.pub_ files** <br/>
_<user_folder_path> = path to user folder of remote user on remote computer_ <br/>
_id_rsa = contains private SSH key (keep secure on the computer used to remotely connect to the Raspberry Pi)_ <br/>
_id_rsa.pub = contains public SSH key (share this key with Raspberry Pi to verify identity)_ 
   * _on Linux_: <br/>
   `ls <user_folder_path>/.ssh` <br/>
   * _on Windows 10_: <br/>
   `dir <user_folder_path>\.ssh\ ` <br/>

### 2.4 Add remote user's public SSH key to the list of trusted SSH identities of Raspberry Pi
1. [ ] **Start the SSH agent on remote computer (from remote computer's terminal or PowerShell as administrator)**
   * _on Linux_: <br/>
   `eval "$(ssh-agent -s)"` <br/>
   * _on Windows 10 (use Windows PowerShell)_: <br/>
   `Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service` <br/>
   `start-ssh-agent.cmd` <br/><br/>
2. [ ] **Add remote user's SSH identities to ssh-agent on remote computer (from remote computer's terminal as administrator)** <br/>
_<user_folder_path> = path to user folder of remote user on remote computer_
   * _on Linux_: <br/>
   `ssh-add <user_folder_path>/.ssh/id_rsa` <br/>
   * _on Windows 10_: <br/>
   `ssh-add <user_folder_path>\.ssh\id_rsa` <br/> <br/>
3. [ ] **Copy remote user's public SSH key to Raspberry Pi (from remote computer's terminal as administrator)** <br/>
_<user_folder_path> = path to user folder of remote user on remote computer_ <br/>
_<user_name>  = user name of Raspberry Pi OS account to connect as_ <br/>
_<ip_address> = IP address of Raspberry Pi to connect to_
   * _on Linux_: <br/>
   `ssh-copy-id <username>@<ip address>`
   * _on Windows 10_: <br/>
   `type <user_folder_path>\.ssh\id_rsa.pub | ssh <username>@<ip address> "cat >> .ssh/authorized_keys"` <br/>
   _... enter_ `<password>` _of Raspberry Pi OS user account to connect as, when prompted for password_ <br/><br/>


## 3. Raspberry Pi Configuration
source: https://www.raspberrypi.com/documentation/computers/configuration.html

### 3.1 Enable Raspberry Pi's communication interfaces
1. [ ] **Backup the configuration file of Raspberry Pi** <br/>
`sudo cp /boot/firmware/config.txt /boot/firmware/config_backup.txt` <br/><br/>
2. [ ] **Enable serial port interface** <br/>
`sudo raspi-config nonint do_rgpio 0` <br/><br/>
3. [ ] **Enable I2C (Inter-Integrated Circuit) protocol interface used by connected sensors** <br/>
`sudo raspi-config nonint do_i2c 0` <br/>
`sudo sh -c "echo -n '\n#Enable i2c-1 bus \ndtparam=i2c-1=on\n' >> /boot/firmware/config.txt"` <br/><br/>
4. [ ] **Enable UART (ttyS0) protocol interface** <br/>
`sudo sh -c "echo -n '\n#Enable the primary/console UART (ttyS0) interface \nenable_uart=1\n' >> /boot/firmware/config.txt"` <br/><br/>
5. [ ] **Enable remote access to the GPIO pins** <br/>
`sudo raspi-config nonint do_rgpio 0` <br/><br/>
6. [ ] **Reboot the Raspberry Pi** <br/>
`sudo reboot`

### 3.2 Add missing kernel modules for the i2c bus
1. [ ] **Load the necessary kernel modules** <br/>
`sudo cp /boot/firmware/config.txt /boot/firmware/config_backup.txt` <br/><br/>

### 3.3 Grant root access to I2C protocol
_/dev/i2c-1 = file that manages I2C protocol on Raspberry Pi (some python libraries need it to have root privileges)_
1. [ ] **Create user device rule file named 99-i2c.rules inside rules folder** <br/>
`sudo nano /etc/udev/rules/99-i2c.rules` <br/>
`sudo sh -c "echo -n 'SUBSYSTEM=="i2c-dev", MODE="0660"' >> /etc/udev/rules/99-i2c.rules"` <br/><br/>


## 4. Installation of Dependencies
source: https://www.raspberrypi.com/documentation/computers/configuration.html

### 3.1 Enable Raspberry Pi's communication interfaces