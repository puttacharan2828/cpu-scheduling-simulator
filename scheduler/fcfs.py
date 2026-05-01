def fcfs_scheduling(processes):
    # Sort by arrival time
    processes = sorted(processes, key=lambda x: x["arrival"])

    current_time = 0
    result = []
    gantt = []

    for p in processes:
        start_time = max(current_time, p["arrival"])
        completion_time = start_time + p["burst"]

        turnaround_time = completion_time - p["arrival"]
        waiting_time = turnaround_time - p["burst"]

        result.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "completion": completion_time,
            "turnaround": turnaround_time,
            "waiting": waiting_time
        })

        gantt.append((p["pid"], start_time, completion_time))

        current_time = completion_time

    return result, gantt