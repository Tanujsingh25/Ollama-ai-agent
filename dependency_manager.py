import importlib
import subprocess
import sys

def is_installed(lib):
    try:
        importlib.import_module(lib)
        return True
    except ImportError:
        return False

def install(lib):
    print(f"Installing missing library: {lib}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

def ensure_libraries(libs):
    for lib in libs:
        if not is_installed(lib):
            install(lib)
