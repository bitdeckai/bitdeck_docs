#!/usr/bin/env python3
"""
Simple example that connects to a Crazyflie and logs position data from Lighthouse.
Only prints XYZ position coordinates.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
from cflib.utils.reset_estimator import reset_estimator

# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


def position_callback(timestamp, data, logconf):
    """Callback function for position data"""
    x = data['kalman.stateX']
    y = data['kalman.stateY']
    z = data['kalman.stateZ']
    print(f'Position: X={x:.3f}, Y={y:.3f}, Z={z:.3f}')


def log_position_data(scf):
    """Start logging position data from Lighthouse"""
    log_conf = LogConfig(name='Position', period_in_ms=100)
    log_conf.add_variable('kalman.stateX', 'float')
    log_conf.add_variable('kalman.stateY', 'float')
    log_conf.add_variable('kalman.stateZ', 'float')

    scf.cf.log.add_config(log_conf)
    log_conf.data_received_cb.add_callback(position_callback)
    log_conf.start()

    # Keep logging for 30 seconds
    time.sleep(30)
    log_conf.stop()


if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    cf = Crazyflie(rw_cache='./cache')
    with SyncCrazyflie(uri, cf=cf) as scf:
        # Reset the estimator to get accurate position data
        reset_estimator(scf)
        
        # Start logging position data
        print(f'Connecting to Crazyflie at {uri}...')
        print('Logging position data for 30 seconds...')
        log_position_data(scf)
        print('Done!')
