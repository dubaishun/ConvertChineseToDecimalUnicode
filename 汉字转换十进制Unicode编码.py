import os
import sys
import tkinter as tk
from tkinter import scrolledtext  # 导入滚动文本模块

# ----- Start of Image Processor Code -----

def chinese_to_unicode(chinese_str):
    return str(ord(chinese_str))

def start_main_application():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    pic_directory = os.path.join(application_path, "pic")

    def export_filenames_by_size():
        extensions = ['.jpg', '.jpeg', '.png']
        files = [f for f in os.listdir(pic_directory) if os.path.splitext(f)[1].lower() in extensions]
        files_sorted_by_size = sorted(files, key=lambda x: os.path.getsize(os.path.join(pic_directory, x)))
        
        names_without_extension = [os.path.splitext(filename)[0] for filename in files_sorted_by_size]
        
        for name in names_without_extension:
            if len(name) != 1:
                txt_filenames.insert(tk.END, f"获取的图片名中不是单字：{name}\n")
                return
        
        encoded_names = [chinese_to_unicode(name) for name in names_without_extension]
    
        txt_filenames.insert(tk.END, ",".join(names_without_extension))
        txt_encoded_names.insert(tk.END, ",".join(encoded_names))

    root = tk.Tk()
    root.title("汉字转换十进制Unicode编码")

    window_width = 800
    window_height = 530

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int((screen_width / 2) - (window_width / 2))
    center_y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    # 修正了字符串中的引号问题
    lbl_info = tk.Label(root, text="获取图片名的排列方式：'大小--递增'，转换后将图片也按'大小-递增'排列，将生成的编码和图片导入到FontCreator，可生成字体库。", font=("Arial", 10))
    lbl_info.grid(sticky='w', padx=10, pady=10)

    lbl_filenames = tk.Label(root, text="文件名", font=("Arial", 12))
    lbl_encoded_names = tk.Label(root, text="Unicode编码", font=("Arial", 12))

    txt_filenames = scrolledtext.ScrolledText(root, width=50, height=25)
    txt_encoded_names = scrolledtext.ScrolledText(root, width=50, height=25)

    btn_convert = tk.Button(root, text="获取图片名转换汉字十进制Unicode编码", command=export_filenames_by_size, width=40, height=2)

    lbl_info.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lbl_filenames.grid(row=1, column=0, padx=10, pady=5)
    lbl_encoded_names.grid(row=1, column=1, padx=10, pady=5)
    txt_filenames.grid(row=2, column=0, padx=10, pady=5)
    txt_encoded_names.grid(row=2, column=1, padx=10, pady=5)
    btn_convert.grid(row=3, column=0, columnspan=2, pady=20)

    root.mainloop()

# 主程序入口
if __name__ == "__main__":
    start_main_application()