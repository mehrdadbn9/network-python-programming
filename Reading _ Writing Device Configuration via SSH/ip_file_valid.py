import os.path
import sys


def ip_file_valid():
    # Prompting user for input
    ip_file = input("\n# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")

    if os.path.isfile(ip_file) == True:
        print(f"it's valid {ip_file}")
    else:
        print(f"{ip_file}it's not a valid ip")
        sys.exit()

    selected_ip_file = open(ip_file,'r')
    selected_ip_file.seek(0)
    ip_list = selected_ip_file.readlines()
    selected_ip_file.close()
    return ip_list