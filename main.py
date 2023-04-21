import pandas as pd
import tkinter as tk
import paramiko

import os

file_name = "task3.xlsx"

current_dir = os.getcwd()

file_path = os.path.join(file_name)

print(file_path)

df = pd.read_excel('task3.xlsx', usecols=["Name", "Topology", "Owner", "VM", "MPlane"])

# Funcție pentru afișarea datelor în funcție de preferințe

def ssh_connect(hostname):
    # Set up SSH connection parameters
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname = '172.19.144.134'
    username = 'adam'
    password = '0000'

    # Connect to the SSH server
    try:
        ssh.connect(hostname, username=username, password=password)
        print('Connected to SSH server')
    except paramiko.ssh_exception.AuthenticationException:
        print('Authentication failed')
    except:
        print('Error connecting to SSH server')


    ssh.close()

def display_data():
    preferinte = search_entry.get()
    results = df.loc[df['Name'] == preferinte]
    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, results.to_string(index=False))
root = tk.Tk()
search_label = tk.Label(root, text="Nume")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Cautare", command=display_data)
display_text = tk.Text(root)

button = tk.Button(root, text="Connect SSH", command=ssh_connect)
button.pack(side=tk.BOTTOM)
search_label.pack(side=tk.TOP)
search_entry.pack(side=tk.TOP)
search_button.pack(side=tk.TOP)

display_text.pack(side=tk.BOTTOM)


root.mainloop()


def ssh_connect():
    # Set up SSH connection parameters
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname = '172.19.144.134'
    username = 'adam'
    password = '0000'


    try:
        ssh.connect(hostname, username=username, password=password)
        print('Connected to SSH server')
    except paramiko.ssh_exception.AuthenticationException:
        print('Authentication failed')
    except:
        print('Error connecting to SSH server')


    ssh.close()


def check_ssh_connection():

    ssh_connected = False  # Setăm la True dacă conexiunea SSH este stabilită


    if ssh_connected:
        button_ute_ca.config(state=tk.NORMAL)
        button_agent_gve_common.config(state=tk.NORMAL)
    else:
        button_ute_ca.config(state=tk.DISABLED)
        button_agent_gve_common.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("Interfață cu butoane")

    # Creăm butonul UTE_CA
    button_ute_ca = tk.Button(root, text="UTE_CA", state=tk.DISABLED)
    button_ute_ca.pack()

    # Creăm butonul AGENT_GVE_COMMON
    button_agent_gve_common = tk.Button(root, text="AGENT_GVE_COMMON", state=tk.DISABLED)
    button_agent_gve_common.pack()


    check_ssh_connection()

    root.mainloop()

