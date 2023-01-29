import datetime
import logging
import queue
import time
import numpy as np
import logging
import sys
import threading
import copy
from redvypr.device import redvypr_device
from redvypr.data_packets import check_for_command


description = 'redvypr device skeleton'

config_template = {}
config_template['string_send']    = {'type': 'str','default':'Hello World!'}
config_template['delay_s']        = {'type': 'float','default':2}
config_template['redvypr_device'] = {}
config_template['redvypr_device']['publish']     = True
config_template['redvypr_device']['subscribe']   = False
config_template['redvypr_device']['description'] = description


logging.basicConfig(stream=sys.stderr)
logger = logging.getLogger('redvypr_device_skeleton')
logger.setLevel(logging.DEBUG)



def start(device_info,config=None,dataqueue=None,datainqueue=None,statusqueue=None):
    funcname = __name__ + '.start():'
    logger.debug(funcname)
    print('config',config)
    i = 0
    while True:
        try:
            data = datainqueue.get(block=False)
        except:
            data = None
        if(data is not None):
            command = check_for_command(data,thread_uuid=device_info['thread_uuid'])
            logger.debug('Got a command: {:s}'.format(str(data)))
            if (command == 'stop'):
                logger.debug('Command is for me: {:s}'.format(str(command)))
                break

        dstr = str(config['string_send'])
        print(dstr)
        dataqueue.put(dstr)
        dataqueue.put({'count':i})
        i+=1
        time.sleep(config['delay_s'])
