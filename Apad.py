import tkinter as tk 
from tkinter import Menu, PhotoImage, ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os
from tkinter.constants import BOTTOM


main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Apad text editor - Un Title')
main_application.wm_iconbitmap('icon.ico')





url=''
url2=''
content2=''
base_name=''
base_name2=''

def new_func(event=None):
    text_editor.delete('1.0',tk.END)
    main_application.title('Apad text editor - Un Title')

# def open_func(event=None):
#     pass

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 

def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 

def save_func(event=None):
    global url ,content2,url2,base_name,base_name2
    #try:
    if url:
        content = str(text_editor.get(1.0, tk.END))
        # url2=url
        content2 = text_editor.get(1.0, tk.END)
        # os.open(url,'w')
        url.write(content2)
        #with open(url, 'w', encoding='utf-8') as fw:
            #fw.write(content)
        # os.close(url)29
    else:
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        content2 = text_editor.get(1.0, tk.END)
        url.write(content2)
        url.close()
    base_name=os.path.basename(str(url))
    # for i in base_name:
    #     base_name2.append(i)
    # j=0
    # while j<=28:
    #     base_name2.pop(-1)
    #     j+=1
    # d=0
    # while j<=len(base_name2):
    #     base_name+=base_name2[d]
    #     d+=1
    # # print(base_name2)
    base_name2=base_name.replace("' mode='w' encoding='cp1252'>",'')
    main_application.title(str(base_name2))

    #except:
        #return 

def open_func(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))

def save_as_func(event=None):
    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    content2 = text_editor.get(1.0, tk.END)
    url.write(content2)
    url.close()

text_changed = False 
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 

def change_theme(event=None):
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color) 

def clear_all_func(event=None):
    text_editor.delete('1.0',tk.END)


def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()













new_icon=PhotoImage(file=r'icons2\new.png')
open_icon=PhotoImage(file=r'icons2\open.png')
save_icon=PhotoImage(file=r'icons2\save.png')
save_as_icon=PhotoImage(file=r'icons2\save_as.png')
exit_icon=PhotoImage(file=r'icons2\exit.png')


main_menu=tk.Menu(main_application)

file = tk.Menu(main_menu,tearoff=False)
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_func)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_func)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_func)
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Alt+A',command=save_as_func)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)

edit = tk.Menu(main_menu,tearoff=False)

copy_icon=PhotoImage(file=r'icons2\copy.png')
paste_icon=PhotoImage(file=r'icons2\paste.png')
cut_icon=PhotoImage(file=r'icons2\cut.png')
clear_all_icon=PhotoImage(file=r'icons2\clear_all.png')
find_icon=PhotoImage(file=r'icons2\find.png')

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C', command=lambda:text_editor.delete(1.0,'end'))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

tool_bar_icon=PhotoImage(file=r'icons2\tool_bar.png')
status_bar_icon=PhotoImage(file=r'icons2\status_bar.png')

view = tk.Menu(main_menu,tearoff=False)
view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar, image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar, image=status_bar_icon,compound=tk.LEFT, command=hide_statusbar)

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#474747', '#d3b774'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


color_theme = tk.Menu(main_menu, tearoff=False)

# color_theme.add_command(label='Light Default',image=light_default_icon,compound=tk.LEFT)
# color_theme.add_command(label='Light Plus',image=light_plus_icon,compound=tk.LEFT)
# color_theme.add_command(label='Dark',image=dark_icon,compound=tk.LEFT)
# color_theme.add_command(label='Red',image=red_icon,compound=tk.LEFT)
# color_theme.add_command(label='Monkai',image=monokai_icon,compound=tk.LEFT)
# color_theme.add_command(label='Night Blue',image=night_blue_icon,compound=tk.LEFT)
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1 

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
main_application.config(menu=main_menu)


tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

end_bar = ttk.Label(main_application, text='Copyright @2020 - techyattra.in, musicalchair.in')
end_bar.pack(side=tk.BOTTOM)


## font box 
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_cb = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_cb['values'] = font_tuple
font_cb.current(font_tuple.index('Arial'))

## size box 
size_var = tk.IntVar()
font_size_cb = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size_cb['values'] = tuple(range(8,81))
font_size_cb.current(4)

font_cb.grid(row=0,column=0,padx=5,pady=5)
font_size_cb.grid(row=0,column=1,padx=5,pady=5)



text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
#text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.pack(fill=tk.BOTH,expand=True)

text_editor.bind('<<Modified>>', changed)


def change_font(event=None):
    global current_font_family,current_font_size
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size,current_font_family
    current_font_size = size_var.get()
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))




font_cb.bind("<<ComboboxSelected>>",change_font)
font_size_cb.bind("<<ComboboxSelected>>",change_fontsize)

bold_icon=PhotoImage(file=r'icons2/bold.png')
italic_icon=PhotoImage(file=r'icons2/italic.png')
underline_icon=PhotoImage(file=r'icons2/underline.png')
font_color_icon=PhotoImage(file=r'icons2/font_color.png')
align_center_icon=PhotoImage(file=r'icons2/align_center.png')
align_left_icon=PhotoImage(file=r'icons2/align_left.png')
align_right_icon=PhotoImage(file=r'icons2/align_right.png')

bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

this_app_copyright = 'Copyright @2020 - techyattra.in, musicalchair.in'

font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

align_center_btn=ttk.Button(tool_bar,image=align_center_icon,command=align_center)
align_center_btn.grid(row=0,column=7,padx=5)

align_left_btn=ttk.Button(tool_bar,image=align_left_icon, command=align_left)
align_left_btn.grid(row=0,column=6,padx=5)

align_right_btn=ttk.Button(tool_bar,image=align_right_icon,command=align_right)
align_right_btn.grid(row=0,column=8,padx=5)



def change_bold():
    current_font_size=size_var.get()
    current_font_family=font_family.get()
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

def change_italic():
    current_font_size=size_var.get()
    current_font_family=font_family.get()
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
italic_btn.configure(command=change_italic)

def change_underline():
    current_font_size=size_var.get()
    current_font_family=font_family.get()
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)

def change_font_color():
    color_var=colorchooser.askcolor()
    text_editor.config(fg=color_var[1])

font_color_btn.configure(command=change_font_color)







status_bar=ttk.Label(main_application,text='Characters : 0 , Words : 0')
status_bar.pack(side=BOTTOM)


main_application.bind("<Control-n>",new_func)
main_application.bind("<Control-o>",open_func)
main_application.bind("<Control-s>",save_func)
main_application.bind("<Alt-a>",save_as_func)
main_application.bind("<Control-q>",exit_func)

main_application.bind("<Control-c>",lambda:text_editor.event_generate("<Control c>"))
main_application.bind("<Control-v>",lambda:text_editor.event_generate("<Control v>"))
main_application.bind("<Control-x>",lambda:text_editor.event_generate("<Control x>"))
main_application.bind("<Control-Alt-c>",clear_all_func)
main_application.bind("<Control-f>",find_func)






main_application.mainloop()
