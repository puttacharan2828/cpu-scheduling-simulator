import matplotlib.pyplot as plt

def plot_gantt_chart(gantt):
    fig, ax = plt.subplots(figsize=(10, 2))

    # ✅ ADD DARK BACKGROUND HERE
    ax.set_facecolor('#111111')
    fig.patch.set_facecolor('#111111')

    for (pid, start, end) in gantt:
        ax.barh(0, end - start, left=start)
        ax.text((start + end) / 2, 0, pid,
                va='center', ha='center', color='white', fontsize=10)

    ax.set_xlabel("Time", color="white")
    ax.set_yticks([])

    # Make axis text white (so visible on dark bg)
    ax.tick_params(colors='white')

    # Remove borders for clean UI
    for spine in ax.spines.values():
        spine.set_visible(False)

    return fig