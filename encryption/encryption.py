import tkinter
import random
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

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mod(self, a, b):
        for d in range(1,b):
            if (a*d)%b==1:
                return d
    
    def is_prime(self, n):
        prime=True
        divisor=2
        while divisor<=n**0.5 and prime:
            if n%divisor==0:
                prime=False
            divisor+=1
        return prime
    
    def generate_prime(self,start=100,end=300):
        while True:
            p = random.randint(start, end)
            if self.is_prime(p):
                return p

    def generate_keypair_encrypt(self):
        p=self.generate_prime()
        q=self.generate_prime()
        while q==p:
            q=self.generate_prime()
        
        self.n=q*p
        phi_oil=(p-1)*(q-1)

        e=random.randint(2, phi_oil)
        while self.gcd(e, phi_oil) != 1:
            e = random.randint(2, phi_oil)

        self.d=self.mod(e,phi_oil)
        return (e,self.n)

    def encrypt(self,text):
        e, n = self.generate_keypair_encrypt()
        text = [ord(char) for char in text]
        encrypt_text = [(char ** e) % n for char in text]
        encrypt_text_result = ' '.join(str(char) for char in encrypt_text)
        
        self.textBox_Result.config(state="normal")
        self.textBox_Result.delete(0, tkinter.END)
        self.textBox_Result.insert(0, encrypt_text_result)
        self.textBox_Result.config(state="readonly")

        self.textBox_dforDecryption.config(state="normal")
        self.textBox_dforDecryption.delete(0, tkinter.END)
        self.textBox_dforDecryption.insert(0, self.d)
        self.textBox_dforDecryption.config(state="readonly")

        self.textBox_nforDecryption.config(state="normal")
        self.textBox_nforDecryption.delete(0, tkinter.END)
        self.textBox_nforDecryption.insert(0, self.n)
        self.textBox_nforDecryption.config(state="readonly")

        with open("encrypted.txt",mode="a") as file:
            file.write(f"encrypted texr : {self.textBox_Result.get()}\nD for decryption : {self.textBox_dforDecryption.get()}\nN for encryption : {self.textBox_nforDecryption.get()}\n")
            file.write("<------------------------------------------------------------------------------------------------------>")
   
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("encryption")
        self.geometry("420x220")
    
    def create_widgets(self):
        self.label_EnterTencrypt=tkinter.Label(self,text="Enter text to encrypt:",font=("Arial", 12,"bold"))
        self.textBox_EnterTencrypt=tkinter.Entry(self,width=25,font=("Arial", 12))
        self.textBox_EnterTencrypt.icursor(tkinter.END)
        self.textBox_EnterTencrypt.xview(tkinter.END)

        self.label_Result=tkinter.Label(self,text="Result in encryption:",font=("Arial", 12,"bold"))
        self.textBox_Result=tkinter.Entry(self,width=25,font=("Arial", 12),state='readonly')
        self.textBox_Result.icursor(tkinter.END)
        self.textBox_Result.xview(tkinter.END)

        self.label_dforDecryption=tkinter.Label(self,text="D for Decryption:",font=("Arial", 12,"bold"))
        self.textBox_dforDecryption=tkinter.Entry(self,width=25,font=("Arial", 12),state='readonly')
        self.textBox_dforDecryption.icursor(tkinter.END)
        self.textBox_dforDecryption.xview(tkinter.END)

        self.label_nforDecryption=tkinter.Label(self,text="N for Decryption:",font=("Arial", 12,"bold"))
        self.textBox_nforDecryption=tkinter.Entry(self,width=25,font=("Arial", 12),state='readonly')
        self.textBox_nforDecryption.icursor(tkinter.END)
        self.textBox_nforDecryption.xview(tkinter.END)

        self.button_Encrypt=tkinter.Button(self,text="Encrypt",font=("Arial", 11,"bold"),width=20,border=1,relief='solid',bg="#ddd",activebackground="#aaa",command=lambda: self.encrypt(self.textBox_EnterTencrypt.get()))
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
        self.button_Encrypt.grid(row=4,column=0,pady=(20,2),padx=(10,0),columnspan=3,sticky='w')
        self.button_Clear.grid(row=4,column=1,pady=(20,2),padx=(50,0),columnspan=3,sticky='w')

    def show_program(self):
        self.mainloop()

window=Program()
window.create_widgets()
window.locate_widgets()
window.show_program()

