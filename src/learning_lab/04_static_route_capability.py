#!/usr/bin/env python2.7

# Copyright 2015 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

''' Sample code to determine 'static route' capability for a specific device.

    Print the documentation of function 'capability_discovery'.
    Apply the function.
    Print the function output.
'''

from __future__ import print_function as _print_function
from pydoc import plain
from pydoc import render_doc as doc
import os
from basics.interpreter import sys_exit
from basics.routes import capability_ns, capability_name
from basics.inventory import capability_discovery, inventory_mounted, connected

def demonstrate(device_name):
    ''' Apply function 'capability_discovery' to the specified device for required capability. '''
    print()
    print('capability_discovery(device_name=%s, capability_name=%s, capability_ns=%s)' % (device_name, capability_name, capability_ns))
    discovered = capability_discovery(device_name=device_name, capability_name=capability_name, capability_ns=capability_ns)
    if discovered:
        print('\t', *discovered)
        return True
    else:
        print(None)
        return False
    
def main():
    ''' Document and demonstrate the function until a capable device is found.'''
    print(plain(doc(capability_discovery)))
    for device_name in inventory_mounted():
        try:
            if demonstrate(device_name):
                return os.EX_OK
        except Exception as e:
            if connected(device_name):
                # Unexplained exception.                
                print(e)
                return os.EX_TEMPFAIL
            else:
                # Expect exception when device not connected.             
                print('connected(%s): False' % device_name)
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())
