from tkinter import *
import pandas as pd # Để đọc và xử lý bảng dữ liệu
from sklearn.svm import SVC # Để tạo và huấn luyện mô hình SVM
from sklearn.model_selection import train_test_split # Để chia dữ liệu thành tập huấn luyện và tập kiểm tra
from sklearn.metrics import accuracy_score # Để đánh giá độ chính xác của mô hình
from sklearn.linear_model import LogisticRegression

top = Tk()
top.title('SVM')
top.geometry('900x700')
top['bg'] = 'cyan'

#nhiet do
name = Label(top, font=('Arial, 14'), text="Nhiệt độ (Độ C)", fg = 'black')
name.place(x=30, y= 30)
nhietdo = Entry(top, width=20, font=('Arial, 14'), fg='black')
nhietdo.place(x=180, y=30)

#khuyen mai
name = Label(top, font=('Arial, 14'), text="Khuyến mãi (%)", fg = 'black')
name.place(x=500, y=30)
khuyenmai = Entry(top, width=20, font=('Arial, 14'), fg='black')
khuyenmai.place(x=650, y=30)

#gia ban
name = Label(top, font=('Arial, 14'), text="Giá bán ($)", fg = 'black')
name.place(x=30, y=100)
giaban = Entry(top, width=20, font=('Arial, 14'), fg='black')
giaban.place(x=180, y=100)

#chat luong
name = Label(top, font=('Arial, 14'), text="Chất lượng (*)", fg = 'black')
name.place(x=500, y=100)
chatluong = Entry(top, width=20, font=('Arial, 14'), fg='black')
chatluong.place(x=650, y=100)

#quang cao
name = Label(top, font=('Arial, 14'), text="Quảng cáo (%)", fg = 'black')
name.place(x=30, y=200)
quangcao = Entry(top, width=20, font=('Arial, 14'), fg='black')
quangcao.place(x=180, y=200)

#pho bien
name = Label(top, font=('Arial, 14'), text="Độ phổ biến (%)", fg = 'black')
name.place(x=500, y=200)
phobien = Entry(top, width=20, font=('Arial, 14'), fg='black')
phobien.place(x=650, y=200)

#mat do
name = Label(top, font=('Arial, 14'), text="Mật độ dân cư", fg = 'black')
name.place(x=30, y=300)
matdo = Entry(top, width=20, font=('Arial, 14'), fg='black')
matdo.place(x=180, y=300)

#doanh thu
name = Label(top, font=('Arial, 14'), text="Doanh thu ($)", fg = 'black')
name.place(x=500, y=300)
doanhthu = Entry(top, width=20, font=('Arial, 14'), fg='black')
doanhthu.place(x=650, y=300)


#du doan svm
name = Label(top, font=('Arial, 14'), text="Kết quả dự đoán", fg = 'black')
name.place(x=500, y=400)
kq = Entry(top, width=20, font=('Arial, 14'), fg='black')
kq.place(x=650, y=400)

#do chinh xac svm
name = Label(top, font=('Arial, 14'), text="Độ chính xác", fg = 'black')
name.place(x=500, y=450)
P = Entry(top, width=20, font=('Arial, 14'), fg='black')
P.place(x=650, y=450)


#du doan 
name = Label(top, font=('Arial, 14'), text="Kết quả dự đoán", fg = 'black')
name.place(x=500, y=550)
kq1 = Entry(top, width=20, font=('Arial, 14'), fg='black')
kq1.place(x=650, y=550)

#do chinh xac 
name = Label(top, font=('Arial, 14'), text="Độ chính xác", fg = 'black')
name.place(x=500, y=600)
P1 = Entry(top, width=20, font=('Arial, 14'), fg='black')
P1.place(x=650, y=600)


#click svm
def svm():
    name = Label(top, font=('Arial, 14'), text="Đã click svm", fg = 'black')
    name.place(x=30, y=420) 
    # Đọc bảng dữ liệu csv từ file
    df = pd.read_csv("C:\\Users\\ADMIN\\Downloads\\baodangao.csv") 

    # Xem thông tin tổng quan về bảng dữ liệu 
    df.info()

    # Chọn các cột làm đặc trưng (features) và nhãn (labels)
    X = df[["Nhiệt độ trung bình (độ C)", "Khuyến mãi (%)", "Giá bán ($)", "Chất lượng (*)", "Quảng cáo chiến dịch(%)", "Biến phổ rộng (%)", "Mật độ dân cư (số/km)","Doanh thu hiện tại"]] # Các cột làm đặc trưng
    y = df["Dự đoán"] # Cột làm nhãn

    # Chia dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Tạo mô hình SVM với hàm nhân tuyến tính (linear kernel)
    svm = SVC(kernel="linear")

    # Huấn luyện mô hình với tập huấn luyện
    svm.fit(X_train, y_train)

    # Dự đoán nhãn cho tập kiểm tra
    y_pred = svm.predict(X_test)

    # Tính độ chính xác của mô hình trên tập kiểm tra
    acc = accuracy_score(y_test, y_pred)
    P.delete(0,END)
    P.insert(0, acc)

    #   Dùng mô hình để dự đoán thử với dữ liệu mới
    arrr= [[float(nhietdo.get()), float(khuyenmai.get()),float(giaban.get()), float(chatluong.get()),float(quangcao.get()),float(phobien.get()),float(matdo.get()),float(doanhthu.get())]]
    new_data = arrr # Một mẫu dữ liệu mới với các giá trị của các đặc trưng
    new_pred = svm.predict(new_data) # Dự đoán nhãn cho mẫu mới
    kq.delete(0,END)
    kq.insert(0, new_pred)
         
    
    
svm = Button(top, text='SVM', width=12, height=2, font=('Arial, 14'), fg='green', command=svm )
svm.place(x=200, y=410)


#click 
def tt2():
    name = Label(top, font=('Arial, 14'), text="Đã click LR", fg = 'black')
    name.place(x=30, y=570)
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv('C:\\Users\\ADMIN\\Downloads\\baodangao.csv')

    # Tách các thuộc tính độc lập và biến phụ thuộc
    X = data.iloc[:, :-1]  # Các thuộc tính độc lập
    y = data.iloc[:, -1]  # Biến phụ thuộc

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Khởi tạo mô hình hồi quy logistic
    model = LogisticRegression()

    # Huấn luyện mô hình trên tập huấn luyện
    model.fit(X_train, y_train)

    # Dự đoán nhãn cho tập kiểm tra
    y_pred = model.predict(X_test)

    # Đánh giá độ chính xác của mô hình
    accuracy = accuracy_score(y_test, y_pred)
    P1.delete(0,END)
    P1.insert(0, accuracy)

    # Dùng mô hình để dự đoán thử với dữ liệu mới
    arrr= [[float(nhietdo.get()), float(khuyenmai.get()),float(giaban.get()), float(chatluong.get()),float(quangcao.get()),float(phobien.get()),float(matdo.get()),float(doanhthu.get())]]
    new_data = arrr # Một mẫu dữ liệu mới với các giá trị của các đặc trưng
    new_pred = model.predict(new_data) # Dự đoán nhãn cho mẫu mới
    kq1.delete(0,END)
    kq1.insert(0,new_pred)
lr = Button(top, text='Logistic Regression', width=15, height=2, font=('Arial, 14'), fg='green', command=tt2 )
lr.place(x=200, y=560)


top.mainloop()