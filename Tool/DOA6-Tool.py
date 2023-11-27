import os
import configparser
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime
config_file_path = "config.cfg"
file_path = ""
if os.path.exists(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)
    if "FileLocation" in config["Settings"]:
        file_path = config["Settings"]["FileLocation"]

if not file_path:
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("INI files", "*.ini")])
    if not file_path:
        print("No file selected. Exiting.")
        exit()
    config = configparser.ConfigParser()
    config["Settings"] = {"FileLocation": file_path}
    with open(config_file_path, "w") as config_file:
        config.write(config_file)

steam_ini_path = os.path.join(os.path.dirname(file_path), "steam_emu.ini")
if os.path.exists(steam_ini_path):
    # Create a backup copy with a timestamp
    backup_folder = os.path.join(os.getcwd(), "backup")
    os.makedirs(backup_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file_name = f"steam_emu_backup_{timestamp}.ini"
    backup_file_path = os.path.join(backup_folder, backup_file_name)
    with open(steam_ini_path, 'r') as original_file:
        original_content = original_file.read()
    with open(backup_file_path, 'w') as backup_file:
        backup_file.write(original_content)
    user_name = input("Enter a new username: ")
    for i, line in enumerate(original_content.split('\n')):
        if "UserName" in line:
            original_content = '\n'.join(
                f"UserName={user_name}" if idx == i else l for idx, l in enumerate(original_content.split('\n'))
            )
            break
    modify_language = input("Do you want to modify the language? (y/n): ").lower()
    if modify_language == "y":
        # Modify Language
        language = input("Enter the new language: ")
        for i, line in enumerate(original_content.split('\n')):
            if "Language" in line:
                original_content = '\n'.join(
                    f"Language={language}" if idx == i else l for idx, l in enumerate(original_content.split('\n'))
                )
                break
    with open(steam_ini_path, 'w') as modified_file:
        modified_file.write(original_content)
    print(f"Modification completed. Backup created at {backup_file_path}.")
else:
    print("steam_emu.ini not found in the specified folder.")
