from tkinter import *
from tkinter import messagebox,filedialog
from pathlib import Path
import shutil


class Application:
    def __init__(self):
        self.root=Tk()
        self.root.title=("File Organizer")
        self.root.iconbitmap("Icon.ico")
        """p=PhotoImage(file='Icon.ico')
        self.root.iconphoto(False,'Icon.ico')"""

        self.canvas = Canvas(self.root,width=400,height=200)
        self.canvas.configure(bg="#1c2461")
        self.canvas.pack()

        self.lbl1=Label(self.root,text="Organize your files with a single click!",fg="#dbe0ff",bg="#1c2461")
        self.lbl1.configure(font=("Times",18,"bold"))
        self.canvas.create_window(200,20,window=self.lbl1)

        self.entry=Entry(self.root,width=50)
        self.canvas.create_window(180,70,window=self.entry)

        self.lbl2=Label(self.root,text="Enter or browse the Directory/Folder path which you want to Organize",fg="#dbe0ff",bg="#1c2461")
        self.canvas.create_window(200,105,window=self.lbl2)


        def btn_clicked():
            dir_name=self.entry.get()
            try:
                dir = dir_name.replace("\\", "/")

                make_folder = Path(dir + "/Videos")
                make_folder.mkdir(exist_ok=True)

                make_folder = Path(dir + "/Audio")
                make_folder.mkdir(exist_ok=True)

                make_folder = Path(dir + "/Images")
                make_folder.mkdir(exist_ok=True)

                make_folder = Path(dir + "/Programing Files")
                make_folder.mkdir(exist_ok=True)

                make_folder = Path(dir + "/Miscelleneous")
                make_folder.mkdir(exist_ok=True)

                make_folder = Path(dir + "/Documents")
                make_folder.mkdir(exist_ok=True)

                directory =Path(dir)
                files_in_dir = directory.iterdir()
                for entry in files_in_dir:
                    if entry.is_file():

                        source_folder = dir + "/" + entry.name
                        dest_folder = dir + "/"

                        if ".txt" in entry.name or ".pdf" in entry.name or ".doc" in entry.name or ".docx" in entry.name or ".odt" in entry.name or ".rtf" in entry.name or ".tex" in entry.name or ".wpd" in entry.name:
                            dest_folder += "Documents"
                        elif ".3g2" in entry.name or ".3gp" in entry.name or ".avi" in entry.name or ".flv" in entry.name or ".h264" in entry.name or ".mkv" in entry.name or ".mov" in entry.name or ".m4v" in entry.name or ".mp4" in entry.name or ".mpg" in entry.name or ".mpeg" in entry.name or ".rm" in entry.name or ".sfw" in entry.name or ".wob" in entry.name or ".wmv" in entry.name:
                            dest_folder += "Audio"
                        elif ".aif" in entry.name or ".cda" in entry.name or ".mp3" in entry.name or ".mid" in entry.name or ".midi" in entry.name or ".mpa" in entry.name or ".ogg" in entry.name or ".wav" in entry.name or ".wpl" in entry.name or ".wma" in entry.name:
                            dest_folder += "Videos"
                        elif ".ai" in entry.name or ".bmp" in entry.name or ".gif" in entry.name or ".ico" in entry.name or ".jpeg" in entry.name or ".jpg" in entry.name or ".png" in entry.name or ".ps" in entry.name or ".psd" in entry.name or ".svg" in entry.name or ".tif" in entry.name or ".tiff" in entry.name:
                            dest_folder += "Images"
                        elif ".c" in entry.name or ".class" in entry.name or ".cpp" in entry.name or ".java" in entry.name or ".py" in entry.name or ".cs" in entry.name or ".h" in entry.name or ".pl" in entry.name or ".sh" in entry.name or ".swift" in entry.name or ".vb" in entry.name:
                            dest_folder += "Programing Files"
                        else:
                            dest_folder += "Miscelleneous"
                        try:
                            shutil.move(source_folder, dest_folder)
                        except:
                            done = "{} already exists in '{}' folder.\n Delete duplicate File?".format(entry.name, dest_folder)
                            answer=messagebox.askquestion("Error!",done)
                            if answer=="yes":
                                del_file=Path(source_folder)
                                del_file.unlink()
                        else:
                            pass

            except:
                messagebox.showerror("Error!","Wrong Path")

            messagebox.showinfo(":)","Voila! You're Done")

        self.btn=Button(self.root,text="Click to see Magic!",command=btn_clicked)
        self.canvas.create_window(200,150,window=self.btn)

        def select_folder():
            directory=filedialog.askdirectory(parent=self.root,initialdir='c:/')
            self.entry.insert(0,directory)

        self.photo=PhotoImage(file="browse-folder.png")
        self.photoimage=self.photo.subsample(5,5)
        self.btn2=Button(self.root,command=select_folder,image=self.photoimage)
        self.canvas.create_window(360,70,window=self.btn2)

        self.root.mainloop()

obj=Application()