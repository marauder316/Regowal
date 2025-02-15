import subprocess, os
import filecreator

user_name = os.environ.get("USER")
HOME_DIR = "/home/" + user_name
NEW_DIR = HOME_DIR + "/.regowal/styles/regowaltheme/"


def write_files(dir):
    filecreator.write_color_file(dir)
    filecreator.write_rofi_file(dir)
    filecreator.write_root_file(dir)
    filecreator.write_theme_file(dir)
    filecreator.write_typeface_file(dir)


print(
    """
                  ``....```                 
            `.:/++++++/::-.`                
          -/+++++++:.`                      
        -++++++++:`                         
      `/++++++++-                           
     `/++++++++.                    -/+/    
     /++++++++/             ``   .:+++:.    
    -+++++++++/          ./++++:+++/-`      
    :+++++++++/         `+++++++/-`         
    :++++++++++`      .-/+++++++`             
   `:++++++++++/``.-/++++:-:::-`      `
 `:+++++++++++++++++/:.`            ./`
:++/-:+++++++++/:-..              -/+.
+++++++++/::-...:/+++/-..````..-/+++.
`......``.::/+++++++++++++++++++++/.
         -/+++++++++++++++++++++/.
           .:/+++++++++++++++/-`
              `.-:://////:-.
)
print(
    """
------------------------
Welcome to Regowal setup
------------------------
"""
)
print(
    """
This script will modify your system to use Regowal. Please visit https://github.com/JollyRogerTrader/Regowal to find support and feel free to report bugs.
"""
)
ans = input("Are you sure you want to continue?   [y/n]?")
if ans != "y":
    exit()
try:
    print("Creating needed directories.")
    command = subprocess.call(
        ["mkdir", str(HOME_DIR + "/.regowal/")], stdout=subprocess.DEVNULL
    )
    if command == 0:
        print("Directory created at " + HOME_DIR + "/.regowal/")
        command = subprocess.call(
            ["mkdir", str(HOME_DIR + "/.regowal/styles/")], stdout=subprocess.DEVNULL
        )
        command = subprocess.call(
            ["mkdir", str(HOME_DIR + "/.regowal/styles/regowaltheme/")],
            stdout=subprocess.DEVNULL,
        )
        if command == 0:
            print("Directory created at " + HOME_DIR + "/.regowal/styles/")

    else:
        print()

except:
    print(
        "Error creating directories - this is probably a bug and should be reported to https://github.com/JollyRogerTrader/Regowal"
    )

# writing template files
write_files(NEW_DIR)
xres_command = None

try:
    xres_command = subprocess.check_output(["cat", HOME_DIR + "/.Xresources-regolith"])
except:
    print("Did not find a Xresources-regolith file")

if len(str(xres_command).split("\n")) > 1:
    print(
        ".Xresources-regolith has been customized with additional settings - editing will have to be done manually"
    )
    print(
        "modify .Xresources-regolith to read: "
        + '#include "/home/'
        + user_name
        + '/.regowal/styles/regowaltheme/root"\n'
    )
else:
    try:
        with open(HOME_DIR + "/.Xresources-regolith", "w") as xres_file:
            xres_file.write(
                '#include "/home/' + user_name + '/.regowal/styles/regowaltheme/root"\n'
            )
    except:
        print("Could not write Xresources-regolith file")

print("Verifying you have needed dependancies")
try:
    pip3 = subprocess.call(
        ["pip3", "install", "pillow==6.1.0"], stdout=subprocess.DEVNULL
    )
except subprocess.CalledProcessError as error:
    print(error)

try:
    imagemagick = subprocess.check_call(["which", "convert"], stdout=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    print("Imagemagick is not installed - use 'sudo apt install imagemagick'")

print(
    """
Converting regowal.py to regowal and making it executable
"""
)
# making regowal executable
subprocess.call(["cp", "regowal.py", "regowal"])
subprocess.call(["chmod", "+x", "regowal"])

# adding regowal to a known path variable
try:
    subprocess.call(["cp", "regowal", HOME_DIR + "/.local/bin/"])
    subprocess.call(["cp", "filecreator.py", HOME_DIR + "/.local/bin/"])
    subprocess.call(["cp", "ayumiragetheme.py", HOME_DIR + "/.local/bin/"])
except:
    pass

print(
    """
----------------------------------------------------------
Setup complete => 'regowal (optional: -light -alt) <wallpaper>' is ready
----------------------------------------------------------
"""
)
