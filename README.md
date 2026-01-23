### Excel Image Converter – PNG ➜ JPG (Column-to-Column)



A professional Python tool to convert PNG images embedded in an Excel workbook into optimized JPG images and insert them into another column on the same row, without modifying the original structure.



---



### ✨ Key Features



Keeps row order strictly unchanged

Original PNG images remain intact

JPG images inserted on the same row

Automatic JPG compression (optional size control)

Excel-safe (opens without warnings)

Simple GUI (1-click execution)

Ready for packaging as `.exe`



---



### 📂 Use Case



\- Large Excel file (hundreds of rows)

\- Each row contains:

&nbsp; - PNG image reference in Column F

&nbsp; - Target JPG image inserted into Column G


&nbsp; - No row added / deleted / reordered

&nbsp; - Side-by-side visual comparison

&nbsp; - Clean and reliable output



---



### 🏗 Project Structure

image_converter_project/

│

├── input/

│ └── input.xlsx # Original Excel file

│

├── output/

│ └── output.xlsx # Final Excel file (generated)

│

├── temp/

│ └── row_*.jpg # Temporary JPG files

│

├── src/

│ ├── app.py # Core processing logic

│ └── ui.py # Simple Tkinter UI

│

└── README.md

---


### ⚙️ How It Works

1. Load the original Excel workbook
2. For each row:
   - Read PNG path from **Column F**
   - Convert PNG ➜ JPG using Pillow
   - Optionally compress JPG
   - Insert JPG into **Column G (same row)**
3. Save as a new Excel file (`output.xlsx`)
4. Original data remains untouched

---

### ▶️ How to Run

### Option 1 — GUI (recommended)

```bash
python src/ui.py
```

---

### 🧠 Technologies Used

Python 3.10+

openpyxl (Excel manipulation)

Pillow (image processing)

Tkinter (UI)


---

###  Architecture Diagram (Clear & Client-Readable)

┌────────────────────────┐

│ input.xlsx │

│------------------------│

│ Column F : PNG images │

└───────────┬────────────┘

│

▼

┌────────────────────────┐

│ app.py (Core) │

│------------------------│

│ - Load Excel workbook │

│ - Loop rows │

│ - Convert PNG ➜ JPG │

│ - Save JPG to /temp │

│ - Insert image in G │

└───────────┬────────────┘

│

▼

┌────────────────────────┐

│ openpyxl │

│------------------------│

│ Embed JPG into Excel │

│ (same row, column G) │

└───────────┬────────────┘

│

▼

┌────────────────────────┐

│ output.xlsx │

│------------------------│

│ Column F : PNG (orig) │

│ Column G : JPG (new) │

└────────────────────────┘


(Optional)

┌────────────────────────┐

│ ui.py │

│------------------------│

│ 1-click execution │

│ Error handling │

└────────────────────────┘

---

### 👩‍💻 Author

Eng. Khadija Bouadi


### 📧 Contact

For any queries, reach out to:

GitHub: @khadibd

Email:  khadijabouadi00@gmail.com 




