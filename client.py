# coding=utf-8
import wmi
import psutil
from uptime import uptime
import os
comp = wmi.WMI()
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

def get_host_info(Windows=False):

    def get_uptime():
        return uptime()

    def get_mem():
        return str(psutil.virtual_memory().percent)

    def get_cpu():
        """

        :return: float
        """
        return str(psutil.cpu_percent())

    host_info = {'host': "",
                 'uptime': get_uptime(),
                 'memory': get_mem(),
                 'cpu': get_cpu(),
                 }
    return host_info
