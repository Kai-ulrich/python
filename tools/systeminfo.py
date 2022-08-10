import platform

systeminfo = platform.uname()

print(f"System: {systeminfo.system}")
print(f"Node Name: {systeminfo.node}")
print(f"Version: {systeminfo.version}")
print(f"Machine: {systeminfo.machine}")
print(f"Processor: {systeminfo.processor}")