import requests
from pystyle import *
import time
import os
import sys
import folium  # Import folium

night_owl = """
⠀⢀⣤⣶⣶⣶⣶⣾⣶⣶⣄
⠠⢛⣭⣥⣬⣍⣥⣶⣶⣶⣌⢳⡄
⢰⣿⡟⠿⢿⣿⣿⢟⢛⡻⣿⡌⣿⡄
⢸⣿⣿⣭⡈⣿⣿⠌⣩⣾⣿⢃⡘⣷
⠈⠻⣿⣿⣧⠻⡟⣸⣿⡿⢃⣤⣿⣿⣇
⠀⢷⡌⡙⠿⠷⠀⠿⢋⣥⣼⣿⣿⣿⣿⣆
⠀⠘⣿⣿⣼⣶⣾⣦⣿⣿⣿⣿⣿⣿⣿⢿⣆
⠀⠀⢻⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⡆⢿⡄
⠀⠀⠸⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⣿⣿⠘⣷
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡆⢻⣿⣿⡟⢻⣿⣿⡇
⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⡏⣄⢻⣿⣿⡌⢿⣿⣿⡀
⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣧⠻⣿⣿⡌⣿⢿⣇
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣩⣽⣿⣧⠹⣿⣿⡜⠆⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣿⣿⠟⢿⣧⠻⣧⡹⣆⡘⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⢾⡆⣿⡇⣌⠳⡘⢿⣶⡀
⠀⠀⠀⠀⣴⣦⣠⣤⣾⡿⢁⣤⣄⢁⣿⢈⣙⢧⡙⢌⠻⣧
⠀⠀⠀⠀⠁⠘⠉⠛⠛⠁⠃⠈⠛⠻⠻⠟⠻⠈⠛
"""

A = '\033[95m' 

print(A + night_owl)

from pyfiglet import Figlet

def create_colored_ascii_art(name, font='slant', color='red'):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(name)
    
    # ANSI color codes
    color_codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
    }

    # Apply color to the ASCII art
    colored_ascii_art = f"{color_codes[color]}{ascii_art}{color_codes['reset']}"
    
    return colored_ascii_art

name = 'NightOwl'
ascii_art = create_colored_ascii_art(name, color='purple')

print(ascii_art)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        ip_data = response.json()
        return ip_data
    else:
        return None

def print_ip_info(ip_info):
    if ip_info:
        print("IP Information:", A)
        print(f"IP Address: {ip_info['ip']}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"ISP: {ip_info.get('org', 'N/A')}")

        # Create a map with Folium
        location = ip_info.get('loc', '0,0').split(',')
        latitude = float(location[0])
        longitude = float(location[1])
        
        map_obj = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=f"IP: {ip_info['ip']}").add_to(map_obj)
        
        map_file = 'ip_location_map.html'
        map_obj.save(map_file)
        print(f"Map has been saved to {map_file}")

    else:
        print("Unable to retrieve IP information.")

if __name__ == "__main__":
    user_input = Write.Input("Enter an IP address (or press Enter to use your own IP): ", Colors.blue_to_purple).strip()
    
    if not user_input:
        # If no IP is provided, use the public IP of the machine
        response = requests.get("https://ipinfo.io/json")
        user_input = response.json().get('ip', '')

    ip_info = get_ip_info(user_input)
    print_ip_info(ip_info)
    
def restart_script():
    python = sys.executable
    os.execl(python, python, *sys.argv)

restart_tool = True

while restart_tool:
    choice = Write.Input("[1] Go Back \n[2] Exit \n", Colors.blue_to_black).strip()

    if choice == '1':
        Write.Print("Restarting the tool...", Colors.blue_to_black)
        restart_script()
    elif choice == '2':
        Write.Print('Thanks for using the tool \n', Colors.black_to_green)
        print(ascii_art)
        restart_tool = False
    else:
        print("Invalid choice. Please enter 1 to restart or 2 to exit.")
