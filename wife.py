from scapy.all import srp, Ether, ARP

target_ip = '190.168.1.2/24'
# IP address for destination
#create ARP packet

arp = ARP(pdst=target_ip)
#create the Ether broadcast packet

#ff:ff:ff:ff:ff:ff Mac address indicates broadcasting

ether = Ether(dst='ff:ff:ff:ff:ff:ff')
#stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill in this loop
clients = []

for sent, received in result:
    #for each response, append ip and mac address to "cllient" list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Avail devices in network:")
print("IP"+" "*18+"MAC")

for client in clients:
    print("{:16} {}".format(client["ip"],client['mac']))
#proce = subprocess.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)

#while True:
#    line = proce.stdout.readline()
#    if not line:
#        break
#    connected_ip = line.decode('utf-8').split()[3]

#    if connected_ip == IP_DEVICE:
#        subprocess.Popen(['say', 'Wife is hoome, hide the girl!'])