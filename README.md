# RAS-Swiftros

**RAS-Swiftros** is a modular ROS 2-based mobile robot developed as part of the **RAS Junior Program** at IEEE RAS Javeriana, Pontificia Universidad Javeriana (Bogotá, Colombia). The project introduces students to robotics through hands-on experience using ROS 2, from simulation to real-world hardware integration.

## 🤖 Introduction

RAS-Swiftros is an educational differential-drive mobile robot capable of performing basic autonomous navigation tasks using reactive obstacle avoidance. It was designed and built by first-year students in Mechatronics, Electronics, and Systems Engineering as a platform for learning the full development cycle of a robot using ROS 2.

The robot uses an ESP32 microcontroller for low-level control, integrates sensors for obstacle detection, and communicates with ROS 2 nodes running on a host machine. Simulation is done with `turtlesim`, and code is written in Python for the ROS 2 packages.

This project prioritizes **learning-by-doing**, introducing students to publisher/subscriber patterns, services, firmware deployment, and system integration.

---

## 🧩 Folder Structure

```
RAS-Swiftros/
├── esp_firmware/              --> Code for the ESP32 microcontroller
│   ├── esp_firmware/
│   ├── resource/
│   ├── test/
│   ├── package.xml
│   ├── setup.cfg
│   └── setup.py
│
├── ras2_services/             --> ROS 2 nodes that control robot behavior
│   ├── ras2_services/
│   ├── resource/
│   ├── test/
│   ├── package.xml
│   ├── setup.cfg
│   └── setup.py
│
├── ros2_communication/        --> Handles serial data between ROS and hardware
│   ├── ros2_communication/
│   ├── resource/
│   ├── test/
│   ├── package.xml
│   ├── setup.cfg
│   └── setup.py
│
├── media/                     --> (Optional) Images and videos for documentation
│   └── robot_demo.gif
│
└── README.md                  --> Project documentation
```

---

## 🚀 How to Run

### Requirements

- ROS 2 Humble  
- Python 3.8+  
- Arduino IDE or PlatformIO  
- USB connection to ESP32  
- `pyserial` Python package  

### 1. Upload Firmware to ESP32

```bash
cd esp_firmware/
pio run --target upload
```

### 2. Source ROS 2 and Run the Nodes

```bash
source /opt/ros/humble/setup.bash

# Run ROS 2 services and communication nodes
ros2 run ras2_services movement_service.py
ros2 run ros2_communication serial_node.py
```

---

## ⚙️ ROS 2 Architecture

```
[ROS 2 Service Node] ---> [Serial Node] ---> [ESP32 Firmware] ---> [Motors]
                                       ↑                         ↓
                                [Sensors feedback] <-------------
```

---

## 🎯 Educational Objective

This project was developed by Junior 1 students with the goal of understanding:

- ROS 2 architecture (nodes, services, pub/sub)
- Microcontroller communication via serial (ESP32)
- Real-time sensor feedback
- System integration from simulation (Turtlesim) to real hardware

It serves as a foundation for further robotics development and contributions to the ROS ecosystem.

---

## 🖼️ Media

![Robot Prototype](media/robot_demo.gif)

> Add more images or videos in the `media/` folder for visual documentation.

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 RAS-JAVERIANA-KEVIN-FONSECA

```


---

## 👥 Contributors

Developed by students of the **RAS Junior Program** – IEEE RAS Javeriana  
Pontificia Universidad Javeriana – Bogotá, Colombia  
Mechatronics, Electronics, and Systems Engineering – 3rd semester

> Submitted as part of the ROSCon 2025 Bursary Application
