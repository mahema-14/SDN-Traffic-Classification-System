# Screenshots of the Outputs
  ---

## 1) ping test for ICMP

<img width="955" height="910" alt="icmp_ping" src="https://github.com/user-attachments/assets/adde479f-beea-4dac-b85b-ae7ddcb24ded" />
<img width="955" height="910" alt="icmp_ping2" src="https://github.com/user-attachments/assets/639cf5af-0244-49ce-9161-03a7025ff73d" />

- Connectivity check – Ping confirms hosts can reach each other with no packet loss.
  
- Latency stats – RTT values show network delay and performance.
  
  ---

 ## 2) UDP traffic detection using iperf
 
 <img width="625" height="272" alt="image" src="https://github.com/user-attachments/assets/ab6ab2f9-14df-4d14-91da-3cb640422a10" />

 - UDP throughput check – iPerf confirms successful UDP transmission with measured bandwidth.

 - Quality metrics – Jitter and packet loss stats show stable and reliable performance.

   ---

 ## 3) TCP detection using netcat(nc)

 <img width="607" height="65" alt="image" src="https://github.com/user-attachments/assets/56021d96-2277-4f25-b485-f8849203efc6" />

 - TCP connectivity check – Netcat confirms reliable host-to-host communication over TCP.
 
 - Data transfer validation – Successful message exchange (hello) shows proper TCP packet detection.

   ---
     
 ## 4) Final Traffic logs

 <img width="620" height="474" alt="image" src="https://github.com/user-attachments/assets/5936ab13-f216-425e-acaf-7cca47933f54" />

 - Multi‑protocol classification – Controller detects TCP and UDP packets alongside ICMP.
 
 - Dynamic distribution – Percentages update in real time as traffic mix changes.



