
import os
import sys
from PyInstaller.__main__ import run

def create_exe():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Set the path to the main script
    main_script = os.path.join(current_dir, "..", "src", "optiwrite_ai.py")

    # Set the path to the output directory
    output_dir = os.path.join(current_dir, "..", "dist")

    # Set the name of the output executable
    output_name = "optiwrite_ai"

    # Set the path to the icon file (optional)
    icon_file = os.path.join(current_dir, "..", "gui", "icon.ico")

    # Set the additional options for PyInstaller
    additional_options = [
        "--onefile",  # Create a single executable file
        "--windowed",  # Do not display a console window
        "--name={}".format(output_name),  # Set the name of the output executable
        "--icon={}".format(icon_file) if icon_file else ""  # Set the icon file if provided
    ]

    # Set the arguments for PyInstaller
    args = [
        main_script,
        *additional_options,
        "--distpath={}".format(output_dir)
    ]

    # Run PyInstaller
    run(args)

if __name__ == "__main__":
    create_exe()

