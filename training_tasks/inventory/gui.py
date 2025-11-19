import tkinter
from app2 import Inventory, Item
inventory = Inventory([])

main = tkinter.Tk()
main.geometry("500x500")

label = tkinter.Label(main, text="FUCK")
label.pack()

inputbox = tkinter.Entry(main)
inputbox.pack(pady=20)

def log(event = None):
    for item in inventory.get_contents():
        textbox.insert(tkinter.END, item.name + "\n")

def createAdd(event = None):
    itemName = inputbox.get()
    itemType = "idk"
    itemDescription = "heh"
    itemCost = 10
    inventory.add_items([Item(itemName, itemType, itemDescription, itemCost)])
    log(itemName)

button = tkinter.Button(main, text="Create and add item", command = createAdd)
button.pack(pady=20)

log_button = tkinter.Button(main, text= "Show item", command = createAdd)
log_button.pack(pady=20)

textbox = tkinter.Text(main, height = 10, width= 20)
textbox.pack(pady=20)

main.mainloop()