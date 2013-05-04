import subprocess
import plistlib
import logging

class MacBatteryCapacity(object):
    plugin_name = 'mac_battery_capacity'

    def __init__(self, config):
        pass

    def __call__(self):
        data_raw = subprocess.check_output(['system_profiler', 'SPPowerDataType', '-xml'])
        data = plistlib.readPlistFromString(data_raw)
        battery_info = [i for i in data[0]['_items'] if i['_name'] == 'spbattery_information'][0]

        return [
            {
                'labels': {
                    'name': 'mac_battery_current_capacity'
                },
                'value': battery_info['sppower_battery_charge_info']['sppower_battery_current_capacity']
            },
            {
                'labels': {
                    'name': 'mac_battery_max_capacity'
                },
                'value': battery_info['sppower_battery_charge_info']['sppower_battery_max_capacity']
            }
        ]

if __name__ == '__main__':
    import sys
    import time
    import pprint
    import yaml

    logging.basicConfig()

    plugin = MacBatteryCapacity({})

    pprint.pprint(plugin())
