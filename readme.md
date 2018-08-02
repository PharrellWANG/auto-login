# Automate Network Access Control Login

## You Might Not Need This Project

If you are not in CityU, or if you don't use the wired network in CityU, 
you do not need this project.

## Motivation

Every day before we can access the internet via CS wired network, a login form needs to be submitted in the browser. 
Even if you can use the auto-fill function of Safari or Chrome to assist with the login process, 
it is still **tedious** for you to click that **Secure Login** button and to wait few seconds.

We want the network login process to happen automatically.

## Features

1. Automate login process for **CityU CS Network Access Control**. No need to click a button for submitting form.
2. Execute a command to logout. (Though the logic behind ``logout.py`` is simple).

## Requirements

* macOS or Linux
* python3.6

## Install

### macOS
1. Clone the project to a suitable location, e.g., your home directory ``/Users/USERNAME/``. 
```
git clone https://github.com/PharrellWANG/auto-login.git
```
> You will need to keep this project in your file system. To uninstall, just delete the project folder.

2. Install Selenium to automate browsers. ``pip install selenium``

3. ``brew install jq``

4. Download and install ``geckodriver`` for Firefox. 

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-macos.tar.gz
tar -zxvf geckodriver-v0.21.0-macos.tar.gz && rm -rf geckodriver-v0.21.0-macos.tar.g
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin
```
### Ubuntu 18.04 LTS
1. Clone the project to a suitable location, e.g., your home directory ``/home/USERNAME/``.
```
git clone https://github.com/PharrellWANG/auto-login.git
```
> You will need to keep this project in your file system. To uninstall, just delete the project folder.

2. Install Selenium to automate browsers. ``pip install selenium``

3. Download and install ``geckodriver`` for Firefox. 

You can check the latest release of geckodriver from [here](https://github.com/mozilla/geckodriver/releases).

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
tar -zxvf geckodriver-v0.21.0-linux64.tar.gz && rm -rf geckodriver-v0.21.0-linux64.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin
```

## Usage

Step 1: in project root directory, ``touch credential.txt``, then open ``credential.txt`` with your favorite editor, type **your eid** in the first line, press enter, then type your password in the second line, save it. Modify ``login.py`` to provide right path for ``credential.txt``. ``login.py`` will need to fetch your credential from this file.

Step 2: For macOS users, modify ``auto-login.command`` to provide right path; for Linux users, modify ``auto-login.sh`` to provide right path.

Step 3: Make command file executable: ``chmod +x auto-login.command`` or ``chmod +x auto-login.sh``.

Step 4: Automatically execute it upon reboot: ``crontab -e``, then add ``@reboot /path/to/auto-login.command``. Replace ``/path/to/auto-login.commands`` with appropriate path. Alternatively, you can add ``auto-login.command`` to login items in macOS. For Linux users, replace ``.command`` with ``.sh``.

## Outcome
Every time you reboot the computer, you can directly access www.google.com.hk. There's no need to submit a login form any more.

## Caveat
Please keep your ``credential.txt`` secretly, since it shall contain your credentials.

## Author
Pharrell Z.X. WANG (*wzxnuaa@gmail.com*)

## License
MIT
