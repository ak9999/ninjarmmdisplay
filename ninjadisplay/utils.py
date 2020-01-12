from collections import namedtuple

# Helper functions

def safe_get(dictionary, *keys):
    for key in keys:
        try:
            dictionary = dictionary[key]
        except KeyError:
            return None
    return dictionary


def get_servers(device_list=None):
    if device_list == None:
        device_list = api.get_devices()  # Limited to ten calls every ten minutes
    servers = [d for d in device_list if d['role'] == 'WINDOWS_SERVER']
    return servers


def get_virtual_devices(device_list=None):
    if device_list == None:
        device_list = api.get_devices()  # Limited to ten calls every ten minutes
    virtual_devices = []
    for d in device_list:
        if safe_get(d, 'system', 'model') == "Virtual Machine":
            virtual_devices.append(d)
    return virtual_devices



# Factory functions
Alert = namedtuple('Alert', ['hostname', 'customer', 'url', 'alert'])
