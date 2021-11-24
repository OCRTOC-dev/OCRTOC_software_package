#! /usr/bin/env python3
# Author: Minghao Gou
import os

result = os.popen('ps -x')
res = result.read()
lines = res.splitlines()
p_command = lines[0].find('COMMAND')
kill_prefix_list = ['python ','python3 ','sh ', '/usr/bin/python ','python2', '/opt/ros/melodic/lib/']
print('\033[031m')
for line in lines[1:]:
    pid = line.strip().split()[0]
    cmd = line[p_command:]
    print('pid:{} cmd:{}'.format(pid, cmd))
    for kill_prefix in kill_prefix_list:
        if cmd.startswith(kill_prefix) and not cmd.endswith('kill.py') and not 'run_all_simulation_task.py' in cmd:
            print('kill {}'.format(pid))
            os.kill(int(pid), 9)
            break
print('\033[0m')