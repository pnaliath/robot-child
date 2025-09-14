from jnius import autoclass

# Android Bluetooth classes
BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
UUID = autoclass('java.util.UUID')

# Standard SerialPortService ID
BT_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")

# Get default adapter
adapter = BluetoothAdapter.getDefaultAdapter()

if adapter is None:
    print("Bluetooth not supported on this device.")
elif not adapter.isEnabled():
    print("Bluetooth is disabled.")
else:
    print("Bluetooth is ON")

    # List paired devices
    paired_devices = adapter.getBondedDevices().toArray()
    for device in paired_devices:
        print(f"Paired device: {device.getName()} - {device.getAddress()}")

    # Replace with ESP32 MAC address
    target_mac = "XX:XX:XX:XX:XX:XX"  
    device = adapter.getRemoteDevice(target_mac)

    # Try opening a socket
    socket = device.createRfcommSocketToServiceRecord(BT_UUID)
    socket.connect()
    print("Connected to ESP32!")

    # Send a test command
    socket.getOutputStream().write(b"F150\n")
    print("Sent: F150")

    # Close socket
    socket.close()
