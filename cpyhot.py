import subprocess
import time
import pathlib

cmd = "mount |grep gvfs"
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print((p_path := output.decode().split(" ")[2]))

cmd2 = "find " + p_path + " -name DCIM"
ps2 = subprocess.Popen(cmd2,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
output2 = ps2.communicate()[0]
output1 = str(output2).rstrip()

output = "/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_98893936524e315953/Phone/DCIM"

print(output)
print(output1)
print(len(output))
print(len(output1))

def find_files(output2):
    a_start = time.perf_counter()
    vd = []
    print(f"Start file lookup")
    for file in pathlib.Path(output).rglob("*.jpg"):
        try:
            if file.is_file():
                vd.append(file)
                print (file.name)
        except PermissionError:
            print("Permission Error")
            continue
        except FileNotFoundError:
            print("Not found error")
            continue

    print(f"End file lookup : {time.perf_counter() - a_start:.1f} seconds")
    print(f"Found : {len(vd)} files")
    return vd


result = find_files(output2)
