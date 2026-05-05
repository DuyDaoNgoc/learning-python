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
def transitive_reload(module,visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module]=True

    for attjob in module.__dict__.values():
        if type(attjob)==types.ModuleType:
            transitive_reload(attjob,visited)
def reload_all(module):
    transitive_reload(module, {})
def tester(reloader,module):
    import importlib , sys
    module_name = module
    module_obj = importlib.import_module(module_name)
    print(reloader(module_obj))
if __name__ == "__main__":
    tester(reload_all,"reloadall3")
