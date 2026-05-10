import nmap
import json
import os

def start_med_scan(target_ip):
    print(f"[*] 医疗资产探测流水线启动...")
    print(f"[*] 正在扫描网段: {target_ip}")
    
    # 初始化扫描引擎
    nm = nmap.PortScanner()
    
    try:
        # 核心参数解释：
        # -sV: 版本侦测 (辨别是哪种医疗系统)
        # -T4: 设置扫描速度（1-5，4属于中规中矩，兼顾速度与稳定性）
        # -p : 扫描医疗专用端口 (104:DICOM影像, 6661:HL7通讯, 445:SMB高危端口)
        nm.scan(hosts=target_ip, arguments='-sV -T4 --open -p 80,445,135,104,6661')
    except Exception as e:
        print(f"[X] 扫描程序调用失败: {e}")
        return

    all_hosts_data = []

    for host in nm.all_hosts():
        host_info = {
            "ip": host,
            "status": nm[host].state(),
            "hostname": nm[host].hostname(),
            "last_scan": "2026-05-10", # 可以根据需要使用 time 库获取实时时间
            "details": []
        }
        
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                # 提取该端口的具体服务信息
                service = nm[host][proto][port]
                port_info = {
                    "port": port,
                    "service": service['name'],
                    "product": service['product'],
                    "version": service['version'],
                    "risk_level": "High" if port == 445 else "Normal"
                }
                host_info["details"].append(port_info)
        
        all_hosts_data.append(host_info)

    # 将结果持久化，供项目三看板调用
    with open("scan_report.json", "w", encoding="utf-8") as f:
        json.dump(all_hosts_data, f, ensure_ascii=False, indent=4)
    
    print("-" * 40)
    print(f"[+] 扫描完成！生成资产快照：scan_report.json")
    print(f"[+] 探测到存活设备总数: {len(all_hosts_data)}")
    print("-" * 40)

if __name__ == "__main__":
    # 使用你刚才查到的 IP 网段进行测试
    # 比如输入: 192.168.167.0/24 (扫描整个宿舍网段)
    target = input("请输入目标 IP 或网段 (测试建议输入 127.0.0.1): ")
    start_med_scan(target)