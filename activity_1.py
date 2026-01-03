import tkinter as tk
from tkinter import font

root=tk.Tk()
root.title("--Student Marks--")
#root.geometry("450*400")
root.config(bg="#f2f2f2")

label_font=font.Font(family="calibri",size=11)
entry_font=font.Font(family="calibri",size=11)
btn_font=font.Font(family="calibri",size=11,weight="bold")

l=tk.Label(root,text="Enter marks of sub1 out of 100:",bg="#f2f2f2",font=label_font)
l.grid(row=0,column=0,sticky="w",padx=20)#,pady=5)
e=tk.Entry(root,width=25,font=entry_font)
e.grid(row=0,column=1,padx=10,pady=5)
l1=tk.Label(root,text="Enter marks of sub2 out of 100:",bg="#f2f2f2",font=label_font)
l1.grid(row=1,column=0,sticky="w",padx=20)#,pady=5)
e1=tk.Entry(root,width=25,font=entry_font)
e1.grid(row=1,column=1,padx=10,pady=5)
l2=tk.Label(root,text="Enter marks of sub3 out of 100:",bg="#f2f2f2",font=label_font)
l2.grid(row=2,column=0,sticky="w",padx=20)#,pady=5)
e2=tk.Entry(root,width=25,font=entry_font)
e2.grid(row=2,column=1,padx=10,pady=5)

def disp():
	t=int(e.get())
	t1=int(e1.get())
	t2=int(e2.get())
	if(0<t<=100 and 0<t1<=100 and 0<t2<=100):
		result.config(text="Sum of all sub is:"+str(t+t1+t2))
		avg=int((t+t1+t2)/3)
		result1.config(text="Average of all sub is:"+str(avg))
		if(avg>=35):
			if(avg>=90):
				result2.config(text="Grade: O Grade")
			elif(avg>=80):
				result2.config(text="Grade: A+ Grade")
			elif(avg>=70):
				result2.config(text="Grade: A Grade")
			elif(avg>=60):
				result2.config(text="Grade: B Grade")
			elif(avg>=50):
				result2.config(text="Grade: C Grade")
			else:
				result2.config(text="Grade: D Grade")
		else:
			result2.config(text="Fail")
	else:
			result.config(text="Invalid marks")
			result1.config(text="")
			result2.config(text="")
	
	
button=tk.Button(root,text="Click me",command=disp,font=btn_font,bg="yellow",fg="black",padx=20)
button.grid(row=4,column=0,columnspan=2,pady=15)
result=tk.Label(root,text="",bg="#f2f2f2",font="label_font")
result.grid(row=5,column=0,sticky="w",padx=20)
result1=tk.Label(root,text="",bg="#f2f2f2",font="label_font")
result1.grid(row=6,column=0,sticky="w",padx=20)
result2=tk.Label(root,text="",bg="#f2f2f2",font=("Arial",12,"bold"))
result2.grid(row=7,column=0,sticky="w",padx=20)
root.mainloop()