from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
root = Tk()
root.title('Text Editor')
root.geometry('1200x750')
# Set Default Value for file path
global file_path
file_path = False
# Create New File Function
global selected
selected =False


def new_file():
    global file_path
    file_path = False
    txt_box.delete(1.0, END)
    root.title('New File-Notepad')
    status_bar.config(text='New File      ')


# Create Open File Function
def open_file():
    global counter
    counter = 0
    txt_box.delete(1.0, END)
    # ask for File
    txt_file = filedialog.askopenfilename(initialdir='c:/', title='Open File', filetypes=(('text files', '*.txt'),
                                          ('html files', '*.html'), ('Python Files', '*.py'), ('JavaScript Files', '*.js'), ('All Files', ('*.*'))))
    # Store the file path to reuse it
    global file_path
    file_path = txt_file
    open_file = open(txt_file, 'r')
    root.title(f'{txt_file}-Notepad')
    file_stuff = open_file.read()
    txt_box.insert(END, file_stuff)
    lines = file_stuff.split()
    for word in lines:
        counter += 1
    status_bar.config(text=f'{counter} words      ')

# Create Save as Function


def save_as():
    save_file = filedialog.asksaveasfilename(defaultextension='.*', title='Save File', initialdir='g:/', filetypes=(
        ('text file', '*.txt'), ('python files', '*.py'), ('all files', '*.*')))
    file_txt = open(save_file, 'w')
    file_txt = file_txt.write(txt_box.get(1.0, END))
    txt_box.delete(1.0, END)
    status_bar.config(text=f'Saved: {save_file}      ')

# save exisisted file in the same location


def save_file():
    if file_path:

        file_txt = open(file_path, 'w')
        file_txt = file_txt.write(txt_box.get(1.0, END))
        txt_box.delete(1.0, END)
        status_bar.config(text=f'Saved: {file_path}      ')
    else:
        save_as()


# //////////////////////////////////////////////////////*/////////////////////Edit Menu

# Cut text Fuction 
def cut_text(e):
  global selected
  # Check to see if we use keyboard shortcut 
  if e:
    selected= root.clipboard_get()
  else:
    if txt_box.selection_get():
      selected = txt_box.selection_get()
      root.clipboard_clear()
      root.clipboard_append(selected)
      txt_box.delete('sel.first','sel.last')

# Copy The text Function
def copy_text(e):
  global selected
  # Check to see if we used the shortcut
  if e:
    selected = root.clipboard_get()
  else:
    if txt_box.selection_get():
      selected = txt_box.selection_get()
      root.clipboard_clear()
      root.clipboard_append(selected)

# Paste The text Function 
def paste_text(e):
  global selected 
  # Check to see if shortcut is used 
  if e:
    selected = root.clipboard_get()
  if selected:
    position = txt_box.index(INSERT)
    txt_box.insert(position,selected)


# Disabled Word Wrap Function
def wrap_off():
  global wrap_off_btn
  wrap_off_btn['state'] = 'disabled'
  x_scroll= Scrollbar(main_frame,orient='horizontal')
  x_scroll.pack(side=BOTTOM,fill=X)

  txt_box.config(wrap='none',xscrollcommand=x_scroll.set)
  x_scroll.configure(command=txt_box.xview)
  edit_menu.entryconfig('Word Wrap', state='normal')
    
# ENabled Word Wrap Function 
def wrap_on():
  wrap_off_btn['state'] = 'normal'
  txt_box.config(wrap='word')
  edit_menu.entryconfig('Word Wrap', state='disabled')

  



# ///////////////////////////////////////////////////////Colors Menu
# Change the background theme Function
def bg_color():
  bg_color=colorchooser.askcolor()[1]
  if bg_color:
    txt_box.config(bg=bg_color)

# Change Whole  Text Color 
def whole_txt_color():
  txt_color=colorchooser.askcolor()[1]
  if txt_color:
    txt_box.config(fg=txt_color)

# Change Selected Color text
def selected_txt_color():
  if txt_box.tag_ranges("sel"):
    color_picker = colorchooser.askcolor()[1]
    
    # Create font color
    selected_color = font.Font(txt_box, txt_box.cget('font'))
    # Configure tag color name
    txt_box.tag_configure(
        'colored', foreground=color_picker, font=selected_color)
    current_tag = txt_box.tag_names('sel.first')
    # IF Statemnt
    if 'colored' in current_tag:
      txt_box.tag_remove('colored', 'sel.first', 'sel.last')
    else:
      txt_box.tag_add('colored', 'sel.first', 'sel.last')   
  else:
    messagebox.showerror('Erorr', 'Choose Text First!')
    
   
# //////////////////////////////////////////////////////Options Menu Functions
#** Night Mood OFF Function
def night_off():
  main_color = 'SystemButtonFace'
  second_color = 'SystemButtonFace'
  third_color= 'black'
  # Root Color Dark Mode
  root.config(bg=main_color)
  status_bar.config(bg=main_color,fg=third_color)
  txt_box.config(bg=second_color,fg=third_color)
  tool_bar_frame.config(bg=main_color)
  # buttons
  bold_btn.config(bg=main_color,fg=third_color)
  italic_btn.config(bg=main_color,fg=third_color)
  undo_btn.config(bg=main_color, fg=third_color)
  redo_btn.config(bg=main_color, fg=third_color)
  wrap_off_btn.config(bg=main_color, fg=third_color)
  change_sel_color_btn.config(bg=main_color, fg=third_color)
  # Menu Bar Items Color 
  file_menu.config(bg=second_color)
  edit_menu.config(bg=second_color)
  color_menu.config(bg=second_color)
  option_menu.config(bg=second_color)

#** Night Mood ON Function
def night_on():
  main_color='black'
  second_color = '#373737'
  third_color= 'green'
  # Root Color Dark Mode
  root.config(bg=main_color)
  status_bar.config(bg='#0d9ad6',fg='white')
  txt_box.config(bg=second_color,fg='white')
  tool_bar_frame.config(bg=main_color)
  # buttons
  bold_btn.config(bg=main_color,fg=third_color)
  italic_btn.config(bg=main_color,fg=third_color)
  undo_btn.config(bg=main_color, fg=third_color)
  redo_btn.config(bg=main_color, fg=third_color)
  wrap_off_btn.config(bg=main_color, fg=third_color)
  change_sel_color_btn.config(bg=main_color, fg=third_color)
  # Menu Bar Items Color 
  file_menu.config(bg=second_color)
  edit_menu.config(bg=second_color)
  color_menu.config(bg=second_color)
  option_menu.config(bg=second_color)


# Bold The Text Function
def bold_it():
    # Create the font
    bold_font = font.Font(txt_box, txt_box.cget('font'))
    bold_font.configure(weight='bold')
    # Configure The Tag
    txt_box.tag_config('bold', font=bold_font)
    current_tag = txt_box.tag_names('sel.first')

    # IF Statemnt To Check if is it bold or not
    if 'bold' in current_tag:
        txt_box.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        txt_box.tag_add('bold', 'sel.first', 'sel.last')
    


# Italic The Text Function
def italic_it():
    italic_font = font.Font(txt_box, txt_box.cget('font'))
    italic_font.configure(slant='italic')
    # Configure The Tag
    txt_box.tag_config('italic', font=italic_font)
    current_tag = txt_box.tag_names('sel.first')
    # IF Statement
    if 'italic' in current_tag:
        txt_box.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        txt_box.tag_add('italic', 'sel.first', 'sel.last')


# Create Tool bar frame
tool_bar_frame = Frame(root)
tool_bar_frame.pack(fill=X,pady=5)

# Create Bold Button
bold_btn = Button(tool_bar_frame, text='Bold', font=('Comic Sans MS', 8), command=bold_it)
bold_btn.grid(row=0, column=0, sticky=W, padx=5)

# Create Italic Button
italic_btn = Button(tool_bar_frame, text='Italic', font=('Comic Sans MS', 8), command=italic_it)
italic_btn.grid(row=0, column=1, padx=5)
# Create Wrap Off Button
wrap_off_btn = Button(tool_bar_frame, text='Wrap Off',font=('Comic Sans MS', 8),command=wrap_off)
wrap_off_btn.grid(row=0, column=4, padx=5)

# Change Selected Color Text Button
change_sel_color_btn = Button(tool_bar_frame, text='Change Selected text Color', font=('Comic Sans MS', 8), command=selected_txt_color)
change_sel_color_btn.grid(row=0,column=5,pady=5)

# Create main Frame
main_frame = Frame(root)
main_frame.pack()
# Set Scroll bar
scroll = Scrollbar(main_frame)
scroll.pack(side=RIGHT, fill=Y)

# Create Text Box Erea and set yscrollcommand for that

txt_box = Text(main_frame, font=('Hevatica', 18), selectbackground='yellow',selectforeground='black', undo=True, width=105, height=24, yscrollcommand=scroll.set)
txt_box.pack(pady=5)
# Configure the scroll bar
scroll.configure(command=txt_box.yview)

# ////////////////////////////////// Undo Redo Butttons
# Create Undo Button
undo_btn = Button(tool_bar_frame, text='Undo', font=(
    'Comic Sans MS', 8), command=txt_box.edit_undo)
undo_btn.grid(row=0, column=2, padx=5)

# Create Redo Button
redo_btn = Button(tool_bar_frame, text='Redo', font=(
    'Comic Sans MS', 8), command=txt_box.edit_redo)
redo_btn.grid(row=0, column=3, padx=5)

# create Minu bar
my_menu = Menu(root)
root.config(menu=my_menu)
# Create File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save as', command=save_as)

file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Create Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', accelerator=('Ctrl-C'), command=lambda: copy_text(False))
edit_menu.add_command(label='Cut', accelerator=('Ctrl-X'),command=lambda: cut_text(False))
edit_menu.add_command(label='Paste', accelerator=('Ctrl-V'),command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label='Undo', accelerator=('Ctrl-Z'), command=txt_box.edit_undo)
edit_menu.add_command(label='Redo', accelerator=('Ctrl-Y'), command=txt_box.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label='Word Wrap', accelerator=('ON'),command=wrap_on)

# Make a theme menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Colors', menu=color_menu)
# Add themes to theme_menu
color_menu.add_command(label='Change Slected Text Color',command=selected_txt_color)
color_menu.add_command(label='Change Whole Text Color',command=whole_txt_color)
color_menu.add_command(label='Background Color..',command=bg_color)
# Options Menu
option_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Options',menu=option_menu)
option_menu.add_command(label='Dark Mode OFF',command=night_off)
option_menu.add_command(label='Dark Mode ON',command=night_on)

# Create Staus Bar
status_bar = Label(root, text='Ready      ', anchor=E)
status_bar.pack(side=BOTTOM, fill=X, ipady=10)

# Some Keyboard Binding Shortcuts 
root.bind('<Control-Key-C>',copy_text)  # Copy shortcut
root.bind('<Control-Key-X>',cut_text)   # Cut Shortcut
root.bind('<Control-Key-V>',paste_text)  # Paste Shortcut

root.mainloop() 
