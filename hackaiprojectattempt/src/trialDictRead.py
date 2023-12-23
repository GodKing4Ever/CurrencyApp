from apiCall import readVals
coreCur = 'AED'
k = readVals()
print(k.keys())
coreVal = k[coreCur]
for a in k.keys():
    k[a] = float(f"{(k[a]/coreVal):.6g}")
print("\n\n\n")
# print(k)
# print(type(k))

print(list(k.keys()))