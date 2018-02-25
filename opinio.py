# Open file dialog
import tkinter as tk
from tkinter.filedialog import askopenfilename
#import pandas as pd


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    #df = pd.read_csv(csv_file_path)

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)
root.mainloop()

# Open file, read it, and create objects
import csv
csvfile = open('mentions.csv', "r", encoding='utf-8-sig')
reader = csv.reader(csvfile)
mentions_list = list(reader)
print (mentions_list)

# Analyze sentiment of the article or post
import indicoio
indicoio.config.api_key = "API-KEY"

import csv
with open("output.csv","w", newline='') as f:
    writer = csv.writer(f, dialect='excel')

    for row in mentions_list:
        for url in row:
            print(url)
            writer.writerow([url])
            sentiment = indicoio.sentiment_hq("{}".format(url), url=True)
            print ("Sentiment of article is: {}".format(sentiment))
            writer.writerow(["Sentiment of article is: {}".format(sentiment)])

# Save file dialog
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("CSV (Comma delimited) (*.csv)","*.csv"),("all files","*.*")))
print (root.filename)
