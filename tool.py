import subprocess
import shutil
import os
from colorama import Fore, init
import pyfiglet

init(autoreset=True)


# ============================================================
#                    HAMMAD SECURITY TOOL
# ============================================================

def banner():
    print(Fore.CYAN)
    print(pyfiglet.figlet_format("HAMMAD TOOL", font="slant"))

    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + "       SECURITY SCANNER LAUNCHER")
    print(Fore.YELLOW + "=" * 70)

    print(
        Fore.WHITE
        + "For authorized security testing and your own lab only."
    )

    print(Fore.YELLOW + "=" * 70)


# ============================================================
#                    CHECK SCANNER
# ============================================================

def scanner_installed(scanner):
    return shutil.which(scanner) is not None


def check_scanners():

    scanners = {
        "Nmap": "nmap",
        "Nikto": "nikto",
        "WhatWeb": "whatweb",
        "Nuclei": "nuclei"
    }

    print(Fore.CYAN + "\nSCANNER STATUS")
    print(Fore.CYAN + "=" * 60)

    for name, command in scanners.items():

        if scanner_installed(command):

            print(
                Fore.GREEN
                + "[+] "
                + Fore.WHITE
                + f"{name}: INSTALLED"
            )

        else:

            print(
                Fore.RED
                + "[-] "
                + Fore.WHITE
                + f"{name}: NOT INSTALLED"
            )

    print(Fore.CYAN + "=" * 60)


# ============================================================
#                    RUN COMMAND
# ============================================================

def run_command(command):

    print()
    print(Fore.YELLOW + "Command:")
    print(Fore.WHITE + " ".join(command))

    print(Fore.CYAN + "\n" + "=" * 70)
    print(Fore.GREEN + "SCAN STARTED")
    print(Fore.CYAN + "=" * 70)

    try:

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:

            print(Fore.WHITE + line, end="")

        process.wait()

        print(Fore.CYAN + "\n" + "=" * 70)

        if process.returncode == 0:

            print(
                Fore.GREEN
                + "SCAN COMPLETED"
            )

        else:

            print(
                Fore.RED
                + f"SCAN FINISHED WITH CODE {process.returncode}"
            )

        print(Fore.CYAN + "=" * 70)

    except FileNotFoundError:

        print(
            Fore.RED
            + "\nScanner is not installed."
        )

    except KeyboardInterrupt:

        print(
            Fore.YELLOW
            + "\n\nScan stopped by user."
        )


# ============================================================
#                         NMAP
# ============================================================

def nmap_scanner():

    if not scanner_installed("nmap"):

        print(
            Fore.RED
            + "\nNmap is not installed."
        )

        return

    target = input(
        Fore.YELLOW
        + "\nEnter authorized target IP/hostname: "
    ).strip()

    if not target:

        print(Fore.RED + "Target cannot be empty.")
        return

    print(Fore.CYAN + "\nNMAP OPTIONS")

    print(Fore.WHITE + "[1] Basic scan")
    print(Fore.WHITE + "[2] Service/version detection")
    print(Fore.WHITE + "[3] OS detection")
    print(Fore.WHITE + "[4] Comprehensive lab scan")

    choice = input(
        Fore.YELLOW
        + "\nSelect option: "
    ).strip()

    if choice == "1":

        command = [
            "nmap",
            target
        ]

    elif choice == "2":

        command = [
            "nmap",
            "-sV",
            target
        ]

    elif choice == "3":

        command = [
            "nmap",
            "-O",
            target
        ]

    elif choice == "4":

        command = [
            "nmap",
            "-sV",
            "-O",
            target
        ]

    else:

        print(Fore.RED + "Invalid option.")
        return

    run_command(command)


# ============================================================
#                         NIKTO
# ============================================================

def nikto_scanner():

    if not scanner_installed("nikto"):

        print(
            Fore.RED
            + "\nNikto is not installed."
        )

        return

    target = input(
        Fore.YELLOW
        + "\nEnter authorized web target URL: "
    ).strip()

    if not target:

        print(Fore.RED + "Target cannot be empty.")
        return

    command = [
        "nikto",
        "-h",
        target
    ]

    run_command(command)


# ============================================================
#                         WHATWEB
# ============================================================

def whatweb_scanner():

    if not scanner_installed("whatweb"):

        print(
            Fore.RED
            + "\nWhatWeb is not installed."
        )

        return

    target = input(
        Fore.YELLOW
        + "\nEnter authorized website URL: "
    ).strip()

    if not target:

        print(Fore.RED + "Target cannot be empty.")
        return

    command = [
        "whatweb",
        target
    ]

    run_command(command)


# ============================================================
#                         NUCLEI
# ============================================================

def nuclei_scanner():

    if not scanner_installed("nuclei"):

        print(
            Fore.RED
            + "\nNuclei is not installed."
        )

        return

    target = input(
        Fore.YELLOW
        + "\nEnter authorized web target: "
    ).strip()

    if not target:

        print(Fore.RED + "Target cannot be empty.")
        return

    command = [
        "nuclei",
        "-u",
        target
    ]

    run_command(command)


# ============================================================
#                      SCANNER MENU
# ============================================================

def scanner_menu():

    while True:

        print(Fore.CYAN + "\n" + "=" * 70)
        print(Fore.GREEN + "                 SCANNER MENU")
        print(Fore.CYAN + "=" * 70)

        print(Fore.WHITE + "[1] Nmap")
        print(Fore.WHITE + "[2] Nikto")
        print(Fore.WHITE + "[3] WhatWeb")
        print(Fore.WHITE + "[4] Nuclei")
        print(Fore.WHITE + "[5] Scanner Status")
        print(Fore.RED + "[6] Back")

        choice = input(
            Fore.CYAN
            + "\nHAMMAD-TOOL > "
        ).strip()

        if choice == "1":

            nmap_scanner()

        elif choice == "2":

            nikto_scanner()

        elif choice == "3":

            whatweb_scanner()

        elif choice == "4":

            nuclei_scanner()

        elif choice == "5":

            check_scanners()

        elif choice == "6":

            break

        else:

            print(
                Fore.RED
                + "\nInvalid option."
            )

        input(
            Fore.YELLOW
            + "\nPress ENTER to continue..."
        )


# ============================================================
#                         MAIN MENU
# ============================================================

def main():

    while True:

        banner()

        print(Fore.GREEN + "[1] Start Scanner")
        print(Fore.YELLOW + "[2] Check Installed Scanners")
        print(Fore.RED + "[3] Exit")

        choice = input(
            Fore.CYAN
            + "\nHAMMAD-TOOL > "
        ).strip()

        if choice == "1":

            scanner_menu()

        elif choice == "2":

            check_scanners()

            input(
                Fore.YELLOW
                + "\nPress ENTER to continue..."
            )

        elif choice == "3":

            print(
                Fore.GREEN
                + "\nThank you for using HAMMAD TOOL."
            )

            break

        else:

            print(
                Fore.RED
                + "\nInvalid option."
            )


# ============================================================
#                         START
# ============================================================

if __name__ == "__main__":
    main()
