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

install:
	$(APTUPD)
	$(APT) python3 python3-venv
	sudo -H pip3 install --upgrade pip

clean:
