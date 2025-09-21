import streamlit as st
from improvised_main import Bank   # assuming Bank class is saved in bank.py

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Menu", [
    "Create Account", "Deposit Money", "Withdraw Money",
    "Show Details", "Update Details", "Delete Account"
])

if menu == "Create Account":
    st.subheader("Open a New Bank Account")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=10, max_value=100, step=1)
    email = st.text_input("Enter Email")
    pin = st.text_input("Enter 4-digit PIN", type="password")
    if st.button("Create Account"):
        result = Bank.create_account(name, age, email, pin)
        st.success(result["msg"])
        if result["status"]:
            st.json(result["account"])

elif menu == "Deposit Money":
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        result = Bank.deposit(acc, int(pin), amount)
        st.write(result["msg"])
        if result["status"]: st.write("Balance:", result["balance"])

elif menu == "Withdraw Money":
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        result = Bank.withdraw(acc, int(pin), amount)
        st.write(result["msg"])
        if result["status"]: st.write("Balance:", result["balance"])

elif menu == "Show Details":
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Show"):
        result = Bank.details(acc, int(pin))
        if result: st.json(result)
        else: st.error("No such account")

elif menu == "Update Details":
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    name = st.text_input("New Name (leave blank to skip)")
    email = st.text_input("New Email (leave blank to skip)")
    new_pin = st.text_input("New PIN (optional)", type="password")
    if st.button("Update"):
        result = Bank.update_details(acc, int(pin), name or None, email or None, new_pin or None)
        st.write(result["msg"])

elif menu == "Delete Account":
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Delete"):
        result = Bank.delete_account(acc, int(pin))
        st.write(result["msg"])
