import os
import requests
import sys
from iplogger import run_ip_logger

apikey = 'XXX'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner2():
    print("\n" * 2)
    print(
        "\033[38;2;0;255;0m    ███        ▄████████    ▄████████  ▄████████    ▄█   ▄█▄        ▄█    █▄    ███    █▄     ▄████████    ▄████████\033[0m")
    print(
        "\033[38;2;0;242;64m▀█████████▄   ███    ███   ███    ███ ███    ███   ███ ▄███▀       ███    ███   ███    ███   ███    ███   ███    ███\033[0m")
    print(
        "\033[38;2;0;230;128m   ▀███▀▀██   ███    ███   ███    ███ ███    █▀    ███▐██▀         ███    ███   ███    ███   ███    █▀    ███    ███\033[0m")
    print(
        "\033[38;2;0;214;144m    ███   ▀  ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀         ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀\033[0m")
    print(
        "\033[38;2;0;198;174m    ███     ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄        ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀\033[0m")
    print(
        "\033[38;2;0;183;194m    ███     ▀███████████   ███    ███ ███    █▄    ███▐██▄         ███    ███   ███    ███   ███    █▄  ▀███████████\033[0m")
    print(
        "\033[38;2;0;168;204m    ███       ███    ███   ███    ███ ███    ███   ███ ▀███▄       ███    ███   ███    ███   ███    ███   ███    ███\033[0m")
    print(
        "\033[38;2;0;150;215m   ▄████▀     ███    ███   ███    █▀  ████████▀    ███   ▀█▀       ███    █▀    ████████▀    ██████████   ███    ███\033[0m")
    print(
        "\033[38;2;0;130;235m              ███    ███                           ▀                                                      ███    ███\033[0m")
    print("\n" * 1)


def print_banner():
    print("\n" * 2)
    print("\033[38;2;0;255;0m   ▄█     ▄███████▄ ▄█████████▄    ▄█    █▄    ███    █▄     ▄████████ \033[0m")
    print("\033[38;2;0;242;64m  ███    ███    █████▀       ▄██  ███    ███   ███    ███   ███    ███ \033[0m")
    print("\033[38;2;0;230;128m  ███▌   ███    ███        ▄███▀  ███    ███   ███    ███   ███    █▀  \033[0m")
    print("\033[38;2;0;214;144m  ███▌   ███    ███      ▄███▀   ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄     \033[0m")
    print("\033[38;2;0;198;174m  ███▌ ▀█████████▀     ▄███▀    ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀     \033[0m")
    print("\033[38;2;0;183;194m  ███    ███         ▄███▀        ███    ███   ███    ███   ███    █▄  \033[0m")
    print("\033[38;2;0;168;204m  ███    ███         ███          ███    ███   ███    ███   ███    ███ \033[0m")
    print("\033[38;2;0;150;215m  █▀    ▄████▀       ▀█████████████▀     █▀    ████████▀    ██████████ \033[0m")
    print("\033[38;2;0;130;235m                                                        \033[0m")
    print("\n" * 1)



def print_menu():
    print("\n" * 1)
    print("\033[38;2;0;255;0m        ╔══(1) IP info\033[0m")
    print("\033[38;2;0;255;0m        ║\033[0m")
    print("\033[38;2;0;242;64m        ╠══(2) Proxy Checker\033[0m")
    print("\033[38;2;0;242;64m        ║\033[0m")
    print("\033[38;2;0;230;128m        ╠══(3) ISP and Host info \033[0m")
    print("\033[38;2;0;214;144m        ║\033[0m")
    print("\033[38;2;0;198;174m        ╠══(4) VPN/TOR/Botnet check (Api sucks)\033[0m")
    print("\033[38;2;0;183;194m        ║\033[0m")
    print("\033[38;2;0;168;204m        ╠══(5) IP Grabber \033[0m")
    print("\033[38;2;0;150;215m        ║\033[0m")
    print("\033[38;2;0;130;235m        ╚╦═(6) Exit\033[0m")
    print("\033[38;2;0;130;235m         ║\033[0m")


def fetch_ip_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print("\033[38;2;0;255;0m         ╔════(1) IP info \033[0m")
    print("\033[38;2;0;230;128m         ║ \033[0m")
    ip = input("\033[38;2;0;230;255m         ╚══════> Enter the IP address: \033[0m").strip()
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("\n \033[38;2;0;255;0m    Information for IP {}: \033[0m ".format(ip))
        for key, value in {
            "IP": data.get("ip", "N/A"),
            "Hostname": data.get("hostname", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location": data.get("loc", "N/A"),
            "Organization": data.get("org", "N/A")
        }.items():
            print(f"    \033[38;2;0;230;128m           {key}: \033[38;2;0;150;215m{value}\033[0m")
    except requests.RequestException as e:
        print(f"Error fetching IP info: {e}")
    input("\nPress Enter to return to the menu...")


def host_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print("\033[38;2;0;255;0m         ╔════(3) Isp and Host info \033[0m")
    print("\033[38;2;0;230;128m         ║ \033[0m")
    ip = input("\033[38;2;0;230;255m         ╚══════> Enter the IP address: \033[0m").strip()
    url_h = f"https://api.ip2location.io/?key={apikey}&ip={ip}"
    try:
        response = requests.get(url_h)
        response.raise_for_status()
        data = response.json()
        if "ip" in data:
            print("\n \033[38;2;0;255;0m        Host and ISP related info for IP {}: \033[0m ".format(ip))
            for key, value in {
                "IP": data.get("ip", "N/A"),
                "Autonomous system": data.get("as", "N/A"),
                "AS number": data.get("asn", "N/A"),
                "ISP": data.get("isp", "N/A"),
                "Domain": data.get("domain", "N/A"),
                "Internet speed": data.get("net_speed", "N/A"),
                "Mobile brand": data.get("mobile_brand", "N/A"),
                "Mobile network code": data.get("mnc", "N/A"),
                "Usage type": data.get("usage_type", "N/A"),
                "Address type": data.get("address_type", "N/A"),
                "Ads category": data.get("ads_category", "N/A"),
                "Ads category name": data.get("ads_category_name", "N/A")
            }.items():
                print(f"    \033[38;2;0;230;128m           {key}: \033[38;2;0;150;215m{value}\033[0m")
        else:
            print("Error: Could not retrieve host info. Please check your API key or IP address.")

    except requests.RequestException as e:
        print(f"Error fetching IP info: {e}")

    input("\nPress Enter to return to the menu...")


def proxy_checker():
    os.system('cls')
    print_banner()
    print("\033[38;2;0;255;0m         ╔════(2) Proxy Checker \033[0m")
    print("\033[38;2;0;230;128m         ║ \033[0m")
    proxy_ip = input("\033[38;2;0;230;255m         ╚══════> Enter proxy IP: \033[0m").strip()
    url = f"https://proxycheck.io/v2/{proxy_ip}?vpn=1&asn=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('status') == 'ok' and proxy_ip in data:
            info = data[proxy_ip]
            proxy_type = info.get('type', 'N/A')
            is_proxy = info.get('proxy', 'N/A')
            print(f"\n\033[38;2;0;230;128m            Address type:\033[38;2;0;150;215m {proxy_type} \033[0m")
            print(f"\033[38;2;0;230;128m            Proxy:\033[38;2;0;150;215m {is_proxy} \033[0m")
        else:
            print("Invalid IP address or error retrieving proxy information.")
    except requests.RequestException as e:
        print(f"Error with the proxy: {e}")

    input("\nPress Enter to return to the menu...")


def bot_check():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print("\033[38;2;0;255;0m         ╔════(4) VPN or Botnet Check (Api sucks and gives wrong results) \033[0m")
    print("\033[38;2;0;230;128m         ║ \033[0m")
    ip = input("\033[38;2;0;230;255m         ╚══════> Enter the IP address: \033[0m").strip()
    url_h = f"https://api.ip2location.io/?key={apikey}&ip={ip}"

    try:
        response = requests.get(url_h)
        response.raise_for_status()
        data = response.json()

        if "is_proxy" in data:
            proxy_data = data.get("proxy", {})
            print("\n \033[38;2;0;255;0m        VPN/Bot/Tor check for IP {}: \033[0m ".format(ip))
            for key, value in {
                "Proxy": data.get("is_proxy", "no"),
                "threat": proxy_data.get("threat", "no"),
                "TOR": proxy_data.get("is_tor", "no"),
                "Spammer": proxy_data.get("is_spammer", "no"),
                "Scanner": proxy_data.get("is_scanner", "no"),
                "Botnet": proxy_data.get("is_botnet", "no"),
                "Web crawler": proxy_data.get("is_web_crawler", "no"),
                "Data center check": proxy_data.get("is_data_center", "no"),
                "Consumer privacy network": proxy_data.get("is_consumer_privacy_network", "no"),
                "Enterprise private network": proxy_data.get("is_enterprise_private_network", "no")
            }.items():
                print(f"    \033[38;2;0;230;128m           {key}: \033[38;2;0;150;215m{value}\033[0m")
        else:
            print("Error: Could not retrieve info. Please check your API key or IP address.")

    except requests.RequestException as e:
        print(f"Error fetching IP info: {e}")

    input("\nPress Enter to return to the menu...")


def ip_logger():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print("\033[38;2;0;255;0m         ╔════(5) IP Logger \033[0m")
    print("\033[38;2;0;230;128m         ║ \033[0m")
    print("\033[38;2;0;230;255m         ╚══════> Initializing Ngrok tunnel... \033[0m")
    print()
    run_ip_logger()


def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input(" \033[38;2;0;140;225m        ╚══════> \033[0m").strip()
        if choice == "1":
            info = fetch_ip_info()
        elif choice == "2":
            proxy_checker()
        elif choice == "3":
            host_info()
        elif choice == "4":
            bot_check()
        elif choice == "5":
            ip_logger()
        elif choice == "6":
            clear_screen()
            sys.exit()
        else:
            print("Invalid option selected.")
            input("\nPress Enter to try again...")


if __name__ == "__main__":
    main()
