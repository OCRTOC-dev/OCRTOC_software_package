#! /usr/bin/env python3
# Author: Minghao Gou
import os
from multiprocessing import Process
from pathlib import Path
class Run(Process):
    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__()

    def run(self):
        os.system(self.cmd)

scenes = os.listdir('/root/ocrtoc_ws/src/ocrtoc_materials/scenes')
task_index_set = set()
for scene in scenes:
    task_index_set.add(scene.split('.')[0])
task_index_list = list(task_index_set)

evaluation_file_path = Path('/root/ocrtoc_ws/src/ocrtoc_task/evaluation')
an_index = '1-1-2'
print((evaluation_file_path/(an_index+'_grasp_detection.txt')).exists())

unevaluated_task_index_list = []
for task_index in task_index_list:
    if not (evaluation_file_path/(task_index+'_score.txt')).exists() or \
        not (evaluation_file_path/(task_index+'.yaml')).exists() or \
        not (evaluation_file_path/(task_index+'_grasp_detection.txt')).exists():
        unevaluated_task_index_list.append(task_index)

for task_index in unevaluated_task_index_list:
    p = Run('python3 /root/ocrtoc_ws/src/ocrtoc_task/scripts/run_single_simulation_task.py --task_index={}'.format(task_index))
    p.start()
    p.join()
    p.terminate()
