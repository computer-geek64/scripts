# Scripts
*December 25th, 2018*

Useful command-line scripts for Linux

## Getting Started
Install a Linux or Unix operating system (preferrably [Kali Linux](https://www.kali.org/)).

### Prerequisites
1. Install and update packages
```bash
sudo -i
apt-get update --fix-missing -y
apt-get dist-upgrade -y
apt-get install gnome-screensaver wmctrl -y
apt-get autoremove -y
apt-get clean -y
```
2. Install Python 3.6 (if not already installed)
```bash
apt-get install python3 -y
```
3. Install Python packages (optional, Python scripts already have an automatic dependency installation feature)
```bash
pip install PACKAGE; pip3 install PACKAGE
```

## Installation
Clone or download the repository
* Clone repository: `git clone https://github.com/computer-geek64/accessible-virtual-keyboard/`
* Download repository: `wget https://github.com/computer-geek64/accessible-virtual-keyboard/archive/master.zip`
	* Extract repository: `unzip master.zip`

### Deployment
* Before executing the program, ensure that the shebang exists at the start of each script (usually `#!/bin/bash` or `#!/usr/bin/python3`)
* Always ensure that the line endings are compatible with the operating system that you are using.
* If a warning message surfaces regarding `pip`, upgrade pip with the following command: `python -m pip install --upgrade pip; python3 -m pip install --upgrade pip`

## Execution
Execute each script directly or by using the interpreter command. Example (Python 3.6): `./Main.py` or `python3 Main.py`

## Built With 
* Software:
* [Python](https://www.python.org/) - *Primary project language*
	* [gTTS](https://pypi.org/project/gTTS/) - *Google Text-to-Speech*
	* IDE: [JetBrains](https://www.jetbrains.com/pycharm/) - *High-end integrated development environment for Python*
	* Shell: [GNU Bash](https://www.gnu.org/software/bash/) - *Open-source Bourne Again Shell*

## Contributing
Please read the [CONTRIBUTING.md](/docs/CONTRIBUTING.md) file for details on our code of conduct and pull request policy.

## Versioning
This project uses [git](https://git-scm.com/) version control.

## Sources
See the [sources.md](/docs/sources.md) file for information gathered to help create this project.

## Developers
* **Ashish D'Souza** - *Sole developer* - [computer-geek64](https://github.com/computer-geek64/)

See also the list of [contributors](/docs/CONTRIBUTORS.md) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgment
* This project would not have been possible without open-source
