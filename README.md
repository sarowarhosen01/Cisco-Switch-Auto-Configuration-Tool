# Cisco Switch Auto-Configuration Tool

A Python script that automates the initial configuration of a Cisco Layer 2 switch using Telnet. Built with `asyncio` and `telnetlib3` for fast and reliable automation.

---

## ✨ Features

- **Automated Telnet Login** (with enable mode)
- **Hostname Configuration**
- **VLAN Creation** with meaningful names
- **Access Port Configuration** (FastEthernet 0/1–20)
- **Trunk Port Configuration** (GigabitEthernet 0/1)
- **Best Practices Applied**:
  - PortFast
  - BPDU Guard
  - Proper VLAN segmentation
- Fully asynchronous for better performance

---

## 📋 Configured VLANs

| VLAN ID | Name        | Purpose      | Ports Assigned       |
|---------|-------------|--------------|----------------------|
| 10      | MANAGEMENT  | Management   | Fa0/1 - 5            |
| 20      | USERS       | End Users    | Fa0/6 - 10           |
| 30      | SERVERS     | Servers      | Fa0/11 - 15          |
| 40      | VOICE       | Voice (IP Phones) | Fa0/16 - 20     |

**Trunk Port**: GigabitEthernet 0/1 (allows VLANs 10,20,30,40,99)

---

```
enable
configure terminal

enable secret cisco123

username admin password cisco123

interface GigabitEthernet 0/1
ip address 192.168.31.24 255.255.255.255.0
no shutdown
exit



line vty 0 4
login local
transport input telnet
exit
end

write memory
```

## 🛠️ Requirements

- Python 3.8+
- `telnetlib3` library

### Installation

```bash
pip install telnetlib3
