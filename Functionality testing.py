import serial
import time
def test_unlock_lock():
    # Open serial port (adjust 'COM3' to your ESP32's port)
    ser = serial.Serial('COM3', 115200, timeout=1)
    time.sleep(2)  # Wait for the connection to establish

    try:
        # Send unlock command
        ser.write(b'UNLOCK\n')
        time.sleep(1)  # Wait for response
        print("Sent: UNLOCK")

        # Read response
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            print("Received:", response)

        # Send lock command
        ser.write(b'LOCK\n')
        time.sleep(1)  # Wait for response
        print("Sent: LOCK")

        # Read response
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            print("Received:", response)

    finally:
        ser.close()
if __name__ == '__main__':
    test_unlock_lock()
