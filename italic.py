import tkinter as tk
from tkinter import filedialog, messagebox, font

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        
        # Text Widget
        self.text_area = tk.Text(root, wrap='word', undo=True)
        self.text_area.pack(fill='both', expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)
        self.scrollbar.pack(side='right', fill='y')

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        
        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label="Select All", command=lambda: self.text_area.event_generate("<<SelectAll>>"))

        # Format Menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Bold", command=self.bold_text)
        self.format_menu.add_command(label="Italic", command=self.italic_text)
        self.format_menu.add_command(label="Underline", command=self.underline_text)

        # Shortcut bindings
        root.bind('<Control-n>', lambda event: self.new_file())
        root.bind('<Control-o>', lambda event: self.open_file())
        root.bind('<Control-s>', lambda event: self.save_file())
        root.bind('<Control-Shift-S>', lambda event: self.save_as_file())
        root.bind('<Control-b>', lambda event: self.bold_text())
        root.bind('<Control-i>', lambda event: self.italic_text())
        root.bind('<Control-u>', lambda event: self.underline_text())

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File - Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.root.title(f"{file_path} - Text Editor")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
                self.root.title(f"{file_path} - Text Editor")

    def save_as_file(self):
        self.save_file()

    def bold_text(self):
        current_tags = self.text_area.tag_names(tk.SEL_FIRST)
        if 'bold' in current_tags:
            self.text_area.tag_remove('bold', tk.SEL_FIRST, tk.SEL_LAST)
        else:
            self.text_area.tag_add('bold', tk.SEL_FIRST, tk.SEL_LAST)
            bold_font = font.Font(self.text_area, self.text_area.cget("font"))
            bold_font.configure(weight='bold')
            self.text_area.tag_configure('bold', font=bold_font)

    def italic_text(self):
        current_tags = self.text_area.tag_names(tk.SEL_FIRST)
        if 'italic' in current_tags:
            self.text_area.tag_remove('italic', tk.SEL_FIRST, tk.SEL_LAST)
        else:
            self.text_area.tag_add('italic', tk.SEL_FIRST, tk.SEL_LAST)
            italic_font = font.Font(self.text_area, self.text_area.cget("font"))
            italic_font.configure(slant='italic')
            self.text_area.tag_configure('italic', font=italic_font)

    def underline_text(self):
        current_tags = self.text_area.tag_names(tk.SEL_FIRST)
        if 'underline' in current_tags:
            self.text_area.tag_remove('underline', tk.SEL_FIRST, tk.SEL_LAST)
        else:
            self.text_area.tag_add('underline', tk.SEL_FIRST, tk.SEL_LAST)
            underline_font = font.Font(self.text_area, self.text_area.cget("font"))
            underline_font.configure(underline=True)
            self.text_area.tag_configure('underline', font=underline_font)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
