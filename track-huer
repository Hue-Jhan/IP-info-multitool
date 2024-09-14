import os
import requests
import sys


def print_banner():
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


def print_menu():
    print("\n" * 1)
    print("\033[38;2;0;255;0m        ╔══(1) IP info\033[0m")
    print("\033[38;2;0;255;0m        ║\033[0m")
    print("\033[38;2;0;230;128m        ╠══(2) Proxy Checker\033[0m")
    print("\033[38;2;0;230;255m        ║\033[0m")
    print("\033[38;2;0;198;174m        ╠══(3) IP Grabber (Will add later)\033[0m")
    print("\033[38;2;0;204;255m        ║\033[0m")
    print("\033[38;2;0;168;204m        ╚╦═(4) Exit\033[0m")
    print("\033[38;2;0;168;204m         ║\033[0m")


def fetch_ip_info():
    os.system('cls')
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

        # Extract relevant information
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
           print("not yet cuh")
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid option selected. Please try again.")
            input("\nPress Enter to try again...")


if __name__ == "__main__":
    main()
