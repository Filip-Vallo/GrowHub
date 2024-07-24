# RASPBERRY PI OS CONFIGURATION LOG
_Project: **GrowHub**_ <br/>
_Executed: **2024-07-22** on **Raspberry Pi 4 Model B Rev 1.2** (processor BCM2711, revision c03112) with 4GB RAM_ <br/><br/>

## 1. Installation of Raspberry Pi OS
Source: https://www.raspberrypi.com/documentation/computers/os.html <br/><br/>
1. [ ] **Download last version of Raspberry Pi OS (64-bit) image from https://raspberrypi.com/software/operating-systems/** <br/> 
_Used version: with desktop and no recommended software from 2024-07-04: Linux kernel 6.6.31, Debian version 12 (bookworm)_ <br/><br/>
2. [ ] **Download last version of Raspberry Pi Imager from https://www.raspberrypi.com/software/** <br/>
_Used version: 1.8.5_ <br/><br/>
3. [ ] **Use Raspberry Pi Imager to flash image of Raspberry Pi OS (64-bit) to microSD card** <br/><br/>
4. [ ] **Insert microSD card with Raspberry Pi OS image into Raspberry Pi microSD slot** <br/><br/>
5. [ ] **Connect monitor and peripheral devices (keyboard, mouse) to Raspberry Pi unit** <br/><br/>
6. [ ] **Connect Raspberry Pi unit to power source** <br/><br/>
7. [ ] **Turn on the Raspberry Pi unit and follow the installation instructions of Raspberry Pi OS** <br/><br/>
8. [ ] **Connect Raspberry Pi to local network (same as development workstation)** <br/><br/>
9. [ ] **Update all packages installed on Raspberry Pi to their latest versions and remove obsolete ones**<br/>
`sudo apt update` <br/>
`sudo apt full-upgrade` <br/>
_... type_ `Y` _when prompted for confirmation and press_ `Enter` <br/><br/>


## 2. Firmware Update of Raspberry Pi
Source: https://www.raspberrypi.com/documentation/computers/os.html#upgrade-your-firmware <br/><br/>
1. [ ] **Update the firmware of Raspberry Pi** <br/>
    * _... to the latest stable version:_ <br/>
    `sudo apt install --reinstall raspi-firmware` <br/>
    * _... to the latest version (not safe):_ <br/>
    `sudo rpi-update` <br/><br/>
2. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 3. Bios Update of Raspberry Pi
Source: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-boot-eeprom
1. [ ] **Update the EEPROM bootloader (bios) of Raspberry Pi to the latest version** <br/>
`sudo apt update` <br/>
`sudo rpi-eeprom-update -a` <br/><br/>
2. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 4. SSH Connection to Raspberry Pi
Source: https://www.raspberrypi.com/documentation/computers/remote-access.html#access-a-remote-terminal-with-ssh <br/><br/>

### 4.1 Enable the SSH server on Raspberry Pi
1. [ ] **Create an empty file named ssh in the boot partition** <br/>
`sudo touch /boot/firmware/ssh` <br/> <br/>
2. [ ] **Create folder named .ssh inside the user folder** <br/>
_<user_folder_path> = path to user folder of Raspberry Pi OS account to connect as from remote computer_ <br/>
`mkdir <user_folder_path>/.ssh ` <br/> <br/>
3. [ ] **Create empty file named authorized_keys inside the .ssh folder** <br/> 
`touch <user_folder_path>/.ssh/authorized_keys` <br/> <br/>
4. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>

### 4.2 Configure SSH keypair on remote computer
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
_id_rsa = contains private SSH key (keep secure on the computer used to remotely connect to the Raspberry Pi)_ <br/>
_id_rsa.pub = contains public SSH key (share this key with Raspberry Pi to verify identity)_ <br/>
_<user_folder_path> = path to user folder of remote user on remote computer_
   * _on Linux_: <br/>
   `ls <user_folder_path>/.ssh` <br/>
   * _on Windows 10_: <br/>
   `dir <user_folder_path>\.ssh\ ` <br/><br/>

### 4.3 Add remote user's public SSH key to the list of trusted SSH identities on Raspberry Pi
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
   _... enter_ `<password>` _of Raspberry Pi OS user account to connect as, when prompted for password_ <br/><br/><br/>

### 4.4 Connect to Raspberry Pi's SSH server from remote computer (now without password)
1. [ ] **Find the IP address of Raspberry Pi (from Raspberry Pi's terminal)** <br/>
`hostname -I` <br/><br/>
2. [ ] **Connect to Raspberry Pi (from remote computer's terminal)** <br/>
_<user_name> = user name of Raspberry Pi OS account to connect as_ <br/>
_<ip_address> = IP address of Raspberry Pi to connect to_ <br/>
`ssh <user_name>@<ip_address>` <br/>
_... type_ `yes` _when prompted with security warning (first ssh only) and press_ `Enter`<br/><br/>


## 5. Raspberry Pi Configuration
Sources: <br/>
https://www.raspberrypi.com/documentation/computers/configuration.html#non-interactive-raspi-config <br/>
https://www.raspberrypi.com/documentation/computers/configuration.html#device-trees-overlays-and-parameters <br/>
https://www.raspberrypi.com/documentation/computers/configuration.html#part3 <br/>
https://www.raspberrypi.com/documentation/computers/configuration.html#configure-uarts <br/>
https://www.raspberrypi.com/documentation/computers/config_txt.html#enable_uart <br/><br/>

### 5.1 Enable necessary communication interfaces
_by default all non-essential communication interfaces and their kernel modules are disabled on Raspberry Pi_ <br/>
1. [ ] **Backup the configuration file of Raspberry Pi** <br/>
`sudo cp /boot/firmware/config.txt /boot/firmware/config_backup.txt` <br/><br/>
2. [ ] **Enable serial port interface** <br/>
`sudo raspi-config nonint do_rgpio 0` <br/><br/>
3. [ ] **Enable I2C (Inter-Integrated Circuit) & SMB interfaces with i2c-1 bus** <br/>
_I2C (Inter-Integrated Circuit) =  synchronous, multi-controller/multi-target, single-ended communication protocol for exchanging serial data_ <br/>
_SMB (System Management Bus) = simple single-ended, two-wire communication protocol for exchanging serial data (ancestor of I2C)_ <br/>
_i2c-1 bus = general purpose user-mode I2C & SMB bus located on pins 3 (SDA) and 5 (SCL)_ <br/>
`sudo raspi-config nonint do_i2c 0` <br/>
`sudo sh -c "echo -n '\n#Enable i2c-1 bus \ndtparam=i2c-1=on\n' >> /boot/firmware/config.txt"` <br/><br/>
4. [ ] **Enable UART (ttyS0) interface** <br/>
_UART (Universal Asynchronous Receiver/Transmitter) = simple, two-wire communication protocol for exchanging serial data with shared clock_ <br/>
`sudo sh -c "echo -n '\n#Enable the primary/console UART (ttyS0) interface \nenable_uart=1\n' >> /boot/firmware/config.txt"` <br/><br/>
5. [ ] **Enable remote access to the GPIO pins** <br/>
`sudo raspi-config nonint do_rgpio 0` <br/><br/>
6. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>
7. [ ] **Check for existing i2c-1 file inside the dev folder to confirm enabled i2c-1 bus** <br/>
_/dev/i2c-1 = file that manages i2c-1 bus on Raspberry Pi_ <br/>
`ls -la /dev/i2c-1` <br/><br/>
   * _... if the i2c-1 file does not exist:_ 
    1. [ ] **Manually load needed kernel modules and recheck after restart** <br/>
   `modprobe i2c-bcm2835` <br/>
   `modprobe i2c-dev` <br/>
   `sudo reboot` <br/><br/>
8. [ ] **Check the list of functionalities implemented by i2c-1 bus** <br/>
_(SMBus block read, SMBus block process call can be disabled; all the rest should be enabled)_ <br/>
`i2cdetect -F 1` <br/><br/>

### 5.2 Grant root access to i2c-1 bus
_/dev/i2c-1 = file that manages i2c-1 bus on Raspberry Pi (some python libraries need it to have root access to Raspberry Pi OS)_ <br/>
1. [ ] **Search for existing udev rules for i2c-dev kernel module** <br/>
`grep -Rnw '/etc/udev/rules.d' -e 'i2c-dev'` <br/><br/>
   * _... if there are no results found:_ <br/>
   1. [ ] **Append appropriate rule for i2c-dev kernel module to 99-com.rules file** <br/>
   `sudo sh -c "echo -n '\nSUBSYSTEM==\"i2c-dev\", MODE=\"0660\"' >> /etc/udev/rules.d/99-com.rules"` <br/><br/>
   * _... if there are results found:_ 
   1. [ ] **Check if the rules for i2c-dev kernel module match the line ...** <br/>
   `SUBSYSTEM=="i2c-dev", MODE="0660"` <br/><br/>
      * _... if any of the i2c-dev rules doesn't match:_
      1. [ ] **Fix each mismatched rule manually in each individual udev .rules file** <br/>
      _<file_name>  = file name of udev .rules file with incorrect rule_ <br/>
      `sudo nano /etc/udev/rules.d/<rules_file_name>` <br/><br/>
2. [ ] **Set access privileges of all udev .rules files with rules for i2c-dev kernel module** <br/>
`sudo chmod 0666  /etc/udev/rules.d/<rules_file_name>` <br/><br/>
3. [ ] **Create system user group named i2c (if non-existent)** <br/>
`sudo groupadd -f -r i2c` <br/><br/>
4. [ ] **Add user name of logged-in Raspberry Pi OS account to the i2c group** <br/>
_<user_name> = user name of Raspberry Pi OS account_ <br/>
`sudo usermod -a -G i2c <user_name>` <br/><br/>
5. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>

### 5.3 Grant root access to GPIO pins
_/dev/gpiomem = file that manages GPIO pins on Raspberry Pi (some python libraries need it to have root privileges)_ <br/>
1. [ ] **Search for existing udev rules for gpio kernel modules** <br/>
`grep -Rnw '/etc/udev/rules.d' -e 'gpio'` <br/><br/>
   * _... if there are no results found:_ <br/>
   1. [ ] **Append appropriate rules for gpio kernel modules to 99-com.rules file** <br/>
   `sudo sh -c "echo -n '\nSUBSYSTEM==\"*gpiomem*\", GROUP=\"gpio\", MODE=\"0660\"' >> /etc/udev/rules.d/99-com.rules"` <br/>
   `sudo sh -c "echo -n '\nSUBSYSTEM==\"gpio\", GROUP=\"gpio\", MODE=\"0660\"' >> /etc/udev/rules.d/99-com.rules"` <br/><br/>
   * _... if there are results found:_ 
   1. [ ] **Check if the rules for gpio kernel modules match the lines ...** <br/>
   `SUBSYSTEM=="*gpiomem*", GROUP="gpio", MODE="0660"` <br/>
   `SUBSYSTEM=="gpio", GROUP="gpio", MODE="0660"` <br/><br/>
      * _... if any of the gpio rules doesn't match:_
      1. [ ] **Fix each mismatched rule manually in each individual udev .rules file** <br/>
      _<file_name>  = file name of udev .rules file with incorrect rule_ <br/>
      `sudo nano /etc/udev/rules.d/<rules_file_name>` <br/><br/>
2. [ ] **Set access privileges of all udev rules files with rules for gpio kernel module** <br/>
`sudo chmod 0666  /etc/udev/rules.d/<rules_file_name>` <br/><br/>
3. [ ] **Create system user group named gpio (if non-existent)** <br/>
`sudo groupadd -f -r gpio` <br/><br/>
4. [ ] **Add user name of logged-in Raspberry Pi OS account to the gpio group** <br/>
_<user_name> = user name of Raspberry Pi OS account_ <br/>
`sudo usermod -a -G gpio <user_name>` <br/><br/>
5. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 6. Installation of GrowHub's Dependencies on Raspberry Pi
Sources: <br/>
https://www.python.org/ <br/>
https://realpython.com/installing-python/#how-to-build-python-from-source-code <br/>
https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3 <br/>
https://packaging.python.org/en/latest/overview/ <br/>
https://pipx.pypa.io/stable/docs/ <br/>
https://virtualenv.pypa.io/en/latest/ <br/>
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 <br/>
https://pip.pypa.io/en/stable/user_guide/ <br/><br/>

### 6.1 Alt-install custom version of Python to avoid overwriting system Python
1. [ ] **Install packages needed for Python's successful build creation from source code** <br/>
`sudo apt-get update` <br/>
`sudo apt-get upgrade` <br/>
`sudo apt-get install -y make build-essential openssl libssl-dev wget curl llvm xz-utils` <br/>
`sudo apt-get install -y python3-setuptools python3-pip python3-smbus2 tk-dev zlib1g-dev` <br/>
`sudo apt-get install -y libbz2-dev libc6-dev libdb5.3-dev libexpat1-dev libffi-dev libgdbm-dev` <br/>
`sudo apt-get install -y liblzma-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev   ` <br/><br/>
2. [ ] **Download Python 3.9.19 (XZ compressed source tarball) from https://www.python.org/downloads/source/** <br/>
`wget -P $HOME/Downloads https://www.python.org/ftp/python/3.9.19/Python-3.9.19.tar.xz` <br/><br/>
3. [ ] **Extract downloaded Python's source code** <br/>
`tar -xvf $HOME/Downloads/Python-3.9.19.tar.xz` <br/><br/>
4. [ ] **Configure extracted Python to autoinstall pip, use optimizations, and be installed to /opt/python-3.9.19** <br/>
_/usr/local/bin = default path where altinstall command places executables when prefix is not configured_ <br/>
_/opt/python-3.9.19 = path where we configured altinstall command to place executables with --prefix flag_ <br/>
`cd $HOME/Downloads/Python-3.9.19` <br/>
`./configure --enable-optimizations --with-ensurepip=install --prefix=/opt/python-3.9.19` <br/><br/>
5. [ ] **Build Python from source code using make command with 4 parallel processes to speed it up** <br/>
`make -j 4` <br/><br/>
6. [ ] **Alt-install Python to avoid overwriting system Python** <br/>
`sudo make altinstall` <br/><br/>
7. [ ] **Verify successful alt-installation of Python** <br/>
`export PATH=/opt/python-3.9.19/bin:$PATH` <br/><br/>
`python3.9 --version` <br/>
`ls -ls /opt/python-3.9.19/bin/python3.9` <br/><br/>

### 6.2 Create project folder for GrowHub's codebase deployment written in Python
1. [ ] **Create project folder named GrowHub inside $HOME/Projects** <br/>
`cd $HOME` <br/>
`mkdir Projects` <br/>
`cd Projects` <br/>
`mkdir GrowHub` <br/><br/>
2. [ ] **Add $HOME/Projects/GrowHub folder to $PATH of terminal's (bash) .profile file** <br/>
_.profile file is not read by bash if .bash_profile or .bash_login files exist in $HOME directory_ <br/>
`sudo sh -c "echo -n '\n#Project GrowHub \nexport PATH=\"\$PATH:\$HOME/Projects/GrowHub\"\n' >> $HOME/.profile"` <br/><br/>

### 6.3 Create isolated Python virtual environment for GrowHub project 
1. [ ] **Install pipx tool that allows to install and manage python packages (smarter pip)** <br/>
`sudo apt install pipx` <br/>
`pipx ensurepath` <br/>
`eval "$(register-python-argcomplete pipx)"` <br/><br/>
2. [ ] **Install virtualenv that allows to create isolated Python environments** <br/>
`pipx install virtualenv` <br/><br/>
3. [ ] **Verify successful installation of virtualenv** <br/>
`virtualenv --help` <br/><br/>
4. [ ] **Create Python virtual environment for GrowHub project named venv** <br/>
`cd $HOME/Projects/GrowHub`
`virtualenv -p /opt/python-3.9.19/bin/python3.9 venv` <br/><br/>
5. [ ] **Verify successful creation of Python virtual environment by activating it** <br/>
`source venv/bin/activate` <br/>
`which python` <br/>
`python --version` <br/>
`deactivate` <br/>
`which python` <br/>
`python --version` <br/><br/>
6. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>

### 6.4 Install needed python libraries for GrowHub project
1. [ ] **Activate GrowHub's virtual environment and verify its correct path and version** <br/>
`cd $HOME/Projects/GrowHub`
`source venv/bin/activate` <br/>
`which python` <br/>
`python --version` <br/><br/>
2. [ ] **Update pip tool that allows to install and manage python packages** <br/>
`python -m pip install --upgrade pip` <br/><br/>
3. [ ] **List python libraries that are already installed in GrowHub's virtual environment** <br/>
`python -m pip list` <br/><br/>
4. [ ] **Install remaining python libraries needed for GrowHub project into its virtual environment** <br/>
`pip install setuptools wheel docutils python-dateutil` <br/>
`pip install smbus3 RPi.GPIO pigpio bme680` <br/><br/>
5. [ ] **List outdated python libraries in GrowHub's virtual environment** <br/>
`python -m pip list --outdated` <br/><br/>
   * _... if there are any outdated libraries:_ <br/>
   1. [ ] **Update outdated python libraries** <br/>
   pip install --upgrade `pip list --outdated | awk 'NR>2 {print $1}'` <br/><br/>

### 6.5 Installation of needed software tools for GrowHub project



