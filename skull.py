mport os
import shutil

def create_backup(file_path):
    """Creates a backup of the existing file if it exists."""
    backup_path = f"{file_path}.bak"
    if os.path.exists(file_path):
        shutil.copy(file_path, backup_path)
        print(f"Original file backed up as: {backup_path}")
    else:
        print("No existing .bashrc file found to back up.")

def write_bashrc(file_path, content):
    """Writes the specified content to the given file path."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"{file_path} file successfully created!")
    except Exception as e:
        print(f"Error creating the file: {e}")

# ASCII art with "Hacker" text inside `echo` commands
bashrc_content = r'''
clear
echo "              _    _            _             "
echo "             | |  | |          | |            "
echo "             | |__| | __ _  ___| | _____ _ __ "
echo "             |  __  |/ _' |/ __| |/ / _ \ '__|"
echo "             | |  | | (_| | (__|   <  __/ |   "
echo "             |_|  |_|\__,_|\___|_|\_\___|_|   "
echo "                         ______         "
echo "                      .-'      '-.      "
echo "                     /            \\    "
echo "                    |   .-.  ._.   |    "
echo "                    | )(_o/  \\o_)( |    "
echo "                    |/     /\\     \\|    "
echo "                    (_     ^^     _)    "
echo "                     \\__|IIIIII|__/     "
echo "                      | \\IIIIII/ |      "
echo "                      \\          /      "
echo "                        \\------/        "
'''

# Determine the path to .bashrc
bashrc_path = os.path.expanduser('~/.bashrc')

# Backup and write the file
create_backup(bashrc_path)
write_bashrc(bashrc_path, bashrc_content)
