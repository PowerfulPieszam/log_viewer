# 📑 log_saver

a simple program for saving and reading logs, built in **Python + CustomTkinter**.

## functions
- Viewing logs from the `logs.txt` file
- Coloring logs depending on type:
- `[INFO]` → yellow
- `[PROCESS]` → orange
- `[ERROR]` → red
- Adding new logs
- Clearing all logs
- Automatically saving changes to the file

## How to launch
1. clone repo:
   ```bash
   git clone (https://github.com/PowerfulPieszam/log_viewer)
   cd log-viewer
2. make sure u have everything important:
   ```bash
   pip install -r requirements.txt
   python log_saver_main.py

## ⚠️ Possible installation issues

On some systems for example Python 3.11/3.12 on Linux or Python installed from the Microsoft store you may encounter the following error when installing dependencies:
error: externally-managed-environment

This means that you cannot install packages globally.  
The recommended solution is to create and use a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux
source .venv/bin/activate

pip install -r requirements.txt
```
Alternatively, you can force the installation globally I do not recommend that:
```bash
pip install customtkinter --break-system-packages
```

If that doesn't help, ask AI, after all, it's the 21st century.
