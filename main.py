import pandas as pd
import tkinter as tk
import paramiko
import os
# citirea fișierului Excel

if os.path.exists("task3.xlsx"):
    if "VM2" in pd.read_excel("task3.xlsx", nrows=0).columns:
        df = pd.read_excel("task3.xlsx", usecols=["Name", "Topology", "Owner", "VM", "VM2", "MPlane"])
    else:
        df = pd.read_excel("task3.xlsx", usecols=["Name", "Topology", "Owner", "VM", "MPlane"])
else:
    print("Fișierul task3.xlsx nu a fost găsit în directorul curent.")




# definirea funcției de căutare după nume
def search_name():
    # citirea numelui din widget-ul de căutare
    name = search_entry.get()
    # selectarea rândurilor care conțin numele dat
    results = df.loc[df["Name"] == name]
    # afișarea rezultatelor în widget-ul de afișare
    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, results.to_string(index=False))
    # adăugarea butoanelor pentru conectare prin SSH
    for index, row in results.iterrows():
        ips = row["VM"].split(",")
        for ip in ips:
            if is_valid_ip(ip):
                ssh_button = tk.Button(root, text=f"Conectare la {ip}", command=lambda ip=ip: connect_ssh(ip))
                ssh_button.pack()



# funcție pentru a verifica dacă o adresă IP este validă
def is_valid_ip(ip):
    try:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    except:
        return False


def execute_command(ssh, command):
    # verificarea dacă obiectul transport este valabil
    if ssh.get_transport() is not None:
        # obținerea canalului SSH
        channel = ssh.get_transport().open_session()
        # trimiterea comenzii pe canal
        channel.exec_command(command)
        # citirea ieșirii comenzii
        comanda = channel.recv(1024).decode().strip()
        # afișarea ieșirii comenzii în consolă
        display_text.insert(tk.END, f"\nNumele gazdei: {comanda}\n")


# funcție pentru a efectua conexiunea SSH la o adresă IP dată
def connect_ssh(ip):
    # citirea numelui de utilizator și a parolei
    username = username_entry.get()
    password = password_entry.get()
    # stabilirea conexiunii SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username='adam', password='0000')
    # afișarea output-ului comenzii "hostname"
    stdin, stdout, stderr = ssh.exec_command("hostname")
    output = stdout.read().decode().strip()
    display_text.insert(tk.END, f"\nConectat la {ip} cu succes!\nNumele gazdei: {output}\n")
    # adăugarea butoanelor pentru comenzi
    command_button1 = tk.Button(root, text="Comanda 1", command=lambda: execute_command(ssh, "ls"))
    command_button2 = tk.Button(root, text="Comanda 2")
    command_button1.pack()
    command_button2.pack()

    # găsirea tuturor mașinilor virtuale aferente acestui SBTS
    vms = []
    for index, row in df.iterrows():
        if row["Topology"] == ip:
            vms.append(row["VM"])
    # dacă există două mașini virtuale, adă


