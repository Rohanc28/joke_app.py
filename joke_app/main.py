#make joke.py
# JOKE
import textwrap
import json
import requests
import tkinter as tk

def anyjoke():
  response = requests.get("https://v2.jokeapi.dev/joke/Programming")
  json_data = json.loads(response.text)

  #try single
  try:
    quote = "'' "+str(json_data["joke"]) +  " ''"
    
  #try twopart
  except:
    quote = "'' " + str(json_data["setup"]) + "\n" + str(json_data["delivery"]) + " ''"
  res=""
  res=('\n'.join(textwrap.wrap(quote,30,break_long_words=False)))
  label.config(text=res,bg='black',fg='white',width=100)
  #label.config(text=(textwrap.wrap(quote, width=30, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None)))
    

window=tk.Tk()
window.geometry("400x300")
window.title("Joke APP")
window.config(bg='black')
ref_img=tk.PhotoImage(file='refresh-32.png')

top=tk.Frame(window,bg='black')
top.pack(padx=10,pady=5,anchor='center')
f=("poppins",13,"bold")


label=tk.Label(window,font=f)
label.pack(pady=20)

button=tk.Button(window,font=f,text="Refresh",command=anyjoke,image=ref_img,bg='black',borderwidth=0)
button.pack(pady=10,in_=top,side='left')


window.mainloop()