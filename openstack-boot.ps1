# Enable Hyper-V feature
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor

# Set hypervisor launch type to auto
bcdedit /set hypervisorlaunchtype off

wsl --shutdown

# Reboot the computer
Restart-Computer
