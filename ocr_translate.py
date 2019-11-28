from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk

from PIL import Image
import pytesseract
from textblob import TextBlob
import cv2

class frame(Tk):
    pass
    
		
		
		

class Home(frame):
    def __init__(self):
        super(frame,self).__init__()
        self.minsize(1000,1000)

		
		
        self.d1={'english':'eng','hindi':'hin','tamil':'tam','telugu':'tel','urdu':'urd','russian':'rus','spanish':'spa','arabic':'ara','bengali':'ben','french':'fra','gujarati':'guj','indonesian':'ind','italian':'ita','japanese':'jav','kannada':'kan','marati':'mar','malayalam':'mal','nepali':'nep','punjabi':'pan'}
        self.d2={'english':'en','hindi':'hi','tamil':'ta','telugu':'te','urdu':'ur','russian':'ru','spanish':'es','german':'de','french':'fr','arabic':'ar','bengali':'bn','gujarati':'gu','indonesian':'id','italian':'it','japanese':'ja','kannada':'kn','marati':'mr','malayalam':'ml','nepali':'ne','punjabi':'pa'}       
        self.labelFrame=ttk.LabelFrame(self,text="SELECT AN IMAGE FILE TO OPEN:")
        self.labelFrame.place(relx=0.02,rely=0.05,relheight=0.75
                , relwidth=0.3)

        self.entry1=Entry()
        self.entry1.place(relx=0.18,rely=0.72)

        
        
        self.openImageButton()
        

        self.label1=Label(text="Enter the Language To Perform OCR:")
        self.label1.place(relx=0.03,rely=0.72)

       

        
        
        
        self.labelFrame1=ttk.LabelFrame(self,text="DETECTED TEXT:")
        self.labelFrame1.place(relx=0.34,rely=0.05,relheight=0.75
                , relwidth=0.32)
        self.textbox1=Text()
        self.textbox1.place(relx=0.35,rely=0.1,relheight=0.55, relwidth=0.3)

    
        self.labelFrame2=ttk.LabelFrame(self,text="TRANSLATED TEXT")
        self.labelFrame2.place(relx=0.67,rely=0.05,relheight=0.75
                , relwidth=0.32)
        self.textbox2=Text(height=30,width=50)
        self.textbox2.place(relx=0.68,rely=0.1,relheight=0.55, relwidth=0.3)

        self.label2=Label(text="Enetr The Language To Be Translated:")
        self.label2.place(relx=0.35,rely=0.68)

        self.entry2=Entry()
        self.entry2.place(relx=0.5,rely=0.68)

        
        
        
        self.extractButton()
        self.translateButton()


        
	

    def openImageButton(self):
        self.button=ttk.Button(self.labelFrame,text="Browse Image",command=self.fileDialog)
        self.button.place(relx=0.25, rely=0.80, height=33, width=94, bordermode='ignore')
		
    def extractButton(self):
            
            
            
                            
            self.button1=ttk.Button(self.labelFrame,text="Perform OCR",command=self.performOcr)
            self.button1.place(relx=0.45, rely=0.80, height=33, width=94, bordermode='ignore')
            
    def translateButton(self):                
            self.button2=Button(text="Translate Text",command=self.translate)
            self.button2.place(relx=0.45, rely=0.72)
            
    def fileDialog(self):
        self.filename=filedialog.askopenfilename(initialdir="/",title="Select A File",filetype=(("jpeg","*.jpg"),("All Files","*.*")))
        self.imageShow(self.filename)
        
    def imageShow(self,path):
        image=Image.open(path)
        photo=ImageTk.PhotoImage(image)
        
        label=ttk.Label(self,image=photo)
        label.image=photo
        label.place(x=100,y=75)
        
    def performOcr(self):
            self.textbox1.delete(0.0,'end')
            self.entry1_value=self.entry1.get()
            for i in self.d1.keys():
                    if(i==self.entry1_value):
                            self.ocr=self.d1[i]

            self.img=cv2.imread(self.filename)
            self.text=pytesseract.image_to_string(Image.open(self.filename),lang=self.ocr)
            self.textbox1.insert(0.0,self.text)
    def translate(self):
            self.textbox2.delete(0.0,'end')
            self.entry2_value=self.entry2.get()
            for i in self.d2.keys():
                    if(i==self.entry2_value):
                            self.lang=self.d2[i]
            self.text2=TextBlob(self.text)
            self.detectlang=self.text2.detect_language()
            self.trans_text=self.text2.translate(from_lang=self.detectlang, to=self.lang)
            self.textbox2.insert(0.0,self.trans_text)

    
if __name__=='__main__':
    root=Home()
    root.mainloop()











