from importlib import reload
import UseReload.index as index
import UseReload.script0 as script0
reload(index)
reload(script0)



import threenames

print(threenames.b, threenames.c)
from threenames import a, b, c
print(a, b, c)
