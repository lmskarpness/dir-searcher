import tkinter as tk
from tkinter import filedialog

class GUI:
    def __init__(self, dir_manager, search_engine):
        self.dir_manager = dir_manager
        self.search_engine = search_engine

        # Fonts
        self.label_font = ("Arial", 12)
        self.button_font = ("Arial", 8)
        self.tip_font = ("Helvetica", 8)


        # Widgets and window
        self.window = tk.Tk()
        self.setup_widgets()
        self.window.mainloop()

    # GUI Setup, labels + build functions
    def setup_widgets(self):
        self.window.geometry("450x540")
        self.window.resizable(False, False)
        self.window.title("Multi-Folder File Finder")

        # Menu bar
        self.create_menu_bar()

        # Search area GUI
        search_label = tk.Label(self.window, text="Search Term", font=self.label_font)
        search_label.pack()
        self.search_layout()

        # Directory area GUI
        dir_label = tk.Label(self.window, text="Add Directory", font=self.label_font)
        dir_tip = tk.Label(self.window, text="Enter a path, or click '+' to open the file explorer.", font=self.tip_font)
        dir_label.pack()
        dir_tip.pack()
        self.add_dir_layout()

        # Active Directories
        active_label = tk.Label(self.window, text="Active Directories", font=self.label_font)
        active_label.pack()
        # Active directories frame. Built with two columns, button/name
        self.active_frame = tk.Frame(self.window)
        self.active_frame.pack(fill="x", padx=10, pady=5)
        self.active_frame.columnconfigure(1, weight=1) # Dir name should expand

    # Menu bar
    def create_menu_bar(self):
        menubar = tk.Menu(self.window)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.window.config(menu=menubar)

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, 'w') as file:
                for directory in self.dir_manager.get_all():
                    file.write(directory + "\n")

    def load_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
                self.dir_manager.set_all(lines)  # replace current entries with loaded ones
        self.clear_actives_frame()
        self.load_active_dirs()

    # Search box GUI
    def search_layout(self):
        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=5)

        # Make column 0 stretch
        frame.columnconfigure(0, weight=1)

        # Entry box will stretch horizontal with 5px padding each side
        search_box = tk.Entry(frame)
        search_box.grid(row=0, column=0, sticky="ew", padx=5)

        search_btn = tk.Button(frame, text="Search", command=lambda: self.search(search_box.get()), font=self.button_font)
        search_btn.grid(row=1, column=0)

    # Add directory box and button GUI
    def add_dir_layout(self):
        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=5)

        entry = tk.Entry(frame, width = 30)
        entry.grid(row=0, column=0)

        button = tk.Button(frame, text="+", command=lambda: self.add_directory(entry.get()), font=self.button_font)
        
        button.grid(row=0, column=1)

    # Active Directories GUI
    def clear_actives_frame(self):
        for widget in self.active_frame.winfo_children():
            widget.destroy()

    def add_active_dir(self, directory, row):
        dir_str = tk.Label(self.active_frame, text=directory)
        dir_str.grid(row=row, column=1)

        button = tk.Button(self.active_frame, text="-", command=lambda: self.remove_directory(directory), font=self.button_font)
        button.grid(row=row, column=0)

    def load_active_dirs(self):
        dirs = self.dir_manager.get_all()
        for i, dir in enumerate(dirs):
            self.add_active_dir(dir, i)


    # Callbacks
    def add_directory(self, directory):
        if not directory:
            directory = tk.filedialog.askdirectory()
        
        self.clear_actives_frame()      # Clear list
        self.dir_manager.add(directory) # Add to directory manager
        self.load_active_dirs()         # Load active dirs to update GUI

    def remove_directory(self, directory):
        self.clear_actives_frame()         # Clear list
        self.dir_manager.remove(directory) # Remove from directory manager
        self.load_active_dirs()            # Reload active dirs

    def search(self, term):
        # Search string via FileSearchEngine.search(directories, target)
        results = self.search_engine.search(self.dir_manager.get_all(), term)
        print(results)
        pass

    def save(self):
        # Save currently listed directories to a txt file
        pass

    def load(self):
        # Load directories from a text file
        pass