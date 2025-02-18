from fpdf import FPDF
import pandas as pd

# Load the data
file_path = "order_details.csv"
df = pd.read_csv(file_path)

# Data Analysis
total_orders = df['order_id'].nunique()
total_pizzas_sold = df['quantity'].sum()
most_ordered_pizza = df.groupby('pizza_id')['quantity'].sum().idxmax()

# Create PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Pizza Order Report", ln=True, align='C')

pdf.ln(10)  # Line break
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Orders: {total_orders}", ln=True)
pdf.cell(200, 10, f"Total Pizzas Sold: {total_pizzas_sold}", ln=True)
pdf.cell(200, 10, f"Most Ordered Pizza: {most_ordered_pizza}", ln=True)

# Save the PDF
pdf_output_path = "order_report.pdf"
pdf.output(pdf_output_path)

print(f"PDF report generated: {pdf_output_path}")
