from lager import lager
from lager.ble import Central
from ble_scan_test import *
from ble_gatts_test import *
from ble_read_write_notify_test import *


def main():
    gateway = lager.Lager()
    dut = gateway.connect("nrf52",interface="ftdi",transport="swd",speed=3000)
    print(f"Connected to DUT:{dut}")

    #reset device
    dut.reset()

    central = Central()
    device = test_scan(central, 'Nordic_HRM')
    display_gatts_table(central, device)
    test_gatts_table_hrm(central, device)
    test_gatts_table_battery(central, device)
    test_gatts_table_dis(central, device)
    test_hrm_notifications(central, device)
    test_batt_notifications(central, device)
    test_dis_read(central, device)    

    print("Brilliant!")
    dut.close()





if __name__ == '__main__':
     main()
