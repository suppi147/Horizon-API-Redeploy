# Enable Hyper-V feature
dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All

# Set hypervisor launch type to auto
bcdedit /set hypervisorlaunchtype auto

wsl --update

# Reboot the computer
Restart-Computer
