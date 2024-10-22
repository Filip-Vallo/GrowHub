# RASPBERRY PI OS CONFIGURATION
_Project: **GrowHub**_ <br/>
_Tested: **2024-07-22** on **Raspberry Pi 4 Model B Rev 1.2** (processor BCM2711, revision c03112) with 4GB RAM_ <br/><br/>



## 1. Installation of Raspberry Pi OS
___
Source: <br/>
[1]: https://www.raspberrypi.com/documentation/computers/os.html <br/>
___

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
___
Source: <br/>
[2]: https://www.raspberrypi.com/documentation/computers/os.html#upgrade-your-firmware <br/>
___

1. [ ] **Update the firmware of Raspberry Pi** <br/>
    * _... to the latest stable version:_ <br/>
    `sudo apt install --reinstall raspi-firmware` <br/>
    * _... to the latest version (not safe):_ <br/>
    `sudo rpi-update` <br/><br/>
2. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 3. Bios Update of Raspberry Pi
___
Source: <br/>
[3]: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-boot-eeprom <br/>
___

1. [ ] **Update the EEPROM bootloader (bios) of Raspberry Pi to the latest version** <br/>
`sudo apt update` <br/>
`sudo rpi-eeprom-update -a` <br/><br/>
2. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 4. SSH Connection to Raspberry Pi
___
Source: <br/>
[4]: https://www.raspberrypi.com/documentation/computers/remote-access.html#access-a-remote-terminal-with-ssh <br/>
___

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
_<username>  = username of Raspberry Pi OS account to connect as_ <br/>
_<ip_address> = IP address of Raspberry Pi to connect to_
   * _on Linux_: <br/>
   `ssh-copy-id <username>@<ip address>`
   * _on Windows 10_: <br/>
   `type <user_folder_path>\.ssh\id_rsa.pub | ssh <username>@<ip address> "cat >> .ssh/authorized_keys"` <br/>
   _... enter_ `<password>` _of Raspberry Pi OS user account to connect as, when prompted for password_ <br/><br/>

### 4.4 Connect to Raspberry Pi's SSH server from remote computer (now without password)
1. [ ] **Find the IP address of Raspberry Pi (from Raspberry Pi's terminal)** <br/>
`hostname -I` <br/><br/>
2. [ ] **Connect to Raspberry Pi (from remote computer's terminal)** <br/>
_<username> = username of Raspberry Pi OS account to connect as_ <br/>
_<ip_address> = IP address of Raspberry Pi to connect to_ <br/>
`ssh <username>@<ip_address>` <br/>
_... type_ `yes` _when prompted with security warning (first ssh only) and press_ `Enter`<br/><br/>


## 5. Raspberry Pi Configuration
___
Sources: <br/>
[5]: https://www.raspberrypi.com/documentation/computers/configuration.html#non-interactive-raspi-config <br/>
[6]: https://www.raspberrypi.com/documentation/computers/configuration.html#device-trees-overlays-and-parameters <br/>
[7]: https://www.raspberrypi.com/documentation/computers/configuration.html#part3 <br/>
[8]: https://www.raspberrypi.com/documentation/computers/configuration.html#configure-uarts <br/>
[9]: https://www.raspberrypi.com/documentation/computers/config_txt.html#enable_uart <br/>
___

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
4. [ ] **Add username of logged-in Raspberry Pi OS account to the i2c group** <br/>
_<username> = username of Raspberry Pi OS account_ <br/>
`sudo usermod -a -G i2c <username>` <br/><br/>
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
4. [ ] **Add username of logged-in Raspberry Pi OS account to the gpio group** <br/>
_<username> = username of Raspberry Pi OS account_ <br/>
`sudo usermod -a -G gpio <username>` <br/><br/>
5. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>


## 6. Installation of GrowHub's Dependencies on Raspberry Pi
___
Sources: <br/>
[10]: https://realpython.com/installing-python/#how-to-build-python-from-source-code <br/>
[11]: https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3 <br/>
[12]: https://pipx.pypa.io/stable/docs/ <br/>
[13]: https://virtualenv.pypa.io/en/latest/ <br/>
[14]: https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 <br/>
[15]: https://packaging.python.org/en/latest/overview/ <br/>
[16]: https://pip.pypa.io/en/stable/user_guide/ <br/>
[17]: https://learn.pimoroni.com/article/getting-started-with-bme680-breakout <br/>
[18]: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi <br/>
[19]: https://files.atlas-scientific.com/pi_sample_code.pdf <br/>
[20]: https://docs.influxdata.com/influxdb/v2/api-guide/client-libraries/python/ <br/>
[21]: https://abyz.me.uk/rpi/pigpio/download.html <br/>
[22]: https://www.geeksforgeeks.org/crontab-in-linux-with-examples/ <br/>
[23]: https://docs.influxdata.com/influxdb/v2/install/?t=Raspberry+Pi#install-influxdb-as-a-service-with-systemd <br/>
___

### 6.1 Alt-install custom version of Python to avoid overwriting system Python <br/> 
Sources: _[[10](https://realpython.com/installing-python/#how-to-build-python-from-source-code)], [[11](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3)]_
1. [ ] **Install packages needed for Python's successful build creation from source code** <br/>
`sudo apt update` <br/>
`sudo apt upgrade` <br/>
`sudo apt-get install -y make build-essential python3-setuptools python3-pip wget curl xz-utils` <br/>
`sudo apt-get install -y openssl libssl-dev tk-dev llvm python3-smbus2` <br/>
`sudo apt-get install -y libbz2-dev libc6-dev libdb5.3-dev libexpat1-dev libffi-dev libgdbm-dev zlib1g-dev` <br/>
`sudo apt-get install -y liblzma-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev` <br/><br/>
2. [ ] **Download Python 3.9.19 (XZ compressed source tarball) from https://www.python.org/downloads/source/** <br/>
`wget -P $HOME/Downloads https://www.python.org/ftp/python/3.9.19/Python-3.9.19.tar.xz` <br/><br/>
3. [ ] **Extract downloaded source code to $HOME//Downloads** <br/>
`tar -xvf $HOME/Downloads/Python-3.9.19.tar.xz -C $HOME//Downloads` <br/><br/>
4. [ ] **Configure extracted Python to autoinstall pip, use optimizations, and be installed to /opt/python-3.9.19** <br/>
_/usr/local/bin = default path where altinstall command places executables when prefix is not configured_ <br/>
_/opt/python-3.9.19 = path where we configured altinstall command to place executables with --prefix flag_ <br/>
`cd $HOME/Downloads/Python-3.9.19` <br/>
`./configure --enable-optimizations --with-ensurepip=install --prefix=/opt/python-3.9.19` <br/><br/>
5. [ ] **Build Python from source code using 4 parallel processes to speed it up** <br/>
`make -j 4` <br/><br/>
6. [ ] **Alt-install Python from build to avoid overwriting system Python** <br/>
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
Sources: _[[12](https://pipx.pypa.io/stable/docs/)], [[13](https://virtualenv.pypa.io/en/latest/)], [[14](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)]_
1. [ ] **Install pipx tool that allows to install and manage python packages (smarter pip)** <br/>
`sudo apt-get install -y pipx` <br/>
`pipx ensurepath` <br/>
`eval "$(register-python-argcomplete pipx)"` <br/><br/>
2. [ ] **Install virtualenv that allows to create isolated Python environments** <br/>
`pipx install virtualenv` <br/><br/>
3. [ ] **Verify successful installation of virtualenv** <br/>
`virtualenv --help` <br/><br/>
4. [ ] **Create Python virtual environment for GrowHub project named venv** <br/>
`cd $HOME/Projects/GrowHub` <br/>
`virtualenv -p /opt/python-3.9.19/bin/python3.9 venv` <br/><br/>

### 6.4 Install needed python packages (libraries) in virtual environment
Sources: _[[15](https://packaging.python.org/en/latest/overview/)], [[16](https://pip.pypa.io/en/stable/user_guide/)], [[17](ttps://learn.pimoroni.com/article/getting-started-with-bme680-breakout)], [[18](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)], [[19](https://files.atlas-scientific.com/pi_sample_code.pdf)], [[20](https://docs.influxdata.com/influxdb/v2/api-guide/client-libraries/python/)]_
1. [ ] **Activate GrowHub's virtual environment and verify its correct path and version** <br/>
`cd $HOME/Projects/GrowHub` <br/>
`source venv/bin/activate` <br/>
`which python` <br/>
`python --version` <br/><br/>
2. [ ] **Update pip tool that allows to install and manage python packages** <br/>
`python -m pip install --upgrade pip` <br/><br/>
3. [ ] **List python libraries that are already installed in GrowHub's virtual environment** <br/>
`python -m pip list` <br/><br/>
4. [ ] **Install python libraries for core functionality** <br/>
`pip install --upgrade setuptools wheel typing` <br/><br/>
5. [ ] **Install python libraries for communication with Raspberry Pi interfaces** <br/>
`pip install --upgrade smbus3 RPi.GPIO pigpio` <br/><br/>
6. [ ] **Install python libraries for communication with sensors** <br/>
`pip install --upgrade bme680 adafruit-circuitpython-seesaw atlas-i2c` <br/><br/>
7. [ ] **Install python database libraries** <br/>
`pip install --upgrade influxdb-client` <br/><br/>
8. [ ] **Install python utility libraries** <br/>
`pip install --upgrade docutils python-dateutil` <br/><br/>
9. [ ] **List outdated python libraries in GrowHub's virtual environment** <br/>
`python -m pip list --outdated` <br/><br/>
   * _... if there are any outdated libraries:_ <br/>
   1. [ ] **Update outdated python libraries** <br/>
   pip install --upgrade `pip list --outdated | awk 'NR>2 {print $1}'` <br/><br/>
10. [ ] **Deactivate GrowHub's virtual environment** <br/>
`deactivate` <br/><br/>

### 6.5 Install needed OS packages with APT
Sources: _[[17](ttps://learn.pimoroni.com/article/getting-started-with-bme680-breakout)], [[18](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)], [[19](https://files.atlas-scientific.com/pi_sample_code.pdf)]_
1. [ ] **Install git distributed revision control system that also allows to fetch a project or package from GitHub** <br/>
`sudo apt-get install -y git git-lfs` <br/><br/>
2. [ ] **Install software packages for core functionality** <br/>
`sudo apt-get install -y python3-setuptools cmake` <br/><br/>
3. [ ] **Install software packages for communication with Raspberry Pi interfaces** <br/>
`sudo apt-get install -y python3-rpi.gpio rpi.gpio-common i2c-tools` <br/><br/>
4. [ ] **Install software packages for communication with sensors** <br/>
`sudo apt-get install -y libgpiod-dev python3-libgpiod` <br/><br/>
5. [ ] **Install needed utility software packages** <br/>
`sudo apt-get install -y mtools dosfstools gettext` <br/><br/>

### 6.6 Manually install pigpio as a service with pigpiod daemon
Sources: _[[21](https://abyz.me.uk/rpi/pigpio/download.html)], [[22](https://www.geeksforgeeks.org/crontab-in-linux-with-examples/)]_ <br/>
_pigpio installed with apt doesn't support remote access_ <br/>
1. [ ] **Download last version of pigpio from https://github.com/joan2937/pigpio** <br/>
`wget -P $HOME/Downloads https://github.com/joan2937/pigpio/archive/master.zip` <br/><br/>
2. [ ] **Extract downloaded source code to $HOME/Downloads** <br/>
`unzip $HOME/Downloads/master.zip -d $HOME/Downloads` <br/><br/>
3. [ ] **Build pigpio from source code** <br/>
`cd $HOME/Downloads/pigpio-master` <br/>
`make` <br/><br/>
4. [ ] **Install pigpio with pigpiod daemon from build** <br/>
`sudo make install` <br/>
_... automatically installs pigpiod daemon and creates a systemd service file `/lib/systemd/system/pigpiod.service`_ <br/><br/>
5. [ ] **Create root cron job to autostart pigpiod daemon on system boot** <br/>
`sudo crontab -e` <br/>
_... type `1` and press `Enter` when run for the first time to edit with Nano editor_ <br/>
_... add `@reboot              /usr/local/bin/pigpiod` to the end of the crontab file and save_ <br/>
_... Ctrl + O to save / Ctrl + X to exit_ <br/><br/>
6. [ ] **Verify successful creation of cron job for root user** <br/>
`sudo crontab -l -u root` <br/><br/>
7. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>
8. [ ] **Verify successful autostart of pigpiod daemon on system boot** <br/>
`sudo pigpiod -v` <br/><br/>

### 6.7 Manually install firmware for Pimoroni BME680 Breakout
Sources: _[[17](https://learn.pimoroni.com/article/getting-started-with-bme680-breakout)]_
1. [ ] **Clone last version of firmware for Pimoroni BME680 Breakout from https://github.com/pimoroni/bme680-python** <br/>
`sudo git clone https://github.com/pimoroni/bme680-python /opt/bme680` <br/><br/>
2. [ ] **Activate GrowHub's virtual environment and verify its correct path and version** <br/>
`cd $HOME/Projects/GrowHub` <br/>
`source venv/bin/activate` <br/>
`which python` <br/>
`python --version` <br/><br/>
3. [ ] **Install firmware for the sensor in GrowHub's virtual environment** <br/>
`cd /opt/bme680` <br/>
`./install.sh` <br/><br/>
4. [ ] **Deactivate GrowHub's virtual environment** <br/>
`deactivate` <br/><br/>
5. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>

### 6.8 Manually download firmware for Atlas Scientific EZO Circuit(s)
Sources: _[[19](https://learn.pimoroni.com/article/getting-started-with-bme680-breakout)]_
1. [ ] **Clone last version of firmware for Atlas Scientific EZO Circuit(s) from https://github.com/AtlasScientific/Raspberry-Pi-sample-code** <br/>
`sudo git clone https://github.com/AtlasScientific/Raspberry-Pi-sample-code /opt/AtlasScientific_EZO` <br/><br/>

### 6.9 Manually install InfluxDB database as a service with influxd daemon
Sources: _[[23](https://docs.influxdata.com/influxdb/v2/install/?t=Raspberry+Pi#install-influxdb-as-a-service-with-systemd)]_
1. [ ] **Download InfluxData repository for Debian ARM 64-bit (APT keyring file) from https://www.influxdata.com/downloads/** <br/>
`wget -q https://repos.influxdata.com/influxdata-archive_compat.key` <br/><br/>
2. [ ] **Sign downloaded InfluxData APT keyring file with line of code provided on download web page** <br/>
 `echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null` <br/><br/>
3. [ ] **Add signed InfluxData repository to APT** <br/>
`echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list` <br/><br/>
4. [ ] **Install InfluxDB** <br/>
`sudo apt-get update` <br/>
`sudo apt-get install -y influxdb2` <br/>
_... automatically installs influxd daemon and creates a systemd service file `/lib/systemd/system/influxdb.service`_ <br/><br/>
5. [ ] **Start the InfluxDB service** <br/>
`sudo service influxdb start` <br/><br/>
6. [ ] **Restart the Raspberry Pi** <br/>
`sudo reboot` <br/><br/>
7. [ ] **Verify successful autostart of influxd daemon on system boot** <br/>
`sudo service influxdb status` <br/>
_... press `Q` to quit_ <br/><br/>


# 7. Detection of Raspberry Pi Devices
___

1. [ ] **List all detected I2C devices connected to Raspberry Pi** <br/>
`sudo i2cdetect -y 1` <br/>
_... verify there are connected I2C devices on following addresses:_ <br/>
`0x36 (54)` _= Adafruit STEMMA Soil Sensor_ <br/>
`0x63 (99)` _= Atlas Scientific EZO pH Circuit_ <br/>
`0x64 (100)` _= Atlas Scientific EZO Conductivity Circuit_ <br/>
`0x76 (118)` _= Pimoroni BME680 Breakout_ <br/><br/>
