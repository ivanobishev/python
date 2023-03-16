import time, math

seconds = int(input("Say an amount of seconds: "))
time.sleep(1)

hours = math.floor(seconds / 3600)
seconds = seconds - hours * 3600

minutes = math.floor(seconds / 60)
seconds = seconds - minutes * 60

print(f"{hours}:{minutes}:{seconds}")
