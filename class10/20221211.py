from tkinter import *
root=Tk()
root.geometry('880x650')
root.title("KubeTech Shop")
from PIL import Image, ImageTk
# row=1
title_img=Image.open('C:/Users/halst/Downloads/image/image/logo_tree.png')
title_img=title_img.resize((32,32))
title_img=ImageTk.PhotoImage(title_img)
title_label=Label(root,image=title_img)
title_label.grid(row=0,column=0,sticky=W)
Sofa_button=Button(root,text="沙發",pady=2,padx=5,bg="#ECE8E7",fg="#1E1E1E",width=5)
Bedding_button=Button(root,text="寢具",pady=2,padx=5,bg="#ECE8E7",fg="#1E1E1E",width=5)
Kitchen_wear_button=Button(root,text="廚具",pady=2,padx=5,bg="#ECE8E7",fg="#1E1E1E",width=5)
Sofa_button.grid(row=0,column=1,sticky=E+W)
Bedding_button.grid(row=0,column=2,sticky=E+W)
Kitchen_wear_button.grid(row=0,column=3,sticky=E+W)
Signup_button=Button(root,text="會員註冊/登入",pady=2,bg="#F8DCDC",fg="#1E1E1E")
Signup_button.grid(row=0,column=7,sticky=W+E)
# row=2
banner_img=Image.open('C:/Users/halst/Downloads/image/image/banner.jpg')
banner_img=banner_img.resize((852,298))
banner_img=ImageTk.PhotoImage(banner_img)
banner_label=Label(root,image=banner_img)
banner_label.grid(row=1,column=0,columnspan=8,padx=5)
# row=3
Sofa1_img=Image.open('C:/Users/halst/Downloads/image/image/sofa1.jpg')
Sofa1_img=Sofa1_img.resize((202,200))
Sofa1_img=ImageTk.PhotoImage(Sofa1_img)
Sofa1_label=Label(root,image=Sofa1_img)
Sofa1_label.grid(row=2,column=0,columnspan=2,padx=5,sticky=W)

Sofa2_img=Image.open('C:/Users/halst/Downloads/image/image/sofa2.jpg')
Sofa2_img=Sofa2_img.resize((202,200))
Sofa2_img=ImageTk.PhotoImage(Sofa2_img)
Sofa2_label=Label(root,image=Sofa2_img)
Sofa2_label.grid(row=2,column=2,columnspan=2,padx=5,sticky=W)

Sofa3_img=Image.open('C:/Users/halst/Downloads/image/image/sofa3.jpg')
Sofa3_img=Sofa3_img.resize((202,200))
Sofa3_img=ImageTk.PhotoImage(Sofa3_img)
Sofa3_label=Label(root,image=Sofa3_img)
Sofa3_label.grid(row=2,column=4,columnspan=2,padx=5,sticky=W)

Sofa4_img=Image.open('C:/Users/halst/Downloads/image/image/sofa4.jpg')
Sofa4_img=Sofa4_img.resize((202,200))
Sofa4_img=ImageTk.PhotoImage(Sofa4_img)
Sofa4_label=Label(root,image=Sofa4_img)
Sofa4_label.grid(row=2,column=6,columnspan=2,padx=5,sticky=W)
# row=4
Product_name_label1=Label(root,text="三人座沙發, grann/bomstad 黑色/金屬",font=("Inter",10),fg="Black")
Product_name_label2=Label(root,text="三人座沙發, grann/bomstad 黑色/木材",font=("Inter",10),fg="Black")
Product_name_label3=Label(root,text="三人座沙發, grann/bomstad 米色/金屬",font=("Inter",10),fg="Black")
Product_name_label4=Label(root,text="三人座沙發, grann/bomstad 米色/木材",font=("Inter",10),fg="Black")
Product_name_label1.grid(row=3,column=0,columnspan=2,padx=5,sticky=W)
Product_name_label2.grid(row=3,column=2,columnspan=2,padx=5,sticky=W)
Product_name_label3.grid(row=3,column=4,columnspan=2,padx=5,sticky=W)
Product_name_label4.grid(row=3,column=6,columnspan=2,padx=5,sticky=W)
# row=5
Product_price_label1=Label(root,text="NT.28,900",font=("Inter",10),fg="Black")
Product_price_label2=Label(root,text="NT.28,900",font=("Inter",10),fg="Black")
Product_price_label3=Label(root,text="NT.28,900",font=("Inter",10),fg="Black")
Product_price_label4=Label(root,text="NT.28,900",font=("Inter",10),fg="Black")
Product_price_label1.grid(row=4,column=0,columnspan=2,padx=5,sticky=W)
Product_price_label2.grid(row=4,column=2,columnspan=2,padx=5,sticky=W)
Product_price_label3.grid(row=4,column=4,columnspan=2,padx=5,sticky=W)
Product_price_label4.grid(row=4,column=6,columnspan=2,padx=5,sticky=W)
Product_minus_button1=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_num_label1=Label(root,text="0",font=("Inter",10),fg="#1E1E1E")
Product_add_button1=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_minus_button2=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_num_label2=Label(root,text="0",font=("Inter",10),fg="#1E1E1E")
Product_add_button2=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_minus_button3=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_num_label3=Label(root,text="0",font=("Inter",10),fg="#1E1E1E")
Product_add_button3=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_minus_button4=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_num_label4=Label(root,text="0",font=("Inter",10),fg="#1E1E1E")
Product_add_button4=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F8DCDC")
Product_minus_button1.grid(row=4,column=1,sticky=W)
Product_num_label1.grid(row=4,column=1,sticky=W+E)
Product_add_button1.grid(row=4,column=1,sticky=E)
Product_minus_button2.grid(row=4,column=3,sticky=W)
Product_num_label2.grid(row=4,column=3,sticky=W+E)
Product_add_button2.grid(row=4,column=3,sticky=E)
Product_minus_button3.grid(row=4,column=5,sticky=W)
Product_num_label3.grid(row=4,column=5,sticky=W+E)
Product_add_button3.grid(row=4,column=5,sticky=E)
Product_minus_button4.grid(row=4,column=7,sticky=W)
Product_num_label4.grid(row=4,column=7,sticky=W+E)
Product_add_button4.grid(row=4,column=7,sticky=E)
# row=6
root.rowconfigure(5,weight=2)
Detail_list_button=Button(root,text="詳細清單",font=("Inter",10),fg="Black",bg="#F8DCDC")
Detail_list_button.grid(row=5,column=0,sticky=W+S,padx=5,pady=1)
Shoppy_img=Image.open('C:/Users/halst/Downloads/image/image/Shopping Cart.png')
Shoppy_img=Shoppy_img.resize((30,30))
Shoppy_img=ImageTk.PhotoImage(Shoppy_img)
Shoppy_label=Label(root,image=Shoppy_img)
Shoppy_label.grid(row=5,column=4,padx=5,sticky=E+S,pady=1)
Shoppy_price=Label(root,text="供消費:0元",font=("Inter",10),fg="Black")
Shoppy_price.grid(row=5,column=5,columnspan=2,sticky=W+S,padx=5,pady=1)
Pay_button=Button(root,text="結帳",font=("Inter",10),fg="Black",bg="#F8DCDC")
Pay_button.grid(row=5,column=7,sticky=E+S,padx=5,pady=1)



root.mainloop()