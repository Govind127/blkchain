# 🧱 Simple Blockchain App

This is a simple Python and Streamlit-based **Blockchain Simulation App** that allows users to:

- Create a blockchain.
- Add new blocks containing healthcare data (e.g., X-ray, MRI, CT Scan).
- Display the blockchain in list, JSON, and table views.
- Validate the blockchain for tampering.
- Test blockchain integrity by modifying block data.

---

## 🚀 Features

- Interactive UI using **Streamlit**.
- Real-time block creation and visualization.
- Blockchain data shown in:
  - Pretty JSON format
  - Clean tabular format using `tabulate`
- Blockchain validation logic with tampering detection.

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- pip

### 📦 Install Dependencies

Open your terminal (VS Code or Command Prompt) and run:

```bash
pip install streamlit tabulate
streamlit run blockchain_app.py
