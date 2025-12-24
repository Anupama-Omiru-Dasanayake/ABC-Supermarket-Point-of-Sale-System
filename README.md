# 🛒 ABC Supermarket – Point of Sale (POS) System

## 📌 Project Overview
The **ABC Supermarket Point of Sale (POS) System** is a **Python-based, menu-driven console application** developed as part of the **DOC333 – Introduction to Programming Principles** module in IIT Foundation Programme.  
This system manages customer registrations, order placements, sales calculations, and viewing of customer and order details.

---

## 📄 Description
This project simulates a real-world **Point of Sale (POS) system** for a supermarket.  
It is designed to improve efficiency by automating customer and sales management tasks.

The system allows users to:
- Register customers with validation rules
- Place orders for registered customers
- Calculate total sales by branch and date
- View customer details
- View order details with item-wise totals

The application is developed using **Python 3.x** and stores data using in-memory lists.

---

## 🛠️ Technologies Used
- **Programming Language:** Python 3.x  
- **Interface:** Command Line Interface (CLI)  
- **Data Storage:** Python Lists (No database)

---

## ✨ Features
- ✔️ Customer registration with unique Customer IDs  
- ✔️ Age validation (18 years or older)  
- ✔️ Order placement for registered customers  
- ✔️ Maximum of **3 items per order**  
- ✔️ Duplicate Customer ID and Order ID prevention  
- ✔️ Daily sales calculation by branch and date  
- ✔️ View registered customer details  
- ✔️ View order details including item-wise totals  
- ✔️ User-friendly, menu-driven interface  

---

## 🏪 Branch Codes
| Branch Name  | Branch Code |
|-------------|-------------|
| Colombo     | B001        |
| Nugegoda    | B002        |
| Piliyandala | B003        |
| Gampaha     | B004        |

---

## 📋 System Assumptions
- Customers must be **18 years or older**
- Customer ID format: `C001`
- Order ID format: `OD01`
- Customer name must contain **less than 20 characters**
- Address must contain **less than 50 characters**
- Phone number must contain **exactly 10 digits**
- Only **positive numeric values** are allowed for prices and quantities
- One customer can place **only one order**
- Maximum of **3 items per order**
- Currency used: **LKR (Rs.)**

---

## 📂 Project Structure
```text
ABC-Supermarket-Point-of-Sale-System/
│
├── DOC 333 Coursework.py    # Main Python program
├── DOC 333 Report.pdf       # Project documentation
└── README.md                # Project README
```
## 🚀 How to Run the Project

### Prerequisites
- Python **3.x** installed on your system

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anupama-Omiru-Dasanayake/ABC-Supermarket-Point-of-Sale-System.git
2. **Navigate to the project directory**
   ```bash
   cd ABC-Supermarket-Point-of-Sale-System
4. **Run the Python program**
   ```bash
   python pos_system.py
6. **Follow the on-screen menu to:**
- Register customers
- Place orders
- View sales
- View customer and order details

## 👨‍💻 Author

Anupama Omiru (D.M.A.O. Dasanayake)
📧 Email: mr.dasanayake@gmail.com
