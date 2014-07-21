#Will automagically parse your ip and scan the network with nmap
from sh import nmap, ifconfig

ip = ifconfig("en1")
ip = str(ip.split("\n")[3].split("inet ")[1].split(" netmask")[0])

ip_range = ip.split(".")[0] + "." + ip.split(".")[1] + "." + ip.split(".")[2] + "." + "0/24"

print(nmap(ip_range))