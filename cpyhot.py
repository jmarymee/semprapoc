import subprocess
import time
import pathlib
import os
import shutil
import sys

ifDebug = False

cmd = "mount |grep gvfs"
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0]
if not output:
    print("No connected phones found")
    exit()
#print((p_path := output.decode().split(" ")[2]))
p_path = output.decode().split(" ")[2]

if ifDebug: print(p_path)

cmd2 = "find " + p_path + " -name DCIM"
ps2 = subprocess.Popen(cmd2,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
output2 = ps2.communicate()[0]
output1 = str(output2).rstrip()

#output = "/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_98893936524e315953/Phone/DCIM"

if len(sys.argv) > 1:
    destPathBase = str(pathlib.Path.home()) + os.path.sep + sys.argv[1] + os.path.sep
    if ifDebug: print(destPathBase)
else:
    destPathBase = str(pathlib.Path.home()) + os.path.sep
    if ifDebug: print(destPathBase)

if (len(sys.argv)>2):
    interval = int(sys.argv[2])
else:
    interval = 5

print(interval)


if ifDebug:
    print(output)
    print(output1)
    print(len(output))
    print(len(output1))

def find_files(output2):
    a_start = time.perf_counter()
    vd = []
    print(f"Start file lookup")
    for file in pathlib.Path(output1).rglob("*.jpg"):
        try:
            if file.is_file():
                vd.append(file)
                if ifDebug: print(os.path.abspath(file))
                destPath = destPathBase + file.name
                if ifDebug: print(destPath)
                shutil.copyfile(os.path.abspath(file), destPath)
        except PermissionError:
            print("Permission Error")
            continue
        except FileNotFoundError:
            print("Not found error")
            continue

    print(f"End Iteration : {time.perf_counter() - a_start:.1f} seconds")
    print(f"Found and copied: {len(vd)} files")
    return vd

#result = find_files(output2)
while True:
    result = find_files(output2)
    print("Interval complete")
    time.sleep(int(interval))
