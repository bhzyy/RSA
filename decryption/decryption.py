import tkinter
class Program(tkinter.Tk):
    def clear_content(self):
        self.textBox_EnterTencrypt.delete(0, tkinter.END)

        self.textBox_Result.config(state="normal")
        self.textBox_Result.delete(0, tkinter.END)
        self.textBox_Result.config(state="readonly")

        self.textBox_dforDecryption.config(state="normal")
        self.textBox_dforDecryption.delete(0, tkinter.END)
        self.textBox_dforDecryption.config(state="readonly")

        self.textBox_nforDecryption.config(state="normal")
        self.textBox_nforDecryption.delete(0, tkinter.END)
        self.textBox_nforDecryption.config(state="readonly")

        self.label_EnterTencrypt.focus()

    def decrypt(self, text_encrypt, d, num):
        e = int(d)
        n = int(num)
        try:
            numbers = [int(x) for x in text_encrypt.split()]
        except ValueError:
            self.textBox_Result.config(state="normal")
            self.textBox_Result.delete(0, tkinter.END)
            self.textBox_Result.insert(0, "Invalid input!")
            self.textBox_Result.config(state="readonly")
            return 0

        decrypt_text = [chr((char ** e) % n) for char in numbers]
        decrypt_text_result = ''.join(decrypt_text)

        self.textBox_Result.config(state="normal")
        self.textBox_Result.delete(0, tkinter.END)
        self.textBox_Result.insert(0, decrypt_text_result)
        self.textBox_Result.config(state="readonly")

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("decryption")
        self.geometry("420x220")
    
    def create_widgets(self):
        self.label_EnterTencrypt=tkinter.Label(self,text="Enter text to decrypt:",font=("Arial", 12,"bold"))
        self.textBox_EnterTencrypt=tkinter.Entry(self,width=25,font=("Arial", 12))
        self.textBox_EnterTencrypt.icursor(tkinter.END)
        self.textBox_EnterTencrypt.xview(tkinter.END)

        self.label_Result=tkinter.Label(self,text="Result in decryption:",font=("Arial", 12,"bold"))
        self.textBox_Result=tkinter.Entry(self,width=25,font=("Arial", 12),state='readonly')
        self.textBox_Result.icursor(tkinter.END)
        self.textBox_Result.xview(tkinter.END)

        self.label_dforDecryption=tkinter.Label(self,text="D for Decryption:",font=("Arial", 12,"bold"))
        self.textBox_dforDecryption=tkinter.Entry(self,width=25,font=("Arial", 12),state='normal')
        self.textBox_dforDecryption.icursor(tkinter.END)
        self.textBox_dforDecryption.xview(tkinter.END)

        self.label_nforDecryption=tkinter.Label(self,text="N for Decryption:",font=("Arial", 12,"bold"))
        self.textBox_nforDecryption=tkinter.Entry(self,width=25,font=("Arial", 12),state='normal')
        self.textBox_nforDecryption.icursor(tkinter.END)
        self.textBox_nforDecryption.xview(tkinter.END)

        self.button_decrypt=tkinter.Button(self,text="Decrypt",font=("Arial", 11,"bold"),width=20,border=1,relief='solid',bg="#ddd",activebackground="#aaa",command=lambda: self.decrypt(self.textBox_EnterTencrypt.get(),self.textBox_dforDecryption.get(),self.textBox_nforDecryption.get()))
        self.button_Clear=tkinter.Button(self,text="Clear",font=("Arial", 11,"bold"),width=20,border=1,relief='solid',bg="#ddd",activebackground="#aaa",command=self.clear_content)

    def locate_widgets(self):
        self.label_EnterTencrypt.grid(row=0,column=0,padx=(5,2),sticky="w")
        self.textBox_EnterTencrypt.grid(row=0,column=1,columnspan=2)
        self.label_Result.grid(row=1,column=0,pady=(15,2),padx=(5,2),sticky="w")
        self.textBox_Result.grid(row=1,column=1,pady=(15,2),columnspan=2)
        self.label_dforDecryption.grid(row=2,column=0,pady=(15,2),padx=(5,2),sticky="w")
        self.textBox_dforDecryption.grid(row=2,column=1,pady=(15,2),columnspan=2)
        self.label_nforDecryption.grid(row=3,column=0,pady=(15,2),padx=(5,2),sticky="w")
        self.textBox_nforDecryption.grid(row=3,column=1,pady=(15,2),columnspan=2)
        self.button_decrypt.grid(row=4,column=0,pady=(20,2),padx=(10,0),columnspan=3,sticky='w')
        self.button_Clear.grid(row=4,column=1,pady=(20,2),padx=(50,0),columnspan=3,sticky='w')

    def show_program(self):
        self.mainloop()
window=Program()
window.create_widgets()
window.locate_widgets()
window.show_program()

