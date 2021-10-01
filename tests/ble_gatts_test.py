from lager.ble import Central



HRM_SERVICE = "0000180d-0000-1000-8000-00805f9b34fb"
HRM_BODY_SENSOR_LOCATION_CHAR =  "00002a38-0000-1000-8000-00805f9b34fb"
HRM_MEASUREMENT_CHAR =  "00002a37-0000-1000-8000-00805f9b34fb"

BATTERY_SERVICE = "0000180f-0000-1000-8000-00805f9b34fb"
BATTERY_LEVEL_CHAR = "00002a19-0000-1000-8000-00805f9b34fb"

DEVICE_INFORMATION_SERVICE = "0000180a-0000-1000-8000-00805f9b34fb"
MFG_NAME_STRING_CHAR = "00002a29-0000-1000-8000-00805f9b34fb"

def display_gatts_table(central, device):
    with central.connect(device[0]) as client:
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")        
        for service in services:
            print(service)
            for characteristic in service.characteristics:
                print(f"\t{characteristic}")
                print(f"\t{characteristic.properties}")

def test_gatts_table_hrm(central, device):
    with central.connect(device[0]) as client:
        print("Verifying HRM Serivce and Characteristics")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")

        #Check that the services, and the charactersitics for those services actually exist
        hrm_service = services.get_service(HRM_SERVICE)
        if not hrm_service:
            raise SystemExit(f"HRM Service not found:{services}")
        if not any(char.uuid == HRM_MEASUREMENT_CHAR for char in hrm_service.characteristics):
            raise SystemExit("Heart Rate Measurement Not Found")
        if not any(char.uuid == HRM_BODY_SENSOR_LOCATION_CHAR for char in hrm_service.characteristics):
            raise SystemExit("Heart Rate Body Sensor Location Not Found")

        #Verify the properties for each characteristics
        for char in hrm_service.characteristics:
            if char.uuid == HRM_MEASUREMENT_CHAR:
                assert char.properties[0] == 'notify'
            if char.uuid == HRM_BODY_SENSOR_LOCATION_CHAR:
                assert char.properties[0] == 'read'


def test_gatts_table_battery(central, device):
    with central.connect(device[0]) as client:
        print("Verifying Battery Serivce and Characteristics")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")        
        batt_service = services.get_service(BATTERY_SERVICE)
        if not batt_service:
            raise SystemExit(f"Battery Service not found:{services}")
        if not any(char.uuid == BATTERY_LEVEL_CHAR for char in batt_service.characteristics):
            raise SystemExit("Battery Level Not Found")
        for char in batt_service.characteristics:
            if char.uuid == BATTERY_LEVEL_CHAR:
                assert char.properties[0] == 'read'
                assert char.properties[1] == 'notify'


def test_gatts_table_dis(central, device):
    with central.connect(device[0]) as client:
        print("Verifying Device Information Serivce and Characteristics")
        services = client.get_services()
        if not services:
            raise SystemExit("No Services Found")
        di_service = services.get_service(DEVICE_INFORMATION_SERVICE)
        if not di_service:
            raise SystemExit(f"Device Information Service not found:{services}")
        if not any(char.uuid == MFG_NAME_STRING_CHAR for char in di_service.characteristics):
            raise SystemExit("Mfg String Not Found")
        for char in di_service.characteristics:
            if char.uuid == MFG_NAME_STRING_CHAR:
                assert char.properties[0] == 'read'      
