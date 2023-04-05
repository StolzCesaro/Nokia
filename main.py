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
search_label.pack()
search_entry.pack()
search_button.pack()
display_text.pack()
root.mainloop()


def ssh_connect():
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

    # Close the SSH connection
    ssh.close()


# Create a GUI window with a "Connect SSH" button
root = tk.Tk()
button = tk.Button(root, text="Connect SSH", command=ssh_connect)
button.pack()

root.mainloop()
