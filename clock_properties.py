# -*- coding: utf-8 -*-
import subprocess
import re
from pathlib import Path



Re_clock_properties = 'CLOCK_PROPERTIES\s+Ticks\sper\sSeconds:\s+(\d+),\sGlobal\sOffset:\s(\d+),\sLength:\s(\d+)\n'
Tracer_clock_properties = re.compile(Re_clock_properties)


def find_clock_time(path):
    cmd = 'otf2-print -G {}'.format(path)
    Contents = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    Result_clock_properties = Tracer_clock_properties.findall(Contents.stdout.decode('utf-8'))
    return Result_clock_properties
