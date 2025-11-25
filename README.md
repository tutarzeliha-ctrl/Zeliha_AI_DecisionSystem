📄 Zeliha_AI_DecisionSystem

AI-Powered Decision Engine for E-commerce User Behavior Analysis
(TR + EN Bilingual PDF Reporting)

🧠 Overview

This project automatically analyzes user behavior patterns in e-commerce platforms and generates professional bilingual (TR + EN) PDF reports.

Sistem;

Trigger → Behavior → Diagnosis → Action
akışını tam otomatik işler.

🔍 Features

✔ AI-supported event interpretation
✔ TR → EN otomatik çeviri motoru
✔ Profesyonel dark-mode PDF çıktısı
✔ Türkçe karakter destekli font (DejaVuSans)
✔ Modüler proje mimarisi (src/data/output)
✔ Tek tıklamayla rapor üretimi

📂 Project Structure
Zeliha_AI_DecisionSystem/
│
├── data/
│     └── logs.csv
│
├── src/
│     ├── analyzer.py
│     ├── translator.py
│     └── pdf_generator.py
│
├── output/
│     └── AI_Report_TR_EN.pdf (otomatik oluşur)
│
├── README.md
└── requirements.txt

🚀 How to Run
1) Install dependencies
pip install -r requirements.txt

2) Run the pipeline
python src/analyzer.py


This will generate:

output/AI_Report_TR_EN.pdf

🧩 Modules
🔹 translator.py

TR → EN translation module + English behavior/diagnosis/action templates.

🔹 pdf_generator.py

Bilingual PDF creation system with dark mode and DejaVuSans font.

🔹 analyzer.py

Main automation pipeline:

Reads logs

Applies event analysis

Merges results

Generates bilingual PDF

👩‍💻 Developer

Zeliha Tutar
Data & AI Developer (Training)

Bu proje, e-commerce kullanıcı davranışlarını analiz eden gerçek bir AI pipeline mimarisidir.

📌 Repository will continue to improve with new modules and analytics features.
