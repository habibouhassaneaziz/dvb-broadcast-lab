\# DVB-S Broadcast Simulation Lab



\## Overview



This project simulates a simplified \*\*DVB-S (Digital Video Broadcasting - Satellite)\*\* transmission chain using Python.



The goal is to understand how IP data can be transmitted through a satellite broadcast system using \*\*MPEG Transport Stream (MPEG-TS)\*\* packets.



The simulation reproduces the main stages of a DVB-S transmission:



IP Stream → MPEG-TS Encapsulation → Simulated Satellite Channel → Decapsulation → IP Recovery



---



\## Architecture



The simulated transmission pipeline is:



IP Data

↓

Encapsulation into MPEG-TS packets

↓

Satellite Channel Simulation

↓

Packet Loss / Bit Errors

↓

MPEG-TS Decapsulation

↓

Reconstructed IP Stream



---



\## Implemented Components



\### 1. DVB-S Encapsulation



IP data is encapsulated into \*\*MPEG Transport Stream packets (188 bytes)\*\*.



Key parameters:



\- Sync byte: 0x47

\- PID for data packets

\- Continuity counter

\- Fixed TS packet size



File:



dvbs\_simulation.py



---



\### 2. Satellite Channel Simulation



A simplified satellite link is simulated including:



\- Packet loss

\- Bit errors

\- Transmission conditions



File:



satellite\_channel.py



---



\### 3. Network Metrics



The project includes measurement of important \*\*network performance metrics\*\*.



Examples:



\- Packet Loss Rate

\- Bit Error Count

\- Packets Sent

\- Packets Received

\- Effective Loss Rate



These metrics help analyze how the simulated satellite channel affects the transmitted data.



File:



metrics.py



Example output:



Packets sent: 100  

Packets received: 90  

Packets lost: 10  

Effective loss rate: 10%



---



\## Automated Testing



Automated tests are implemented using \*\*pytest\*\*.



The tests verify:



\- Correct encapsulation of IP data

\- Correct reconstruction after decapsulation

\- Transmission behavior under packet loss



Tests location:



tests/test\_transmission.py



Run tests locally:





---



\## CI/CD Pipeline



This project includes a \*\*GitHub Actions CI pipeline\*\*.



The pipeline automatically:



1\. Checks out the repository

2\. Installs Python

3\. Installs pytest

4\. Runs the test suite



The pipeline is triggered automatically on every push to the repository.



Location:



.github/workflows/main.yml



---



\## Technologies Used



\- Python

\- MPEG-TS

\- Git

\- GitHub

\- GitHub Actions

\- pytest



---



\## Learning Objectives



This project was created to better understand:



\- DVB-S broadcast transmission

\- MPEG Transport Stream encapsulation

\- Satellite communication constraints

\- Network performance metrics

\- CI/CD integration for software projects



---



\## Author



Abdoul Aziz Habibou  

Network \& Telecommunications Engineer

