from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        img=Image.open(r"D:\Face_recognition\Images\student_pass.png")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # 2nd image 
        
        img1=Image.open(r"D:\Face_recognition\Images\fr_system.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=500,y=0,width=550,height=130)

        # 3rd image
        
        img2=Image.open(r"D:\Face_recognition\Images\fr_system.png")
        img2=img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1000,y=0,width=550,height=130)

        # bg 
        img3=Image.open(r"D:\Face_recognition\Images\bg.png")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # student button
        img4=Image.open(r"D:\Face_recognition\Images\student.jpg")
        img4 = img4.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b2=Button(bg_img,text="Students Details",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2.place(x=200,y=300,width=220,height=40)
        
        #detect face
        # student button
        img5=Image.open(r"D:\Face_recognition\Images\recognition.jpg")
        img5 = img5.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1_1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1_1.place(x=500,y=100,width=220,height=220)
        
        b2_1=Button(bg_img,text="Face Detection",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_1.place(x=500,y=300,width=220,height=40)
        
        #Attendance Face
        img6=Image.open(r"D:\Face_recognition\Images\attendence.png")
        img6 = img6.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1_2=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1_2.place(x=800,y=100,width=220,height=220)
        
        b2_2=Button(bg_img,text="Attendence ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_2.place(x=800,y=300,width=220,height=40)
        
        #help
        img7=Image.open(r"D:\Face_recognition\Images\help.png")
        img7 = img7.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1_2=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1_2.place(x=1100,y=100,width=220,height=220)
        
        b2_2=Button(bg_img,text="Help Desk ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_2.place(x=1100,y=300,width=220,height=40)
        
        #train face
        img8=Image.open(r"D:\Face_recognition\Images\train.jpg")
        img8 = img8.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1_3=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1_3.place(x=200,y=380,width=220,height=220)
        
        b2_3=Button(bg_img,text="Training Model ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_3.place(x=200,y=580,width=220,height=40)
        
        #photo face
        img9=Image.open(r"D:\Face_recognition\Images\photos.jpg")
        img9 = img9.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1_4=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1_4.place(x=500,y=380,width=220,height=220)
        
        b2_4=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_4.place(x=500,y=580,width=220,height=40)
        
        #developer
        img10=Image.open(r"D:\Face_recognition\Images\develop.png")
        img10= img10.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1_5=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1_5.place(x=800,y=380,width=220,height=220)
        
        b2_5=Button(bg_img,text="Developer ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_5.place(x=800,y=580,width=220,height=40)
        
        #exit
        img11=Image.open(r"D:\Face_recognition\Images\exit.png")
        img11= img11.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1_6=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1_6.place(x=1100,y=380,width=220,height=220)
        
        b2_6=Button(bg_img,text="Training Model ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_6.place(x=1100,y=580,width=220,height=40)
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()