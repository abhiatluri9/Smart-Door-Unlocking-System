import serial
import time
def send_command(command):
    # Open the serial port
    with serial.Serial('COM3', 115200, timeout=1) as ser:  # Adjust
        # the port name as needed
        time.sleep(2)
        ser.write(command.encode('utf-8') + b'\n')
        time.sleep(1)
        response = ser.readline().decode('utf-8').strip()
        print("Response from ESP32:", response)
def main():
    while True:
        command = input("Enter command (UNLOCK/LOCK) or 'exit' to quit: ").strip().upper()
        if command == 'EXIT':
            break
        elif command in ['UNLOCK', 'LOCK']:
            send_command(command)
        else:
            print("Invalid command. Please enter 'UNLOCK', 'LOCK', or 'exit'.")
if __name__ == '__main__':
    main()
