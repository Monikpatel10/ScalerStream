# ⚡ ScalerStream

**ScalerStream** is a real-time log analytics platform designed for distributed systems. It ingests high-throughput log data via Kafka, processes and streams it using a Flask backend, and visualizes it through a responsive React dashboard. Built with scalability, observability, and fault-tolerance in mind.

![Architecture](https://img.shields.io/badge/status-in%20progress-yellow.svg)
![Tech](https://img.shields.io/badge/built%20with-Kafka%20%7C%20Flask%20%7C%20React%20%7C%20Kubernetes-blue)

---

## 📌 Features

- 🔄 Real-time ingestion of logs using **Apache Kafka**
- 🌐 WebSocket-based live streaming dashboard
- 📊 Interactive visualization of system logs and anomalies
- ☁️ Cloud-native deployment with **Docker** & **Kubernetes**
- 🧪 Monitoring with **Prometheus + Grafana**
- 💥 Scalable, distributed architecture with fault tolerance

---

## 🛠️ Tech Stack

| Layer         | Technology                              |
|---------------|------------------------------------------|
| Frontend      | React.js, WebSockets, D3.js              |
| Backend       | Python, Flask, Kafka, Redis              |
| Infrastructure| Docker, Kubernetes, AWS (EKS/EC2), NGINX |
| Data & Logs   | ELK Stack (Elasticsearch, Logstash, Kibana) |
| Monitoring    | Prometheus, Grafana                      |

---

## 🚀 Getting Started

### 📦 Prerequisites

- Docker & Docker Compose
- Kafka + Zookeeper (or Confluent Platform)
- Node.js + npm
- Python 3.9+

### 🔧 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app/main.py# ScalerStream

ScalerStream is a real-time log analytics platform for distributed systems.

## Features
- Kafka-based ingestion
- Flask + WebSockets backend
- React.js frontend dashboard
- Kubernetes deployment

## Running Locally
```bash
cd backend
pip install -r requirements.txt
python app/main.py
```

```bash
cd frontend
npm install
npm start
```
