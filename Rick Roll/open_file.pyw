from tkinter import filedialog
from tkinter import messagebox
import sys
if len(sys.argv) == 1:
    messagebox.showerror(sys.argv[0], 'No specified parameter \"default_path\"')
else:
    file = filedialog.askopenfilename(
        initialdir = sys.argv[1],
        filetypes = [
            ('All files','*.*'),
            ('Don\'t','*.R'),
            ('tell','*.I'),
            ('me','*.C'),
            ('you\'re','*.K'),
            ('too','*.R'),
            ('blind','*.O'),
            ('to','*.L'),
            ('see','*.L')
        ]
    )