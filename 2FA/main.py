import os
import sys
import time

def clear_screen():
    'Not for user use. Used by module.'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def install_package(package_name):
    'Not for user use. Used by module.'
    try:
        pip_version = os.system(f"{sys.executable} -m pip --version")
        if pip_version != 0:
            print("pip is not available. Please install pip first.")
            return
    except Exception as e:
        print(f"Error checking pip version: {e}")
        return
    try:
        print(f"Installing {package_name}...")
        install_command = f"{sys.executable} -m pip install {package_name}"
        result = os.system(install_command)
        if result == 0:
            print(f"{package_name} installed successfully.")
        else:
            print(f"Failed to install {package_name}. Exit code: {result}")
    except Exception as e:
        print(f"Error installing package {package_name}: {e}")

try:
  import pyotp
  import configparser
except:
  install_package('pyotp')
  install_package('configparser')

def main():
    'Main Command'
    clear_screen()
    print("Loading 2FA console...")
    time.sleep(0.35)
    print("Gathering info (if any)...")
    time.sleep(0.35)
    config = configparser.ConfigParser()
    configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'twofactorauth.ini')
    if os.path.exists(configfile) and os.stat(configfile).st_size != 0:
        print("Data found.")
        config.read(configfile)
    else:
        print("No old data.")
    time.sleep(0.05)
    print("Starting program...")
    time.sleep(0.05)
    clear_screen()
    print("Welcome to the 2FA Console!")

    def mainoption():
        print("Choose an option")
        print("")
        print("OTP: List of One Time Passwords")
        print("S: Settings")
        print("E: Exit 2FA Console and return to CodeOn console")
        print("")
        option = input("CON 2FA>> ")
        
        if option == "OTP":
            clear_screen()
            otptable = []
            for OTP in config:
                if OTP != "DEFAULT":
                    otptable.append(OTP)
            for OTP in otptable:
                otpname = config[OTP]['name']
                otpsecret = config[OTP]['secret']
                code = pyotp.TOTP(otpsecret).now()
                print(otpname)
                print(code)
                print("")
            print("30 seconds, until returning to main screen.")
            time.sleep(30)
            mainoption()
        elif option == "S":
            clear_screen()
            print("Create/Delete accounts.")
            print("Choose an option:")
            print("")
            print("C: Create an account")
            print("D: Delete an account")
            print("")
            option2 = input("CON 2FA>> ")
            if option2 == "C":
                clear_screen()
                print("Follow these rules to create an account:")
                print("")
                print("Account name can be anything")
                print("Account secret must be the one given to you from the provider of the authentication key.")
                print("Account type must be HOTP (HMAC-Based) or TOTP (Time-Based)")
                print("If you don't know this, try to create 2 accounts on here, and try one on one and the other on the other.")
                print("Whichever one works, thats the one you want to use.")
                print("Fill out the input forms below.")
                print("")
                name = input("CON 2FA: What do you want the account to be named? ")
                secret = input("CON 2FA: Whats the account secret? ")
                config[str(name)] = {
                    'name': str(name),
                    'secret': secret
                }
                configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'twofactorauth.ini')
                with open(configfile, "w") as configfile:
                    config.write(configfile)
                print("written")
                time.sleep(5)
                clear_screen()
                mainoption()
            elif option2 == "D":
                clear_screen()
                print("Choose an account to delete:")
                print("")
                n = 0
                for account in config:
                    if n == "0":
                        print(f'0: {account}')
                        n = 1
                    else:
                        print(f'{n}: {account}')
                        n = n + 1
                print("")
                doption = input("CON 2FA>> ")
                if doption > len(config):
                    print("Invalid response.")
                    time.sleep(5)
                    clear_screen()
                    mainoption()
                elif doption < len(config):
                    print("Invalid response.")
                    time.sleep(5)
                    clear_screen()
                    mainoption()
                else:
                    try:
                        config[int(doption)].clear()
                        print("Committed Action.")
                        time.sleep(3)
                        clear_screen()
                        mainoption()
                    except:
                        print("Error while committing action.")
                        time.sleep(5)
                        clear_screen()
                        mainoption()
            else:
                print("Invalid option.")
                time.sleep(5)
                clear_screen()
                mainoption()
        elif option == "E":
            pass
        else:
            print("Invalid option.")
            time.sleep(5)
            clear_screen()
            mainoption()

    mainoption()
