import subprocess
import time
import pathlib
import os
import shutil
import sys

# Leave this as False unless you want to see debug output. Mostly print statements
ifDebug = False

# This script is used to copy files from a connected phone to a local directory
# It uses the gvfs-mount command to find the phone if it's connected. If there isn't a phone connected, it will exit
cmd = "mount |grep gvfs"
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0]

#  Check if there is a phone connected. If output is null, then it never saw a connected device in the system call
if not output:
    print("No connected phones found")
    exit()

# This is the path to the phone's DCIM directory
p_path = output.decode().split(" ")[2]

if ifDebug: print(p_path)

# This will now use the gvfs path to find any DCIM directories on the phone. That's where we are lookng for new pictures
cmd2 = "find " + p_path + " -name DCIM"
ps2 = subprocess.Popen(cmd2,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
output2 = ps2.communicate()[0]
output1 = str(output2).rstrip()

# Below is a example of what the output variable will look like. It will vary based on the phone and the number of DCIM directories
#output = "/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_98893936524e315953/Phone/DCIM"

# Args. If you don't pass arg1 it will default to the home directory. If you don't pass arg2 it will default to 5 seconds
# You must pass arg1 if you want to pass arg2
# You MUST have the directory created underneath the user's home directory. It will not create the directory for you
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

if ifDebug: print(interval)


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
        # We do the pathing and copying in the same loop. This is to avoid having to loop through the files twice
        # We could also use the resultant array to do the copying but right now it's not used
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

# For testing. If you only want one iteration, uncomment the line below but be sure to comment out the while loop
#result = find_files(output2)

while True:
    result = find_files(output2)
    print("Interval complete")
    time.sleep(int(interval))
