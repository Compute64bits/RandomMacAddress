from os import system
from random import choice
from psutil import net_if_addrs
from time import sleep

# random mac
mac = ''.join(choice('0123456789ABCDEF')for _ in'x'*12)

print("Modifying mac...")

# edit mac address
system('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\\0001" '+ f'/v NetworkAddress /d {mac} /f')

# restart all ethernet/bluetooh cards
for name in list(net_if_addrs().keys()):
    system(f'netsh interface set interface "{name}" admin=disable')
    system(f'netsh interface set interface "{name}" admin=enable')
  
sleep(10)
print("Mac modified!")
