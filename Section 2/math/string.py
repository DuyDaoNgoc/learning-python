s = "Dao Ngoc Duy"
l =list(s)
print(l)
l[3]  = "C"
print("".join(l))
B =bytearray(b"app")
print(B.extend(b"lication"))

print(B)
print(B.decode())

tool = "python"
major = 3
mintor = 3
print('Using %s version %s.%s '%(tool,major,mintor + 9))
print("using {} version {}.{}".format(tool, major, mintor + 9))
print(f"using {tool} version {major}.{mintor + 9}")
print(str("Using " + tool + " version " + str(major) + "." + str(mintor + 9)))

