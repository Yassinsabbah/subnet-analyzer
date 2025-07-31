# Subnet Analyzer 🚀

This project reads a list of IP addresses and subnet masks, calculates CIDR info, and outputs:
- Network address
- Broadcast address
- Usable host count
- A CSV report
- A bar chart visualizing host distribution

---

## 📂 Files

| File | Description |
|------|-------------|
| `subnet_analyzer.py` | Main script (subnet calculations + export) |
| `visualize.py`       | Bar chart script (optional) |
| `Dockerfile`         | Docker container definition |
| `ip_data.xlsx`       | Input dataset (provided) |
| `subnet_report.csv`  | Generated output report |
| `network_plot.png`   | Host distribution bar chart |
| `report.md`          | Answers to the analysis questions |
| `README.md`          | Project documentation and instructions |

---

## 🐳 How to Run with Docker

```bash
# 🏗️ Build the Docker image
docker build -t subnet-analyzer .

# ▶️ Run the container
docker run --rm subnet-analyzer

# 💾 (Optional) To save the output files (CSV + chart) to your machine
docker run --rm -v $(pwd):/app subnet-analyzer
