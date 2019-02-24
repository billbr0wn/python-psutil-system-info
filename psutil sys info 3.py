from multiprocessing import cpu_count
import datetime
import psutil
import os

print('cpu_use: ', psutil.cpu_percent(interval=0.5), '%')
print()
print('cpu_core 1 and 2: ', psutil.cpu_percent(interval=1, percpu=True), '%')
print()
print('cpu_count: ', psutil.cpu_count(), 'cores')
print()
print('cpu_frequency: ', psutil.cpu_freq(percpu=False)[0]/1000, 'Ghz')
print()

print('swap_used: ', psutil.swap_memory()[3], '%')
print()
print()
print('memory_used: ', psutil.virtual_memory()[2], '%')
print()
print('disk_used: ', psutil.disk_usage('/')[3], '%')
print()

if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
else:
    temps = {}
        
print()
names = set(list(temps.keys()))
for name in names:
    print(name)
    if name in temps:
        print("    Temperatures:")
        for entry in temps[name]:
            print("     %s °C " % (entry.current))
            print()
            
CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
print("CPU Usage = " + CPU_Pct, '%')
print()

boottime = psutil.boot_time() /10000000
print('boot time: ', boottime, ' seconds')



for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    pass








    

