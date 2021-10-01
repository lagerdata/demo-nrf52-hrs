from lager.ble import Central

HRM_SERVICE = "0000180d-0000-1000-8000-00805f9b34fb"
HRM_BODY_SENSOR_LOCATION_CHAR =  "00002a38-0000-1000-8000-00805f9b34fb"
HRM_MEASUREMENT_CHAR =  "00002a37-0000-1000-8000-00805f9b34fb"

BATTERY_SERVICE = "0000180f-0000-1000-8000-00805f9b34fb"
BATTERY_LEVEL_CHAR = "00002a19-0000-1000-8000-00805f9b34fb"

DEVICE_INFORMATION_SERVICE = "0000180a-0000-1000-8000-00805f9b34fb"
MFG_NAME_STRING_CHAR = "00002a29-0000-1000-8000-00805f9b34fb"

BLE_HRS_BODY_SENSOR_LOCATION_OTHER = 0
BLE_HRS_BODY_SENSOR_LOCATION_FOOT = 6

HRS_LOCATIONS = {0: 'BLE_HRS_BODY_SENSOR_LOCATION_OTHER',
  1: 'BLE_HRS_BODY_SENSOR_LOCATION_CHEST',
  2: 'BLE_HRS_BODY_SENSOR_LOCATION_WRIST',
  3: 'BLE_HRS_BODY_SENSOR_LOCATION_FINGER',
  4: 'BLE_HRS_BODY_SENSOR_LOCATION_HAND',
  5: 'BLE_HRS_BODY_SENSOR_LOCATION_EAR_LOBE',
  6: 'BLE_HRS_BODY_SENSOR_LOCATION_FOOT'}





def test_hrm_notifications(central, device):
    with central.connect(device[0]) as client:
        print("Validating HRM Notification Data")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")

        val = int.from_bytes(client.read_gatt_char(HRM_BODY_SENSOR_LOCATION_CHAR),"little")
        assert BLE_HRS_BODY_SENSOR_LOCATION_OTHER < val <= (BLE_HRS_BODY_SENSOR_LOCATION_FOOT)

        try:
            timed_out, messages = client.start_notify(HRM_MEASUREMENT_CHAR, max_messages=5, timeout=10)
            if timed_out:
                raise SystemExit("Heart Rate Notifications Failed")
        finally:
            client.stop_notify(HRM_MEASUREMENT_CHAR)


def test_batt_notifications(central, device):
    with central.connect(device[0]) as client:
        print("Validating Battery Notification Data")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")    
        val = int.from_bytes(client.read_gatt_char(BATTERY_LEVEL_CHAR),"little")
        assert 20 <= val <= 100
        try:
            timed_out, messages = client.start_notify(BATTERY_LEVEL_CHAR, max_messages=2, timeout=30)
            if timed_out:
                raise SystemExit("Battery Level Notifications Failed")
        finally:
            client.stop_notify(BATTERY_LEVEL_CHAR)    



def test_dis_read(central, device):
    with central.connect(device[0]) as client:
        print("Validating DIS Read Data")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")     
        val = client.read_gatt_char(MFG_NAME_STRING_CHAR).decode("utf-8")
        assert val == 'NordicSemiconductor'
