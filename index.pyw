import threading
import tkinter as tk
from tkinter import ttk

from decoding import decoder
from encoding import encoder
from morse_alphabet import packages
import rsa_module

class PlayThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)   
        
    def run(self):
        gui.button_sd.configure(state = 'disabled')
        encoder.play_text(gui.text_view.get('1.0', 'end-1c'))
        gui.button_sd.configure(state = 'active')
        
class UI:
    
    def __init__(self, root):
        self.root = root
        root.title('Encoder')
        root.resizable(0,0)
 
        tabs = ttk.Notebook(root)
        tab_encode = ttk.Frame(tabs)
        tab_decode = ttk.Frame(tabs)

        self.useERSA = tk.BooleanVar()
        self.useERSA.set(0)
        self.useDRSA = tk.BooleanVar()
        self.useDRSA.set(0)

        #region tab_encode
        self.ent1 = tk.Text(tab_encode, height = 10, width = 50, font=('Consolas', 11))
        self.ent1.grid(column = 0, row = 0, padx = 5, pady = 5, columnspan = 2)

        self.enc_text = tk.Label(tab_encode, text = 'Additional Encoding')
        self.enc_text.grid(column = 0, row = 1, sticky = 'w'+'e', columnspan = 2)
        self.radio_off = tk.Radiobutton(tab_encode, text ='Off', variable = self.useERSA, value = 0)
        self.radio_off.grid(column = 0, row = 2, sticky = 'w'+'e')
        self.radio_rsa = tk.Radiobutton(tab_encode, text = 'RSA', variable = self.useERSA, value = 1)
        self.radio_rsa.grid(column = 1, row = 2, sticky = 'w'+'e')

        self.text_view = tk.Text(tab_encode, height = 10, width = 50, font=('Consolas', 11), state = 'disabled')
        self.text_view.grid(column = 0, row = 3, padx = 5, sticky = 'w'+'e', columnspan = 2)

        self.button = ttk.Button(tab_encode, text = 'Encode', command = self.button_pressed_encode)
        self.button.grid(column = 0, row = 4, padx = 5, sticky = 'w'+'e')

        self.button_sd = ttk.Button(tab_encode, text = 'Play code', command = self.play_text)
        self.button_sd.grid(column = 1, row = 4, padx = 5, pady = 5, sticky = 'w'+'e')
        #endregion

        #region tab_decode
        self.ent2 = tk.Text(tab_decode, height = 10, width = 50, font=('Consolas', 11))
        self.ent2.grid(column = 0, row = 0, padx = 5, pady = 5, columnspan = 2)

        self.enc_text2 = tk.Label(tab_decode, text = 'Additional Encoding')
        self.enc_text2.grid(column = 0, row = 1, sticky = 'w'+'e', columnspan = 3)
        self.radio_off2 = tk.Radiobutton(tab_decode, text ='Off', variable = self.useDRSA, value = 0)
        self.radio_off2.grid(column = 0, row = 2, sticky = 'w'+'e')
        self.radio_rsa2 = tk.Radiobutton(tab_decode, text = 'RSA', variable = self.useDRSA, value = 1)
        self.radio_rsa2.grid(column = 1, row = 2, sticky = 'w'+'e')

        self.text_view2 = tk.Text(tab_decode, heigh = 10, width = 50, font=('Consolas', 11))
        self.text_view2.grid(column = 0, row = 3, padx = 5, columnspan = 2)
        
        self.lang_ch = tk.StringVar(tab_decode)
        self.lang_menu = ttk.OptionMenu(tab_decode, self.lang_ch, *self.__getPackages())
        self.lang_menu.grid(column = 1, row = 4, padx = 5, pady = 3, sticky = 'w'+'e')

        self.button2 = ttk.Button(tab_decode, text = 'Decode', command = self.button_pressed_decode, width = 17)
        self.button2.grid(column = 0, row = 4, padx = 5, pady = 5, sticky = 'w'+'e')
        #endregion

        tabs.add(tab_encode, text = 'Encode')
        tabs.add(tab_decode, text = 'Decode')
        tabs.pack(fill = tk.BOTH)

        self.cipher = rsa_module.RSA_Cipher()
        self.cipher.generate_key(2048)

    def button_pressed_encode(self):
        self.text_view.configure(state = 'normal')
        self.text_view.delete('1.0', 'end-1c')
        self.text_view.insert('1.0', encoder.encodeToMorse(self.ent1.get('1.0', 'end-1c'), self.useERSA.get(), self.cipher))
        self.text_view.configure(state = 'disabled')

    def button_pressed_decode(self):
        self.text_view2.configure(state = 'normal')
        self.text_view2.delete('1.0', 'end-1c')
        self.text_view2.insert('1.0', decoder.decodeMorse(self.ent2.get('1.0', 'end-1c'), self.lang_ch.get(), self.useDRSA.get(), self.cipher))
        self.text_view2.configure(state = 'disabled')

    def __getPackages(self):
        lang_list = ["Pick Language"]
        for package in packages:
            if package.IfBasePackage == False:
                lang_list.append(package.name)
        return lang_list

    def play_text(self):
        thread = PlayThread()
        thread.start()
  
if __name__ == '__main__':
    root = tk.Tk()
    gui = UI(root)
    root.mainloop()
    
    
