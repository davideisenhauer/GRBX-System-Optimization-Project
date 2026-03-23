# GRBX-System-Optimization-Project
Developed a discrete-event simulation in Python (SimPy) to model GRBX user flow, analyze queue behavior, and evaluate system performance under varying demand scenarios. Conducted capacity analysis to identify bottlenecks, showing nonlinear performance degradation as utilization increased and reducing wait times by over 90% through optimization.

https://dje0015.myportfolio.com/grbx-system-optimization-project

## Overview
This project applies industrial engineering principles to model and analyze user flow within the GRBX platform. A discrete-event simulation was developed to evaluate system performance under varying demand and capacity conditions.

## Objective
To understand how increasing user demand impacts system performance and identify optimal capacity strategies to maintain efficiency.

## Methodology
1. Discrete-event simulation using SimPy
2. Modeled user arrivals and service times
3. Evaluated queue behavior and system performance metrics
4. Tested multiple demand and capacity scenarios

## Key Findings
1. System performs efficiently at low demand with minimal congestion
2. Performance degrades as utilization increases
3. Increasing capacity significantly reduces wait times and queue buildup
4. System exhibits nonlinear performance degradation near capacity limits

## Tools Used
- Python
- SimPy
- NumPy

## How to Run
```bash
git clone https://github.com/yourusername/GRBX-System-Optimization-Project.git
cd GRBX-System-Optimization-Project
pip install simpy
python grbx_simulation.py
