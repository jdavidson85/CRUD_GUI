import tkinter
import tkinter.messagebox
import tkinter.font as tkfont
import pickle


class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=13)

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        self.look.configure(indicatoron=True)
        self.add.configure(indicatoron=True)
        self.change.configure(indicatoron=True)
        self.delete.configure(indicatoron=True)

        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu, width=10)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, width=10)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class LookGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.info_string = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search, width=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.info_string.set(result)

    def go_back(self):
        self.look.destroy()


def main():
    root = tkinter.Tk()
    _ = CrudGUI(root)
    root.mainloop()


main()

