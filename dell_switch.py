#!/usr/bin/python3
import subprocess
import sys

class SubprocessError(Exception):
    """
    Error in subprocess command
    """
    print(f"Error in command execution")

class dell_emc:
    """
    Dell EMC Switch Task Automation
    """
    def __init__(self):
        pass

    def find_devices(self, device):
        """
        See if there are any connections
        to the specified interfaces

        ex: 'ttyUSB0', 'ttyUSB1'

        """
        self.device = device
        switch_device = '/dev/'+self.device
        print(f"Looking for {switch_device}")
        cmd = f"ls {switch_device}"
        try:
            conn = subprocess.getoutput(cmd)
        except SubprocessError as e:
            print(e)

    def connect(self, baud):
        self.baud = baud
        print("connecting to whatever")
