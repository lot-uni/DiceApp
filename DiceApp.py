import tkinter as tk
import random

# 1.tkinterでウィンドウを作成
root = tk.Tk()
root.title('DiceApp')
root.geometry('400x400')

# 2.ラベルクリック時の処理
def click_func(event):
    roll_count = iter(range(10)[::-1])
    def roll():# 3.PhotoImageを十回変更する
        FileName = "dice.00" + str(random.randint(1,6)) + ".png"
        photo.config(file=FileName)
        if next(roll_count) > 0:
            root.after(80, roll)
    roll()

# 3. PhotoImageオブジェクト、Buttonオブジェクトを作成
photo = tk.PhotoImage(file="dice.001.png")
PhotoLabel = tk.Label(image=photo)

# 4. PhotoImageオブジェクトの表示
PhotoLabel.bind("<ButtonPress>", click_func)
PhotoLabel.pack()

# 5. メインループ
root.mainloop()