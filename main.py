# main.py

import tkinter as tk
from tkinter import messagebox

# 创建主应用窗口
def create_app():
    app = tk.Tk()
    app.title("My Application")
    app.geometry("400x300")

    # 标签
    label = tk.Label(app, text="欢迎使用我的应用程序！", font=("Arial", 14))
    label.pack(pady=20)

    # 按钮点击事件
    def on_button_click():
        messagebox.showinfo("提示", "按钮已点击！")

    # 创建按钮
    button = tk.Button(app, text="点击我", command=on_button_click, font=("Arial", 12))
    button.pack(pady=20)

    # 启动应用
    app.mainloop()

if __name__ == "__main__":
    create_app()
