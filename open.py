import subprocess
# لیست برنامه هایی که می خواهید باز شوند
programs = ["notepad.exe"]
for program in programs:
    subprocess.Popen(program)