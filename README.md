
# 医疗资产安全扫描器 (Medical Asset Scanner) 🏥🛡️

本项目是医疗网络态势感知系统的重要组成部分，专注于医疗内网资产的自动化发现与风险评估。

## 🌟 项目亮点
- **协议深度探测**：针对医疗环境定制，支持 DICOM (104) 影像传输协议及 HL7 (6661) 业务通讯协议的指纹识别。
- **高危风险识别**：内置勒索病毒防御逻辑，自动标记 445 (SMB) 等易受攻击的端口为 `High Risk`。
- **数据生态联动**：扫描结果以标准 JSON 格式输出，可无缝对接 Flask 态势感知看板进行可视化展示。

## 🛠️ 技术栈
- **语言**：Python 3.x
- **核心引擎**：Nmap (Network Mapper)
- **依赖库**：python-nmap, json

## 📖 快速开始
1. **安装环境**：确保本地已安装 Nmap 软件，并激活环境执行 `pip install python-nmap`。
2. **运行扫描**：
   ```bash
   python xiangmuone.py

<img width="1098" height="563" alt="屏幕截图 2026-05-13 110507" src="https://github.com/user-attachments/assets/d5805ed9-a700-4447-8330-546c9e8fede8" />
<img width="1254" height="738" alt="屏幕截图 2026-05-13 110538" src="https://github.com/user-attachments/assets/0ea293c8-7844-4302-9df9-d8169f818fa3" />
