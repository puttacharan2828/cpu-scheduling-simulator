def round_robin(processes, time_quantum):
    from collections import deque

    processes = sorted(processes, key=lambda x: x["arrival"])

    queue = deque()
    current_time = 0
    i = 0
    n = len(processes)

    remaining_bt = {p["pid"]: p["burst"] for p in processes}
    completion_time = {}

    gantt = []

    while queue or i < n:
        # Add arrived processes
        while i < n and processes[i]["arrival"] <= current_time:
            queue.append(processes[i])
            i += 1

        if queue:
            p = queue.popleft()
            pid = p["pid"]

            exec_time = min(time_quantum, remaining_bt[pid])

            start_time = current_time
            current_time += exec_time
            remaining_bt[pid] -= exec_time

            gantt.append((pid, start_time, current_time))

            # Add newly arrived processes during execution
            while i < n and processes[i]["arrival"] <= current_time:
                queue.append(processes[i])
                i += 1

            # If not finished → push back
            if remaining_bt[pid] > 0:
                queue.append(p)
            else:
                completion_time[pid] = current_time

        else:
            current_time += 1

    # Calculate result
    result = []
    for p in processes:
        ct = completion_time[p["pid"]]
        tat = ct - p["arrival"]
        wt = tat - p["burst"]

        result.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "completion": ct,
            "turnaround": tat,
            "waiting": wt
        })

    return result, gantt