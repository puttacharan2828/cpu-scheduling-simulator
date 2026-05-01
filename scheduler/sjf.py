def sjf_non_preemptive(processes):
    processes = sorted(processes, key=lambda x: x["arrival"])

    completed = []
    ready_queue = []
    current_time = 0
    gantt = []
    result = []

    while processes or ready_queue:
        # Add arrived processes to ready queue
        while processes and processes[0]["arrival"] <= current_time:
            ready_queue.append(processes.pop(0))

        if ready_queue:
            # Select process with smallest burst time
            ready_queue.sort(key=lambda x: x["burst"])
            p = ready_queue.pop(0)

            start_time = current_time
            completion_time = current_time + p["burst"]

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

        else:
            # If no process is ready, jump time
            current_time += 1

    return result, gantt