# -*- coding: utf-8 -*-
import re
import pandas as pd
from otf2Parser.otf2_2_ascii import All_traces_ascii
from pathlib import Path

 



def event_time(tracepath):
    Tracer_loop_time = 0
    Tracer_walltime_time = 0
    Isend_time = 0
    Irecv_time = 0
    Waitall_time = 0
    Alltoall_time = 0
    Waitany_time = 0
    Allreduce_time = 0
    Reduce_time = 0
    Barrier_time = 0
    Testany_time = 0
    
    loop_init_time = 0
    loop_final_time = 0
    
    Contents = Path(tracepath).read_text()
    
    Re_Tracer_loop_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"TRACER_Loop"\s+<(\d+)>\n'
    Re_Tracer_loop_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"TRACER_Loop"\s+<(\d+)>\n'
    Re_Tracer_walltime_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"TRACER_WallTime_stencil4d"\s+<(\d+)>\n'
    Re_Tracer_walltime_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"TRACER_WallTime_stencil4d"\s+<(\d+)>\n'
    Re_Tracer_walltime_a2a_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"TRACER_WallTime_a2a"\s+<(\d+)>\n'
    Re_Tracer_walltime_a2a_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"TRACER_WallTime_a2a"\s+<(\d+)>\n'
    Re_Isend_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Isend"\s+<(\d+)>\n'
    Re_Isend_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Isend"\s+<(\d+)>\n'
    Re_Irecv_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Irecv"\s+<(\d+)>\n'
    Re_Irecv_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Irecv"\s+<(\d+)>\n'
    Re_waitall_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Waitall"\s+<(\d+)>\n'
    Re_waitall_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Waitall"\s+<(\d+)>\n'
    Re_alltoall_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Alltoall"\s+<(\d+)>\n'
    Re_alltoall_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Alltoall"\s+<(\d+)>\n'
    Re_waitany_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Waitany"\s+<(\d+)>\n'
    Re_waitany_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Waitany"\s+<(\d+)>\n'
    Re_allreduce_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Allreduce"\s+<(\d+)>\n'
    Re_allreduce_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Allreduce"\s+<(\d+)>\n'
    Re_reduce_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Reduce"\s+<(\d+)>\n'
    Re_reduce_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Reduce"\s+<(\d+)>\n'
    Re_barrier_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Barrier"\s+<(\d+)>\n'
    Re_barrier_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Barrier"\s+<(\d+)>\n'
    Re_testany_enter = 'ENTER\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Testany"\s+<(\d+)>\n'
    Re_testany_leave = 'LEAVE\s*(\d+)\s*(\d+)\s*Region:\s+"MPI_Testany"\s+<(\d+)>\n'
    
    Tracer_loop_enter = re.compile(Re_Tracer_loop_enter)
    Tracer_loop_leave = re.compile(Re_Tracer_loop_leave)
    Tracer_walltime_enter = re.compile(Re_Tracer_walltime_enter)
    Tracer_walltime_leave = re.compile(Re_Tracer_walltime_leave)
    Isend_enter = re.compile(Re_Isend_enter)
    Isend_leave = re.compile(Re_Isend_leave)
    Irecv_enter = re.compile(Re_Irecv_enter)
    Irecv_leave = re.compile(Re_Irecv_leave)
    Waitall_enter = re.compile(Re_waitall_enter)
    Waitall_leave = re.compile(Re_waitall_leave)
    Alltoall_enter = re.compile(Re_alltoall_enter)
    Alltoall_leave = re.compile(Re_alltoall_leave)
    Waitany_enter = re.compile(Re_waitany_enter)
    Waitany_leave = re.compile(Re_waitany_leave)
    Allreduce_enter = re.compile(Re_allreduce_enter)
    Allreduce_leave = re.compile(Re_allreduce_leave)
    Reduce_enter = re.compile(Re_reduce_enter)
    Reduce_leave = re.compile(Re_reduce_leave)
    Barrier_enter = re.compile(Re_barrier_enter)
    Barrier_leave = re.compile(Re_barrier_leave)
    Testany_enter = re.compile(Re_testany_enter)
    Testany_leave = re.compile(Re_testany_leave)
    
    Result_Tracer_loop_enter = Tracer_loop_enter.findall(Contents)
    Result_Tracer_loop_leave = Tracer_loop_leave.findall(Contents)
    Result_Tracer_walltime_enter = Tracer_walltime_enter.findall(Contents)
    Result_Tracer_walltime_leave = Tracer_walltime_leave.findall(Contents)
    Result_Isend_enter = Isend_enter.findall(Contents)
    Result_Isend_leave = Isend_leave.findall(Contents)
    Result_Irecv_enter = Irecv_enter.findall(Contents)
    Result_Irecv_leave = Irecv_leave.findall(Contents)
    Result_waitall_enter = Waitall_enter.findall(Contents)
    Result_waitall_leave = Waitall_leave.findall(Contents)   
    Result_Alltoall_enter = Alltoall_enter.findall(Contents)
    Result_Alltoall_leave = Alltoall_leave.findall(Contents)
    Result_Waitany_enter = Waitany_enter.findall(Contents)
    Result_Waitany_leave = Waitany_leave.findall(Contents)
    Result_Allreduce_enter = Allreduce_enter.findall(Contents)
    Result_Allreduce_leave = Allreduce_leave.findall(Contents)
    Result_Reduce_enter = Reduce_enter.findall(Contents)
    Result_Reduce_leave = Reduce_leave.findall(Contents)
    Result_Barrier_enter = Barrier_enter.findall(Contents)
    Result_Barrier_leave = Barrier_leave.findall(Contents)
    Result_Testany_enter = Testany_enter.findall(Contents)
    Result_Testany_leave = Testany_leave.findall(Contents)
    
    
    if(len(Result_Tracer_loop_leave) == len(Result_Tracer_loop_enter)) and (len(Result_Tracer_loop_enter) == 1):
        Tracer_loop_time = int(Result_Tracer_loop_leave[0][1]) - int(Result_Tracer_loop_enter[0][1])
        loop_init_time = int(Result_Tracer_loop_enter[0][1])
        loop_final_time = int(Result_Tracer_loop_leave[0][1])
    else:
        print("Tracer loop not recorded correctly")
        
    if(len(Result_Tracer_walltime_leave) == len(Result_Tracer_walltime_enter)) \
    and (len(Result_Tracer_walltime_enter) == 1) \
    and loop_init_time <= int(Result_Tracer_walltime_leave[0][1]) <= loop_final_time \
    and loop_init_time <= int(Result_Tracer_walltime_enter[0][1]) <= loop_final_time:
        Tracer_walltime_time = int(Result_Tracer_walltime_leave[0][1]) - int(Result_Tracer_walltime_enter[0][1])
        
    if(len(Result_Isend_enter) == len(Result_Isend_leave)) and (len(Result_Isend_enter) > 0):
        for i, j in enumerate(zip(Result_Isend_leave, Result_Isend_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Isend_time += (int(j[0][1]) - int(j[1][1]))
            
    if(len(Result_Irecv_enter) == len(Result_Irecv_leave)) and (len(Result_Irecv_enter) > 0):
        for i, j in enumerate(zip(Result_Irecv_leave, Result_Irecv_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Irecv_time += (int(j[0][1]) - int(j[1][1]))

    if(len(Result_waitall_enter) == len(Result_waitall_leave)) and (len(Result_waitall_enter) > 0):
        for i, j in enumerate(zip(Result_waitall_leave, Result_waitall_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Waitall_time += (int(j[0][1]) - int(j[1][1]))
    
    if(len(Result_Alltoall_enter) == len(Result_Alltoall_leave)) and (len(Result_Alltoall_enter) > 0):
        for i, j in enumerate(zip(Result_Alltoall_leave, Result_Alltoall_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Alltoall_time += (int(j[0][1]) - int(j[1][1]))
                
    if(len(Result_Waitany_enter) == len(Result_Waitany_leave)) and (len(Result_Waitany_enter) > 0):
        for i, j in enumerate(zip(Result_Waitany_leave, Result_Waitany_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Waitany_time += (int(j[0][1]) - int(j[1][1]))
                
    if(len(Result_Allreduce_enter) == len(Result_Allreduce_leave)) and (len(Result_Allreduce_enter) > 0):
        for i, j in enumerate(zip(Result_Allreduce_leave, Result_Allreduce_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Allreduce_time += (int(j[0][1]) - int(j[1][1]))
                
    if(len(Result_Reduce_enter) == len(Result_Reduce_leave)) and (len(Result_Reduce_enter) > 0):
        for i, j in enumerate(zip(Result_Reduce_leave, Result_Reduce_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Reduce_time += (int(j[0][1]) - int(j[1][1]))
                
    if(len(Result_Barrier_enter) == len(Result_Barrier_leave)) and (len(Result_Barrier_enter) > 0):
        for i, j in enumerate(zip(Result_Barrier_leave, Result_Barrier_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Barrier_time += (int(j[0][1]) - int(j[1][1]))
                
    if(len(Result_Testany_enter) == len(Result_Testany_leave)) and (len(Result_Testany_enter) > 0):
        for i, j in enumerate(zip(Result_Testany_leave, Result_Testany_enter)):
            if loop_init_time <= int(j[0][1]) <= loop_final_time and loop_init_time <= int(j[1][1]) <= loop_final_time:
                Testany_time += (int(j[0][1]) - int(j[1][1]))
            
    return {'Tracer_loop_time': Tracer_loop_time,
            'Tracer_walltime_time': Tracer_walltime_time,
            'Isend_time': Isend_time,
            'Irecv_time': Irecv_time,
            'Waitall_time': Waitall_time,
            'Alltoall_time': Alltoall_time,
            'Waitany_time': Waitany_time,
            'Allreduce_time': Allreduce_time,
            'Reduce_time': Reduce_time,
            'Barrier_time': Barrier_time,
            'Testany_time': Testany_time}

def read_otf():
    traceName = []
    ticksPerSecond = []
    tracerLoopTime = []
    communicationTime = []
    computationTime = []
    percentageOfCommunication = []
    for num, i in enumerate(All_traces_ascii[0]):
        print('Trace Name : {}'.format(str(i[0])))
        Tracer_loop_time_total = 0
        Tracer_walltime_time_total = 0
        Isend_time_total = 0
        Irecv_time_total = 0
        Waitall_time_totat = 0  
        Alltoall_time_total = 0
        Waitany_time_total = 0
        Allreduce_time_total = 0
        Reduce_time_total = 0
        Barrier_time_total = 0
        Testany_time_total = 0
        for j in range(int(i[1])):
            File_name = 'ascii_{}.out'.format(j)
            Time_event_dict = event_time(Path(i[0], File_name))
#            print(Time_event_dict)
            Tracer_loop_time_total += Time_event_dict.get('Tracer_loop_time')
            Tracer_walltime_time_total += Time_event_dict.get('Tracer_walltime_time')
            Isend_time_total += Time_event_dict.get('Isend_time')
            Irecv_time_total += Time_event_dict.get('Irecv_time')
            Waitall_time_totat += Time_event_dict.get('Waitall_time')
            Alltoall_time_total += Time_event_dict.get('Alltoall_time')
            Waitany_time_total += Time_event_dict.get('Waitany_time')
            Allreduce_time_total += Time_event_dict.get('Allreduce_time')
            Reduce_time_total += Time_event_dict.get('Reduce_time')
            Barrier_time_total += Time_event_dict.get('Barrier_time')
            Testany_time_total += Time_event_dict.get('Testany_time')
        Ticks_per_second = int(All_traces_ascii[1][num][0][0])
#        print('Ticks per second : {}'.format(Ticks_per_second))
        comm_time = Isend_time_total + Irecv_time_total + Waitall_time_totat + Alltoall_time_total + Waitany_time_total +Allreduce_time_total + Reduce_time_total + Barrier_time_total + Testany_time_total
#        print('Tracer loop time : {}'.format( Tracer_loop_time_total / Ticks_per_second ))
#        print('Communication time : {}'.format( comm_time / Ticks_per_second ))
#        print('Computation time : {}'.format( (Tracer_loop_time_total - comm_time) / Ticks_per_second ))
#        print('Percentage of computation : {}'.format((Tracer_loop_time_total - comm_time)/Tracer_loop_time_total * 100))
        traceName.append(str(i[0]))
        ticksPerSecond.append(int(All_traces_ascii[1][num][0][0]))
        tracerLoopTime.append(Tracer_loop_time_total / Ticks_per_second)
        communicationTime.append(comm_time / Ticks_per_second)
        computationTime.append((Tracer_loop_time_total - comm_time) / Ticks_per_second)
        percentageOfCommunication.append((Tracer_loop_time_total - comm_time)/Tracer_loop_time_total * 100)
    df = pd.DataFrame({
    'Trace Name': traceName,
    'Ticks per second': ticksPerSecond
    })
    print(df)

read_otf()
