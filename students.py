from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Students:
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
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #LEFT FRAME
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        img_left=Image.open(r"D:\Face_recognition\Images\fr_system.png")
        img_left=img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl2=Label(Left_frame,image=self.photoimg_left)
        f_lbl2.place(x=5,y=0,width=720,height=130)
        
        #current course
        Current_Course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        Current_Course_frame.place(x=5,y=135,width=720,height=150)
        
        dep_label=Label(Current_Course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Current_Course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","CSE","CSD","ISE","AI-ML","EEE","ECE","CIVIL","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(Current_Course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Current_Course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=20,sticky=W)
        
        #year
        year_label=Label(Current_Course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Current_Course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        Sem_label=Label(Current_Course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Sem_combo=ttk.Combobox(Current_Course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        Sem_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # class student info
        Class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Students Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=275,width=720,height=250)
        
        #Student id
        Studentid_label=Label(Class_Student_frame,text="Studentd ID:",font=("times new roman",12,"bold"),bg="white")
        Studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Studentid_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        StudentName_label=Label(Class_Student_frame,text="Studentd Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        StudentName_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        Student_div_label=Label(Class_Student_frame,text="Studentd Division:",font=("times new roman",12,"bold"),bg="white")
        Student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Student_div_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #roll
        Student_roll_label=Label(Class_Student_frame,text="Student Roll:",font=("times new roman",12,"bold"),bg="white")
        Student_roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Student_roll_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #gender
        Student_gen_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Student_gen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        Student_gen_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_gen_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        Student_gen_label=Label(Class_Student_frame,text="D.O.B:",font=("times new roman",12,"bold"),bg="white")
        Student_gen_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Student_gen_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_gen_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #email
        Student_gen_label=Label(Class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Student_gen_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Student_gen_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_gen_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone
        Student_gen_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        Student_gen_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Student_gen_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_gen_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address
        Student_gen_label=Label(Class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Student_gen_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        Student_gen_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_gen_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher name
        Student_gen_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        Student_gen_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        Student_gen_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Student_gen_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        radiobutton1=ttk.Radiobutton(Class_Student_frame,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=5,column=0)
        
        radiobutton2=ttk.Radiobutton(Class_Student_frame,text="No Photo Sample",value="Yes")
        radiobutton2.grid(row=5,column=1)
        
        #button frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width =715,height=35)
        
        save_btn=Button(btn_frame,text="Save",width=23,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=23,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=5)
        
        delete_btn=Button(btn_frame,text="Delete",width=23,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=5)
        
        reset_btn=Button(btn_frame,text="Reset",width=23,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5)
        
        # button frame for photo options
        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        # Take Photo Button
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=34, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        # Update Photo Button (fixed label)
        updatephoto_btn = Button(btn_frame1, text="Update Photo Sample", width=34, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        updatephoto_btn.grid(row=0, column=1)

        
        
        
        
        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        #img_right=Image.open(r"D:\Face_recognition\Images\fr_system.png")
        #img_right=img_right.resize((720, 130), Image.Resampling.LANCZOS)
        #self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        #f_lbl2=Label(Right_frame,image=self.photoimg2)
        #f_lbl2.place(x=1000,y=0,width=550,height=130)

if __name__ == "__main__":
    root=Tk()
    obj=Students(root)
    root.mainloop()