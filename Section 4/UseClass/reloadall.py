import types
from importlib import reload
def status(module):
    print(f"Reloading module: {module.__name__}")

def tryreload(module):
    try:
        reload(module)
        status(module)
    except Exception as e:
        print(f"Error occurred while reloading {module.__name__}: {e}")
