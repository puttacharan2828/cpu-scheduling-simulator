def priority_preemptive(processes):
    processes = sorted(processes, key=lambda x: x["arrival"])

    n = len(processes)
    remaining_bt = {p["pid"]: p["burst"] for p in processes}
    completion_time = {}

    current_time = 0
    completed = 0

    gantt = []
    last_pid = None

    while completed < n:
        # Get available processes
        available = [
            p for p in processes
            if p["arrival"] <= current_time and remaining_bt[p["pid"]] > 0
        ]

        if available:
            # Select highest priority (lower number = higher priority)
            p = min(available, key=lambda x: x["priority"])
            pid = p["pid"]

            # Gantt handling
            if last_pid != pid:
                gantt.append([pid, current_time, current_time + 1])
            else:
                gantt[-1][2] += 1

            remaining_bt[pid] -= 1
            current_time += 1
            last_pid = pid

            if remaining_bt[pid] == 0:
                completion_time[pid] = current_time
                completed += 1

        else:
            current_time += 1

    # Format Gantt
    gantt_final = [(p, s, e) for p, s, e in gantt]

    # Results
    result = []
    for p in processes:
        ct = completion_time[p["pid"]]
        tat = ct - p["arrival"]
        wt = tat - p["burst"]

        result.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "priority": p["priority"],
            "completion": ct,
            "turnaround": tat,
            "waiting": wt
        })

    return result, gantt_final