import streamlit as st
import pandas as pd

from scheduler.fcfs import fcfs_scheduling
from scheduler.sjf import sjf_non_preemptive
from scheduler.priority import priority_non_preemptive
from scheduler.round_robin import round_robin
from scheduler.srtf import srtf
from scheduler.priority_preemptive import priority_preemptive
from utils.gantt_chart import plot_gantt_chart

st.set_page_config(page_title="Process Scheduling Simulator", layout="wide")

st.title("🖥️ CPU Scheduling Simulator")
st.markdown("Easily simulate and compare different CPU scheduling algorithms.")

# =========================
# 🔹 SIDEBAR CONTROLS
# =========================
st.sidebar.header("⚙️ Input Settings")

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    [
        "FCFS",
        "SJF",
        "Priority (Non-Preemptive)",
        "Round Robin",
        "SRTF",
        "Priority (Preemptive)",
        "Compare All Algorithms"
    ]
)

num_processes = st.sidebar.number_input(
    "Number of Processes",
    min_value=1,
    step=1,
    value=1,
    key="num_proc"
)

time_quantum = None
if algorithm in ["Round Robin", "Compare All Algorithms"]:
    time_quantum = st.sidebar.number_input(
        "Time Quantum",
        min_value=1,
        value=2,
        key="tq"
    )

if st.sidebar.button("🔄 Reset"):
    st.session_state.clear()
    st.session_state["num_proc"] = 1
    st.session_state["tq"] = 2
    st.rerun()

# =========================
# 🔹 MAIN SCREEN
# =========================

# Scheduling Type Display
if algorithm in ["FCFS", "SJF", "Priority (Non-Preemptive)"]:
    st.info("🟦 Scheduling Type: Non-Preemptive")
elif algorithm != "Compare All Algorithms":
    st.info("🟧 Scheduling Type: Preemptive")

# =========================
# 🔹 INPUT TABLE
# =========================
st.subheader("📝 Enter Process Details")

data = pd.DataFrame({
    "PID": [f"P{i+1}" for i in range(num_processes)],
    "Arrival Time": [0]*num_processes,
    "Burst Time": [1]*num_processes
})

if "Priority" in algorithm or algorithm == "Compare All Algorithms":
    data["Priority"] = [1]*num_processes

edited_data = st.data_editor(data, use_container_width=True)

processes = []
for _, row in edited_data.iterrows():
    processes.append({
        "pid": row["PID"],
        "arrival": int(row["Arrival Time"]),
        "burst": int(row["Burst Time"]),
        "priority": int(row["Priority"]) if "Priority" in row else None
    })

# =========================
# 🔥 RUN BUTTON
# =========================
run_clicked = st.button("🚀 Run Simulation", use_container_width=True)

# =========================
# 🔹 RUN LOGIC
# =========================
if run_clicked:
    st.success(f"Running {algorithm}")

    # =========================
    # 🔥 COMPARISON MODE
    # =========================
    if algorithm == "Compare All Algorithms":

        results = {}

        results["FCFS"], _ = fcfs_scheduling(processes)
        results["SJF"], _ = sjf_non_preemptive(processes)
        results["SRTF"], _ = srtf(processes)

        tq = time_quantum if time_quantum else 2
        results["Round Robin"], _ = round_robin(processes, tq)

        results["Priority NP"], _ = priority_non_preemptive(processes)
        results["Priority P"], _ = priority_preemptive(processes)

        comparison = []

        for algo_name, res in results.items():
            df = pd.DataFrame(res)

            comparison.append({
                "Algorithm": algo_name,
                "Avg Waiting Time": df["waiting"].mean(),
                "Avg Turnaround Time": df["turnaround"].mean()
            })

        comp_df = pd.DataFrame(comparison)

        st.markdown("## 🆚 Algorithm Performance Comparison")
        st.dataframe(comp_df, use_container_width=True)

        best = comp_df.loc[comp_df["Avg Waiting Time"].idxmin()]
        st.success(f"🏆 Best Performing Algorithm: {best['Algorithm']} (Lowest Waiting Time)")

    # =========================
    # 🔥 NORMAL MODE
    # =========================
    else:

        if algorithm == "FCFS":
            result, gantt = fcfs_scheduling(processes)

        elif algorithm == "SJF":
            result, gantt = sjf_non_preemptive(processes)

        elif algorithm == "Priority (Non-Preemptive)":
            result, gantt = priority_non_preemptive(processes)

        elif algorithm == "Round Robin":
            result, gantt = round_robin(processes, time_quantum)

        elif algorithm == "SRTF":
            result, gantt = srtf(processes)

        elif algorithm == "Priority (Preemptive)":
            result, gantt = priority_preemptive(processes)

        input_df = pd.DataFrame(processes).fillna("-")
        result_df = pd.DataFrame(result)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📥 Input Summary")
            st.dataframe(input_df, use_container_width=True)

        with col2:
            st.markdown("### 📊 Computed Results")
            st.dataframe(result_df, use_container_width=True)

        # Gantt Chart
        st.markdown("### 📈 Execution Timeline (Gantt Chart)")
        fig = plot_gantt_chart(gantt)
        st.pyplot(fig)

        # Metrics
        total_wt = result_df['waiting'].sum()
        total_tat = result_df['turnaround'].sum()

        st.markdown("### 📊 Performance Metrics")

        col1, col2 = st.columns(2)
        col1.metric("Total Waiting Time", total_wt)
        col2.metric("Total Turnaround Time", total_tat)

        col1, col2 = st.columns(2)
        col1.metric("Average Waiting Time", f"{total_wt / len(result_df):.2f}")
        col2.metric("Average Turnaround Time", f"{total_tat / len(result_df):.2f}")

        # Best TQ Suggestion
        if algorithm == "Round Robin":

            st.divider()
            st.markdown("### ⚙️ Best Time Quantum Suggestion")

            tq_results = []

            for tq_test in range(1, 11):
                rr_result, _ = round_robin(processes, tq_test)
                df_rr = pd.DataFrame(rr_result)

                tq_results.append({
                    "TQ": tq_test,
                    "Avg WT": df_rr["waiting"].mean(),
                    "Avg TAT": df_rr["turnaround"].mean()
                })

            tq_df = pd.DataFrame(tq_results)
            best_row = tq_df.loc[tq_df["Avg WT"].idxmin()]

            col1, col2, col3 = st.columns(3)
            col1.metric("Best TQ", int(best_row["TQ"]))
            col2.metric("Avg WT (Best TQ)", f"{best_row['Avg WT']:.2f}")
            col3.metric("Avg TAT (Best TQ)", f"{best_row['Avg TAT']:.2f}")

# =========================
# 🔹 HELP SECTION
# =========================
with st.expander("ℹ️ How to Use This Tool"):
    st.write("""
    1. Select an algorithm from the sidebar  
    2. Enter process details in the table  
    3. Click 'Run Simulation'  
    4. View results and Gantt chart  
    5. Use 'Compare All Algorithms' to find the best one  
    """)