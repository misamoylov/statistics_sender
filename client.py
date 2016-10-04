# coding=utf-8
import wmi
import psutil
from uptime import uptime
import os
comp = wmi.WMI('192.168.122.113', user='Administrator', password='TestRoot1')
# http://timgolden.me.uk/python/wmi/cookbook.html - документация на wmi
for i in comp.Win32_ComputerSystem():
   print(i.TotalPhysicalMemory, "bytes of physical memory")
for os in comp.Win32_OperatingSystem():
   print(os.FreePhysicalMemory, "bytes of available memory")


# c = wmi.WMI(privileges=["Security"])
#
# watcher = c.watch_for(
#   notification_type="Creation",
#   wmi_class="Win32_NTLogEvent",
#   Type="error"
# )
# while 1:
#   error = watcher()
#   print "Error in %s log: %s" % (error.Logfile, error.Message)
#   # send mail to sysadmin etc.
# uptime = 'systeminfo | find "System Boot Time:"'
# memory = ''
# cpu_info = ''

def get_uptime():
    return uptime()

def get_mem_linux():
    # sswap(total=2097147904L, used=886620160L, free=1210527744L, percent=42.3, sin=1050411008, sout=1906720768)
    return str(psutil.virtual_memory().percent)

def get_cpu_linux():
    """

    :return: float
    """
    return str(psutil.cpu_percent())
