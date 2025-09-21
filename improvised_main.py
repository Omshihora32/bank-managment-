import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    @classmethod
    def load(cls):
        if Path(cls.database).exists():
            with open(cls.database, encoding="utf-8") as fs:
                cls.data = json.load(fs)
        else:
            cls.data = []

    @classmethod
    def save(cls):
        with open(cls.database, "w", encoding="utf-8") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __account_generate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*()", k=1)
        id_parts = alpha + num + spchar
        random.shuffle(id_parts)
        return "".join(id_parts)

    @classmethod
    def create_account(cls, name, age, email, pin):
        cls.load()
        try:
            age = int(age)
            pin = int(pin)
        except:
            return {"status": False, "msg": "Invalid age or pin", "account": None}
        if age < 18 or len(str(pin)) != 4:
            return {"status": False, "msg": "Age must be 18+ and PIN must be 4 digits", "account": None}
        acc_no = cls.__account_generate()
        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no.": acc_no,
            "balance": 0
        }
        cls.data.append(info)
        cls.save()
        return {"status": True, "msg": "Account created!", "account": info}

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        cls.load()
        for user in cls.data:
            if user['account_no.'] == acc_no and user['pin'] == pin:
                if amount > 10000 or amount < 0:
                    return {"status": False, "msg": "Cannot deposit more than 10000.", "balance": user['balance']}
                user['balance'] += int(amount)
                cls.save()
                return {"status": True, "msg": "Deposit successful.", "balance": user['balance']}
        return {"status": False, "msg": "Account or PIN incorrect.", "balance": None}

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        cls.load()
        for user in cls.data:
            if user['account_no.'] == acc_no and user['pin'] == pin:
                if user['balance'] < amount:
                    return {"status": False, "msg": "Insufficient balance.", "balance": user['balance']}
                user['balance'] -= int(amount)
                cls.save()
                return {"status": True, "msg": "Withdraw successful.", "balance": user['balance']}
        return {"status": False, "msg": "Account or PIN incorrect.", "balance": None}

    @classmethod
    def details(cls, acc_no, pin):
        cls.load()
        for user in cls.data:
            if user['account_no.'] == acc_no and user['pin'] == pin:
                user_copy = user.copy()
                user_copy.pop('pin')
                return user_copy
        return None

    @classmethod
    def update_details(cls, acc_no, pin, name=None, email=None, new_pin=None):
        cls.load()
        for user in cls.data:
            if user['account_no.'] == acc_no and user['pin'] == pin:
                if name: user['name'] = name
                if email: user['email'] = email
                if new_pin:
                    try:
                        user['pin'] = int(new_pin)
                    except:
                        return {"status": False, "msg": "PIN must be 4 digits"}
                cls.save()
                return {"status": True, "msg": "Details updated"}
        return {"status": False, "msg": "Account or PIN incorrect"}

    @classmethod
    def delete_account(cls, acc_no, pin):
        cls.load()
        for i, user in enumerate(cls.data):
            if user['account_no.'] == acc_no and user['pin'] == pin:
                cls.data.pop(i)
                cls.save()
                return {"status": True, "msg": "Account deleted"}
        return {"status": False, "msg": "Account or PIN incorrect"}
