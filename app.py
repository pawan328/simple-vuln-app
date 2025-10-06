# app.py (vulnerable)
import os
import sys
import pathlib
import subprocess

def run_command():
    """Deliberately vulnerable: unsanitized user input passed to shell."""
    user_input = input("Enter a directory to list: ")
    # ❌ Vulnerability: passing user input directly into shell=True
    subprocess.run(f"ls {user_input}", shell=True)

def main():
    """Launch the Streamlit Home page."""
    # Path to the HOME.py file
    home_path = pathlib.Path(__file__).parent / "HOME.py"

    # Use the virtual environment's Python if available
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        python_executable = os.path.join(venv_path, "bin", "python")
    else:
        python_executable = sys.executable

    # Run streamlit on the HOME.py file
    subprocess.run([python_executable, "-m", "streamlit", "run", str(home_path)])

if __name__ == "__main__":
    run_command()
    main()