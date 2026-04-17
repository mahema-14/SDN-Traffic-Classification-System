# 🚦 Traffic Classification System using SDN

## 📌 Problem Statement
To classify network traffic based on protocol type (TCP, UDP, ICMP) using Software Defined Networking (SDN) with Mininet and POX controller.

---

## 🎯 Objectives
- Identify TCP, UDP, and ICMP packets  
- Maintain real-time traffic statistics  
- Display classification results  
- Analyze traffic distribution  

---

## 🛠️ Tools & Technologies
- Mininet (Network Simulation)
- POX Controller (SDN Controller)
- Python
- OpenFlow Protocol

---

## 🧠 System Architecture
Hosts → Switch → Controller (POX)

- Switch forwards packets to controller  
- Controller inspects packets and makes decisions  

---

## ⚙️ Methodology
1. Packet arrives at switch  
2. Switch sends packet to controller (Packet-In)  
3. Controller extracts IPv4 protocol field  
4. Classifies traffic:
   - TCP → Protocol 6  
   - UDP → Protocol 17  
   - ICMP → Protocol 1  
5. Updates counters and statistics  
6. Calculates percentage distribution  
7. Installs flow rules (match-action) in switch  

---

## 🚀 Features
- Real-time packet classification  
- Traffic statistics tracking  
- Percentage-based traffic distribution  
- Dynamic flow rule installation  
- Supports TCP, UDP, ICMP traffic  

---

## 🧪 Testing & Results

### ✅ ICMP (Ping)
- Command: `h1 ping h2`
- Observed latency and ICMP detection

### ✅ TCP Traffic
- Command: `nc`
- Successfully detected TCP packets

### ✅ UDP Traffic
- Command: `iperf`
- Measured throughput and detected UDP packets

---

## 📊 Output
- Packet logs (TCP, UDP, ICMP detection)  
- Statistics:
  - Total packet counts  
- Traffic distribution:
  - Percentage of each protocol  

---

## 📸 Screenshots
(See `/screenshots.md` folder for outputs)

---

## 📈 Performance Analysis
- Latency measured using ping  
- Throughput measured using iperf  
- Flow rules observed using `dpctl dump-flows`  

---

## ✅ Conclusion
The system successfully classifies network traffic using SDN principles, maintains statistics, and analyzes traffic distribution efficiently.

---

## 🔮 Future Scope
- GUI dashboard for visualization  
- Machine learning-based traffic analysis  
- Intrusion detection system integration  

---

## 👨‍💻 Author
P Mahema Sai
