import time , sys , os

os.system("cls")
s = "🌎🌍🌏"
for i in range(40):
    
    sys.stdout.write("\r" + s[i%3])
    sys.stdout.flush()
    time.sleep(0.08)
print()