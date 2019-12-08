# -*- coding: utf-8 -*-
import os
from pathlib import Path
from otf2Parser.configuration import config
from otf2Parser.clock_properties import find_clock_time

def open_trace_metafile():
    traces_location = []
    trace_meta_file_path = Path(config.get('location').get('path'))
    with open(trace_meta_file_path, 'r') as trace_meta_file:
        traces_location = trace_meta_file.readlines()
    return traces_location

def open_trace_file():
    all_traces = []
    traces_location = open_trace_metafile()
    trace_output = Path(config.get('output').get('path'))
    clock_time = []
    for i in traces_location:
        clock_time.append(find_clock_time(i))
        trace_info = i.split('/')
        number_of_ranks = trace_info[7]
        trace_name = trace_info[6]
        Path(Path(trace_output, trace_name), number_of_ranks).mkdir(parents=True, exist_ok=True)
        ascii_trace_path = Path(Path(trace_output, trace_name), number_of_ranks)
        all_traces.append((ascii_trace_path, number_of_ranks))
        for j in range(int(number_of_ranks)):
            file_name = 'ascii_{}.out'.format(j)
            trace_ascii_loc = Path(ascii_trace_path, file_name)
            otf2_print_exec = config.get('executable').get('otf2_print')
            trace_ascii_loc_str = str(trace_ascii_loc)
            cmd = "{} -L {} {} > {}".format(otf2_print_exec, j, i.strip('\n'), trace_ascii_loc_str)
            os.system(cmd)     
    return all_traces, clock_time

All_traces_ascii = open_trace_file()