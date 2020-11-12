import subprocess
import schedule

# This command is executed in cmd to clean temp file
cmd = "DEL /F /S /Q %TEMP%"
output = subprocess.call(cmd,shell=1)


    