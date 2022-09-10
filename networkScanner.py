import scapy.all as scapy
import optparse
from pyfiglet import Figlet
from printy import printy
from termcolor import colored
import sys


def get_user_inputs():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="Enter IP Adress!")


    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        printy("You Must Enter IP Address! ",'rBU')
        printy("[yD]Usage #python3 networkScanner.py -i 172.20.10.3/24@")
        sys.exit(0)
    return user_input

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip) # arp request to destination ip 
    #scapy.ls(scapy.ARP()) --> show help 
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # broadcast packet
    combined_packet = broadcast_packet/arp_request_packet # prepared my packet to send 

    
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1) # i used timeout=1 cuz i wanna use faster than program

    answered_list.summary()

def get_banner():
    f = Figlet(font='slant')
    print(colored(f.renderText("Hy3n4"),'yellow'))

if __name__ == '__main__':
    get_banner()
    user_ip_address = get_user_inputs()
    scan_network(user_ip_address.ip_address)
