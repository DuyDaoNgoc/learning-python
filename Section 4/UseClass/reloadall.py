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

op = []
if op == reload_all:
    print("op is reload_all")
else:
    print("op is not reload_all")

modreload_all = tester(reload_all,"reloadall3")

class cat :
    Hoddy = "sleping"
    age = 2
pet = cat()
attr = getattr(pet,"age")
print("mồn lèo", attr, "tuổi ")
 # repviwed and looks good. The code defines a mechanism to reload a module and all of its submodules recursively. It uses the
 # `importlib.reload` function to reload modules and handles exceptions that may occur during the reload process. The `tester`
 # function is used to test the `reload_all` function by importing a specified module and reloading it.

