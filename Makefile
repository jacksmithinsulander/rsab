APT             := sudo apt install
APTUPD          := sudo apt update && sudo apt upgrade
PIP3            := pip3 install
SYSTEMD_ENABLE  := sudo systemctl enable
SYSTEMD_DISABLE := sudo systemctl disable
SYSTEMD_START   := sudo systemctl start
SYSTEMD_STOP    := sudo systemctl stop
SYSTEMD_RELOAD  := sudo systemctl daemon-reload
SYSTEMD_RESTART := sudo systemctl restart
RMV             := sudo rm -rf
ROOT_CP         := sudo cp
PIP_RMV         := pip3 uninstall -y
RBT             := echo "rebooting now, ssh back in 5 minutes :)" && sudo reboot
PY              := python3
VENV            := virtualenv
BOT_DIR         := ${HOME}/rsab
BOT_PATH        := ${HOME}/rsab/main.py
BRCPTH          := ${HOME}/.bashrc

install:
	$(APTUPD)
	$(APT) python3 python3-virtualenv
	sudo -H pip3 install --upgrade pip
	$(VENV) .rsab_venv
	. $(BOT_DIR)/.rsab_venv/bin/activate
	$(PIP3) $(BOT_DIR)/requirements.txt
	echo "alias rsab=$(BOT_PATH)" >> $(BRCPTH)
	source $(BRCPTH)
	chmod +x $(BOT_PATH)

clean:

init:
	
