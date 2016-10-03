# coding=utf-8
import wmi
comp = wmi.WMI()
http://timgolden.me.uk/python/wmi/cookbook.html - документация на wmi
for i in comp.Win32_ComputerSystem():
   print i.TotalPhysicalMemory, "bytes of physical memory"

for os in comp.Win32_OperatingSystem():
   print os.FreePhysicalMemory, "bytes of available memory"
uptime = 'systeminfo | find "System Boot Time:"'
memory = ''
cpu_info = ''