import time
from machine import Pin, UART
# Initialize UART for communication
uart = UART(1, baudrate=115200, tx=17, rx=16)  # Adjust pins as needed
# Define GPIO pin for door lock mechanism
door_lock_pin = Pin(5, Pin.OUT)  # Adjust pin number as needed
def unlock_door():
    # Set the door lock pin to LOW to unlock the door
    door_lock_pin.value(0)
    print("Door unlocked")
    uart.write('UNLOCKED\n')  # Send confirmation back to the UART
def lock_door():
    # Set the door lock pin to HIGH to lock the door
    door_lock_pin.value(1)
    print("Door locked")
    uart.write('LOCKED\n')  # Send confirmation back to the UART
def main():
    # Set the initial state of the door lock
    door_lock_pin.value(1)  # Start with the door locked
    while True:
        # Check for incoming data from UART
        if uart.any():
            data = uart.readline().decode('utf-8').strip()
            print("Received:", data)
            if data == 'UNLOCK':
                unlock_door()
            elif data == 'LOCK':
                lock_door()
        time.sleep(1)  # Delay to avoid busy-waiting
if __name__ == '__main__':
    main()
    
