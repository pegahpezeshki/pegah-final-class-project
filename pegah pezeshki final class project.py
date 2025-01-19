import tkinter as tk
from tkinter import messagebox

# اطلاعات ورود
USERNAME = "پگاه"
PASSWORD = "123456"

# منوی رستوران
menu = {
    "پیتزا": 200000,
    "همبرگر": 180000,
    "مرغ سوخاری": 300000,
    "سیب زمینی": 150000
}


class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("رستوران")
        self.login_screen()

    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="به رستوران خوش آمدید!", font=("Arial", 20)).pack(pady=20)

        tk.Label(self.root, text="نام کاربری:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="رمز عبور:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="ورود", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == USERNAME and password == PASSWORD:
            self.menu_screen()
        else:
            messagebox.showerror("خطا", "نام کاربری یا رمز عبور اشتباه است.")

    def menu_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="منوی رستوران", font=("Arial", 20)).pack(pady=20)

        self.selected_dish = tk.StringVar()

        for dish, price in menu.items():
            tk.Radiobutton(self.root, text=f"{dish}: {price} تومان", variable=self.selected_dish, value=dish).pack(
                anchor='w')

        tk.Button(self.root, text="انتخاب غذا", command=self.show_payment).pack(pady=20)
        tk.Button(self.root, text="خروج", command=self.root.quit).pack(pady=5)

    def show_payment(self):
        dish = self.selected_dish.get()
        if dish:
            price = menu[dish]
            messagebox.showinfo("پرداخت",
                                f"شما {dish} را انتخاب کردید. قیمت: {price} تومان.\nبرای پرداخت، 'پرداخت' را وارد کنید.")
        else:
            messagebox.showwarning("هشدار", "لطفاً یک غذا انتخاب کنید.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()