# coding=utf-8
import wmi
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