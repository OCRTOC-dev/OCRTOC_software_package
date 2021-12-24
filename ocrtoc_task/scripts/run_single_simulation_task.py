#! /usr/bin/env python3
# Author: Minghao Gou

import os
from multiprocessing import Process
import time
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--task_index')
parser.add_argument('--delay_time', type = int, default = 10)
args = parser.parse_args()
task_index = args.task_index
delay_time = args.delay_time

cmds = [
    'roslaunch ocrtoc_task bringup_simulator_pybullet.launch task_index:={}'.format(task_index),
    'roslaunch ocrtoc_task solution.launch',
    'roslaunch ocrtoc_task trigger_and_evaluation.launch task_index:={}'.format(task_index)
]

class Run(Process):
    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__()

    def run(self):
        os.system(self.cmd)

ps = []
for cmd in cmds:
    ps.append(Run(cmd))
    ps[-1].start()
    time.sleep(delay_time)

time.sleep(660)
os.system('python3 /root/ocrtoc_ws/src/ocrtoc_task/scripts/kill.py')