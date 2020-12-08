import tkinter as tk
import os
from sys import argv
from PIL import ImageTk, Image
import py_mail

class Application:
    def __init__(self, master):
        # Initialize lists
        self.location = []
        self.med = []

        self.master = master
        self.frame = tk.Frame(self.master,width=800,height=450)
        self.canvas = tk.Canvas(self.frame,width=600,height=400,bg='grey')
        self.canvas.place(x=20,y=20)
        self.pbGetImage = tk.Button(self.frame, text='Get Image',width=10,command=self.get_image)
        self.pbGetImage.place(x=650,y=20)
        self.pbDetect = tk.Button(self.frame, text='Detect',width=10, command = lambda : predict.main())
        self.pbDetect.place(x=650,y=55)
        self.tbLocation = tk.Text(self.frame, height = 1, width = 12)
        self.tbLocation.insert('1.0','Location?')
        self.tbLocation.place(x=650,y=90)
        self.tbMedName = tk.Text(self.frame, height = 1, width = 12)
        self.tbMedName.insert('1.0','Med Name')
        self.tbMedName.place(x=650,y=125)
        self.pbRecord = tk.Button(self.frame, text='Record',width=10, command=self.record)
        self.pbRecord.place(x=650,y=160)
        self.pbSendReport = tk.Button(self.frame, text='Send Report',width=10,command=lambda : py_mail.main())
        self.pbSendReport.place(x=650,y=195)
        self.frame.pack()

    def get_image(self):
        os.system('fswebcam --no-banner --save img.jpg -d /dev/video0 2> /dev/null')
        self.img = ImageTk.PhotoImage(Image.open('./img.jpg'))
        self.canvas.create_image(300,200,image=self.img)
        self.canvas.image = self.img

    #def detect(self):

    def record(self):
        self.location = self.location + [str(self.tbLocation.get('1.0', 'end-1c'))]
        self.med = self.med + [str(self.tbMedName.get('1.0', 'end-1c'))]
        self.target = open('meds.txt','w')
        self.target.truncate() # clear file
        for i in range(0, len(self.location)):
            self.target.write(self.location[i] + '\t')
            self.target.write(self.med[i] + '\n')
        self.target.close()


def main():
    root = tk.Tk()
    root.title("AdaptoPharm")
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
