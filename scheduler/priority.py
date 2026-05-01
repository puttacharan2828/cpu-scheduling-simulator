def priority_non_preemptive(processes):
    processes = sorted(processes, key=lambda x: x["arrival"])

    ready_queue = []
    current_time = 0
    result = []
    gantt = []

    while processes or ready_queue:
        # Add arrived processes
        while processes and processes[0]["arrival"] <= current_time:
            ready_queue.append(processes.pop(0))

        if ready_queue:
            # Sort by priority (lower value = higher priority)
            ready_queue.sort(key=lambda x: x["priority"])
            p = ready_queue.pop(0)

            start_time = current_time
            completion_time = current_time + p["burst"]

            turnaround_time = completion_time - p["arrival"]
            waiting_time = turnaround_time - p["burst"]

            result.append({
                "pid": p["pid"],
                "arrival": p["arrival"],
                "burst": p["burst"],
                "priority": p["priority"],
                "completion": completion_time,
                "turnaround": turnaround_time,
                "waiting": waiting_time
            })

            gantt.append((p["pid"], start_time, completion_time))

            current_time = completion_time

        else:
            current_time += 1

    return result, gantt