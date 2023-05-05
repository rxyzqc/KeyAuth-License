from keyauth.api import Keyauth
import hashlib
import sys, os
import time

creator = "rxyzqc"


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


client = Keyauth(
    name="",
    owner_id="",
    secret="",
    version="",
    file_hash=getchecksum()
)


# Authenticate
def auth():
    while True:
        clear()
        print(f"\033[34mBy ©{creator}\033[0m")
        license_key = input("License: ")

        if license_key:
            try:
                reply = client.license(license_key=license_key)
            except Exception:
                pass
            else:
                if reply:
                    return

        print("\033[31mInvalid license key\033[0m")
        time.sleep(1)


auth()
input("Press any key to continue . . . ")
