Custom Process Scheduling Simulator
Overview

The Custom Process Scheduling Simulator is an interactive application designed to visualize and compare different CPU scheduling algorithms. It helps users understand how processes are scheduled in an operating system through graphical representation and performance metrics.

Features
Implementation of multiple CPU scheduling algorithms:
First Come First Serve (FCFS)
Shortest Job First (SJF - Non Preemptive)
Shortest Remaining Time First (SRTF)
Priority Scheduling (Preemptive and Non Preemptive)
Round Robin
Gantt chart visualization for process execution
Calculation of key metrics:
Waiting Time
Turnaround Time
Comparison of all algorithms in a single view
Simple and interactive user interface


Technologies Used
Python
Streamlit
Pandas
Matplotlib


Project Structure
project-folder/
│── app.py
│── run_app.bat
│── requirements.txt
│── README.md
│
├── scheduler/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── srtf.py
│   ├── round_robin.py
│   ├── priority.py
│   ├── priority_preemptive.py
│
└── utils/
    ├── gantt.py


Installation and Setup

Follow these steps to set up the project on your system:

1. Install Python (if not already installed)
Download and install Python
While installing, enable "Add Python to PATH"
2. Verify Python Installation

Open Command Prompt or Terminal and run:

python --version

If Python is installed correctly, it will display the version number.

3. Install Required Libraries

Navigate to your project folder and run:

pip install -r requirements.txt

If the above command does not work, install libraries one by one:

pip install streamlit
pip install pandas
pip install matplotlib
4. Verify Installation (Optional)
streamlit --version
Run Application

You can run the project using any of the following methods:

Option 1: Using Command Line
streamlit run app.py

Option 2: Using Batch File (Easy Method)
Double-click the run_app.bat file
The application will automatically open in your browser

Usage
Enter process details such as arrival time, burst time, and priority
Select a scheduling algorithm
View the Gantt chart and performance metrics
Compare results across different algorithms
Objective

The main objective of this project is to provide a practical understanding of CPU scheduling concepts and help students visualize how different algorithms behave under various conditions.

Future Improvements
Add more scheduling algorithms
Enhance UI design
Include export options for results
Add real-time simulation controls
Conclusion

This simulator serves as an educational tool for students to explore and analyze CPU scheduling techniques in an interactive and visual manner.

Author

BTech Data Science Student