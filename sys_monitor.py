import psutil
import sys
import os

from pypresence import Presence
import time

client_id = '1136673114839859341'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop

counter = 0;

while True:  # The presence will stay on as long as the program is running
    cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)

    counter += 1;
    counter = counter % 10;

    if (counter < 5):
        print(RPC.update(large_image="arch-linux", large_text="Arch Linux",
                     small_image="i712thgen", small_text="Intel i7-12700H",
                     details="RAM: " + str(mem_per) + "%  CPU: " + str(cpu_per) + "%",
                     buttons=[{"label": "A Website", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}],
                     start=psutil.boot_time(),
                     state="Kernel: " + os.uname().release))  # Set the presence
    else:
        print(RPC.update(large_image="arch-linux", large_text="Arch Linux",
                     small_image="nvidia", small_text="nVidia RTX 3060 Laptop GPU",
                     details="RAM: " + str(mem_per) + "%  CPU: " + str(cpu_per) + "%",
                     buttons=[{"label": "A Website", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}],
                     start=psutil.boot_time(),
                     state="OS: " + os.uname().release))  # Set the presence

    time.sleep(15) # Can only update rich presence every 15 seconds
