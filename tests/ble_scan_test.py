from lager.ble import Central



def test_scan(central, dev_name):
    # `central.scan` takes two optional keyword args, `name` and `address`, which
    # will filter the list of results down to those devices which match. If neither
    # is provided, all scanned devices will be returned	
	device = central.scan(name=dev_name)
	if not device:
		raise SystemExit("Error Device Not Found")

	print(f"Device Info: {device}")
	return device