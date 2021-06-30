from lager import lager
from lager.ble import Central
import time

HRM_SERVICE = "0000180d-0000-1000-8000-00805f9b34fb"
HRM_BODY_SENSOR_LOCATION_CHAR =  "00002a38-0000-1000-8000-00805f9b34fb"
HRM_MEASUREMENT_CHAR =  "00002a37-0000-1000-8000-00805f9b34fb"

BLE_HRS_BODY_SENSOR_LOCATION_OTHER = 0
BLE_HRS_BODY_SENSOR_LOCATION_FOOT = 6

HRS_LOCATIONS = {0: 'BLE_HRS_BODY_SENSOR_LOCATION_OTHER',
  1: 'BLE_HRS_BODY_SENSOR_LOCATION_CHEST',
  2: 'BLE_HRS_BODY_SENSOR_LOCATION_WRIST',
  3: 'BLE_HRS_BODY_SENSOR_LOCATION_FINGER',
  4: 'BLE_HRS_BODY_SENSOR_LOCATION_HAND',
  5: 'BLE_HRS_BODY_SENSOR_LOCATION_EAR_LOBE',
  6: 'BLE_HRS_BODY_SENSOR_LOCATION_FOOT'}

BATTERY_SERVICE = "0000180f-0000-1000-8000-00805f9b34fb"
BATTERY_LEVEL_CHAR = "00002a19-0000-1000-8000-00805f9b34fb"

DEVICE_INFORMATION_SERVICE = "0000180a-0000-1000-8000-00805f9b34fb"
MFG_NAME_STRING_CHAR = "00002a29-0000-1000-8000-00805f9b34fb"


def main():
    gateway = lager.Lager()
    dut = gateway.connect("nrf52",interface="ftdi",transport="swd",speed=3000)
    print(f"Connected to DUT:{dut}")
    central = Central()

    #reset device
    dut.reset()

    print("Scanning for Nordic HRM Device")

    # `central.scan` takes two optional keyword args, `name` and `address`, which
    # will filter the list of results down to those devices which match. If neither
    # is provided, all scanned devices will be returned

    device = central.scan(name='Nordic_HRM')
    if not device:
        raise SystemExit("Error Device Not Found")
    print(f"Device Info: {device}")

    #Test Connection
    with central.connect(device[0]) as client:
        print("Connected to DUT")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")
        for service in services:
            print(service)
            for characteristic in service.characteristics:
                print(f"\t{characteristic}")
                print(f"\t{characteristic.properties}")

        hrm_service = services.get_service(HRM_SERVICE)
        if not hrm_service:
            raise SystemExit(f"HRM Service not found:{services}")
        if not any(char.uuid == HRM_MEASUREMENT_CHAR for char in hrm_service.characteristics):
            raise SystemExit("Heart Rate Measurement Not Found")
        if not any(char.uuid == HRM_BODY_SENSOR_LOCATION_CHAR for char in hrm_service.characteristics):
            raise SystemExit("Heart Rate Body Sensor Location Not Found")

        for char in hrm_service.characteristics:
            if char.uuid == HRM_MEASUREMENT_CHAR:
                assert char.properties[0] == 'notify'
            if char.uuid == HRM_BODY_SENSOR_LOCATION_CHAR:
                assert char.properties[0] == 'read'

        val = int.from_bytes(client.read_gatt_char(HRM_BODY_SENSOR_LOCATION_CHAR),"little")
        print(HRS_LOCATIONS.get(val))
        assert BLE_HRS_BODY_SENSOR_LOCATION_OTHER < val <= (BLE_HRS_BODY_SENSOR_LOCATION_FOOT)

        try:
            timed_out, messages = client.start_notify(HRM_MEASUREMENT_CHAR, hrm_notify_cb, max_messages=5, timeout=10)
            if timed_out:
                raise SystemExit("Heart Rate Notifications Failed")
        finally:
            client.stop_notify(HRM_MEASUREMENT_CHAR)
        print("Heart Rate Measurement Service Verified")



        batt_service = services.get_service(BATTERY_SERVICE)
        if not batt_service:
            raise SystemExit(f"Battery Service not found:{services}")
        if not any(char.uuid == BATTERY_LEVEL_CHAR for char in batt_service.characteristics):
            raise SystemExit("Battery Level Not Found")
        for char in batt_service.characteristics:
            if char.uuid == BATTERY_LEVEL_CHAR:
                assert char.properties[0] == 'read'
                assert char.properties[1] == 'notify'


        val = int.from_bytes(client.read_gatt_char(BATTERY_LEVEL_CHAR),"little")
        print(f"Battery Level:{val}")
        assert 20 <= val <= 100
        try:
            timed_out, messages = client.start_notify(BATTERY_LEVEL_CHAR, batt_notify_cb, max_messages=2, timeout=30)
            if timed_out:
                raise SystemExit("Battery Level Notifications Failed")
        finally:
            client.stop_notify(BATTERY_LEVEL_CHAR)

        print("Battery Service verified")

        di_service = services.get_service(DEVICE_INFORMATION_SERVICE)
        if not di_service:
            raise SystemExit(f"Device Information Service not found:{services}")
        if not any(char.uuid == MFG_NAME_STRING_CHAR for char in di_service.characteristics):
            raise SystemExit("Mfg String Not Found")
        for char in di_service.characteristics:
            if char.uuid == MFG_NAME_STRING_CHAR:
                assert char.properties[0] == 'read'

        val = client.read_gatt_char(MFG_NAME_STRING_CHAR).decode("utf-8")
        print(f"Manufacturer String:{val}")
        assert val == 'NordicSemiconductor'
        print("Device Information Serivce verified")

    print("Brilliant!")
    dut.close()



def hrm_notify_cb(handle: int, data: bytearray):
    print(f"Received Heart Rate Measurement: {data}")

def batt_notify_cb(handle: int, data: bytearray):
    val = int.from_bytes(data, "little")
    print(f"Received Battery Level: {val}")

if __name__ == '__main__':
     main()
