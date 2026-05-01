# 🖥️ CPU Scheduling Simulator

## 📌 Overview

The **CPU Scheduling Simulator** is an interactive web-based tool that helps users understand and visualize different CPU scheduling algorithms used in operating systems.

It allows users to input custom processes and compare how different algorithms perform based on waiting time and turnaround time.

---

## 🚀 Features

* ✅ Supports multiple scheduling algorithms:

  * First Come First Serve (FCFS)
  * Shortest Job First (SJF)
  * Shortest Remaining Time First (SRTF)
  * Round Robin (RR)
  * Priority Scheduling (Preemptive & Non-Preemptive)

* 📊 Compare all algorithms at once

* 📈 Visual Gantt Chart representation

* ⚙️ Adjustable Time Quantum for Round Robin

* 📝 Easy process input using table interface

* 📉 Performance metrics:

  * Waiting Time
  * Turnaround Time

---

## 🧠 Algorithms Included

| Algorithm   | Type                        |
| ----------- | --------------------------- |
| FCFS        | Non-Preemptive              |
| SJF         | Non-Preemptive              |
| SRTF        | Preemptive                  |
| Round Robin | Preemptive                  |
| Priority    | Preemptive & Non-Preemptive |

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib

---

## ▶️ How to Run Locally

1. Install required libraries:

```
pip install -r requirements.txt
```

2. Run the application:

```
streamlit run app.py
```

3. Open in browser:

```
http://localhost:8501
```

---

## 🌐 Deployment

This project can be deployed using Streamlit Community Cloud for online access.

---

## 🎯 Use Cases

* Learning CPU scheduling algorithms
* Classroom demonstrations
* Lab experiments
* Algorithm comparison and analysis

---

## 👨‍💻 Author

Developed as part of a B.Tech Data Science project (CBP).

---

## 🙏 Acknowledgment

Special thanks to faculty for guidance and support in completing this project.

---

## 📌 Future Enhancements

* Add more scheduling algorithms
* Export results as CSV/PDF
* Improve UI/UX design
* Add step-by-step execution visualization

---

## ⭐ Conclusion

This simulator simplifies complex scheduling concepts by providing an interactive and visual learning experience, making it useful for both students and educators.
