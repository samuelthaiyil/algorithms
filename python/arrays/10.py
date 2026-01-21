def min_processing_time(processor_time, tasks):
    tasks.sort(reverse=True)
    processor_time.sort()

    max_time = 0

    for i in range(len(processor_time)):
        current_time = processor_time[i] + tasks[i * 4]
        max_time = max(max_time, current_time)
    
    return max_time

print(min_processing_time([8, 10], [2,2,3,1,8,7,4,5]))