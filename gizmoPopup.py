import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox
import configparser
import os

numRows = 4
dropdownValues = ["Forward", "Backward", "Stop", "make an noise", "slow down"] 


def on_combobox_select(event, combobox_var):
    # this method will help us select values from a dropdown
    selected_value = combobox_var.get()



def createDropdowns(configure_window):
    # create labels to be displayed on the popup
    createLabels(configure_window=configure_window)
    # initialize the number of rows and the values for dropdowns
    
    # create empty arrays to store dropdown variables and option selected by users
    comboboxVars = []
    comboboxes = []

# iterate the loop up to the value above numRows to include the value
    for i in range(1, numRows + 1):
        # stores all the dropdwon values
        var = tk.StringVar(configure_window)
        #print(var)
        combobox = ttk.Combobox(configure_window, textvariable=var, values=dropdownValues)
        combobox.set(f"Select an option")
        combobox.grid(row=i, column=2, padx=10, pady=10)
        combobox.bind(f"<<ComboboxSelected>>", lambda event, index=i: on_combobox_select(event, comboboxVars[index - 1]))

        comboboxVars.append(var)
        comboboxes.append(combobox)
        
    # create inner function for dropdowns by providing access to variables for comboboxes
    def readValuesFromADropdown():
        # initialize the variables to store the action done by patient and whether they are looking the gizmo
        # 1 <- patient is performing an action or looking at gizmo
        # 0 <- patient is not performing an action or looking at gizmo
        actionPerformedByPatient = ["0", "0", "1", "1"]
        patientLookingAtGizmo = ["0", "1", "0", "1"]


        



        

        for i, var in enumerate(comboboxVars):
            # retrieve the option being selected
            selected_value = var.get()
            

            # Write to config file
            config = configparser.ConfigParser()
            config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configFile.ini')
            config.read(config_file_path)
            # merge all the variables into one line and writing to config file
            combinedValues = f"{actionPerformedByPatient[i]}   {patientLookingAtGizmo[i]}   {selected_value}"
            config["DEFAULT"][f"combinedValues{i}"] = combinedValues

            # open the config file
            with open(config_file_path, "w") as config_file:
                config.write(config_file)

    # create a button to write the values to config file        
    read_button = ttk.Button(configure_window, text="Save to File", command=readValuesFromADropdown)
    # position the grid in the dropdown
    read_button.grid(row = 5, column = 5, padx = 10, pady = 10)


            

            
            


   
    
def createLabels(configure_window):
    # initialize variable to write these labels in the popup
    labelText = [["action", "face", "gizmo action"],
                 ["0", "0"],
                 ["0", "1"],
                 ["1", "0"],
                 ["1", "1"]]
    
    for i, row in enumerate(labelText):
        for j, text in enumerate(row):
            # get the label and position it in the popup
            label = tk.Label(configure_window, text=text)
            label.grid(row=i, column=j, padx=10, pady=10)

    
    
   

    


    #dropdownLabels(configure_window, rows =6, columns = 3)
    '''
    labelText = ["action", "face", "gizmo acction"]
    for i, text in enumerate(labelText):
        label = tk.Label(configure_window, text = text)
        label.grid(row =0, column = i, padx = 10, pady = 10)
    
    labelTextRow2 = ["0", "0"]
    for i, text in enumerate(labelTextRow2):
        label = tk.Label(configure_window, text = text)
        label.grid(row =1, column = i, padx = 10, pady = 10)
    
    labelTextRow3 = ["0", "1"]
    for i, text in enumerate(labelTextRow3):
        label = tk.Label(configure_window, text = text)
        label.grid(row =2, column = i, padx = 10, pady = 10)
    
    labelTextRow4 = ["1", "0"]
    for i, text in enumerate(labelTextRow4):
        label = tk.Label(configure_window, text = text)
        label.grid(row =3, column = i, padx = 10, pady = 10)
    
    labelTextRow4 = ["1", "1"]
    for i, text in enumerate(labelTextRow4):
        label = tk.Label(configure_window, text = text)
        label.grid(row =4, column = i, padx = 10, pady = 10)

   
    combobox_var = tk.StringVar(configure_window)
    combobox = ttk.Combobox(configure_window, textvariable=combobox_var, values=["Forward", "Backward", "Stop"])
    combobox.set("Select an option")
    combobox.grid(row=1, column=2, padx=10, pady=10)
    combobox.bind("Dropdown", lambda event: on_combobox_select(event, combobox_var))

    combobox_var2 = tk.StringVar(configure_window)
    combobox2 = ttk.Combobox(configure_window, textvariable=combobox_var2, values=["Forward", "Backward", "Stop"])
    combobox2.set("Select an option")
    combobox2.grid(row=2, column=2, padx=10, pady=10)
    combobox2.bind("Dropdown2", lambda event: on_combobox_select(event, combobox_var2))

    combobox_var3 = tk.StringVar(configure_window)
    combobox3 = ttk.Combobox(configure_window, textvariable=combobox_var3, values=["Forward", "Backward", "Stop"])
    combobox3.set("Select an option")
    combobox3.grid(row=3, column=2, padx=10, pady=10)
    combobox3.bind("Dropdown3", lambda event: on_combobox_select(event, combobox_var3))

    combobox_var4 = tk.StringVar(configure_window)
    combobox4 = ttk.Combobox(configure_window, textvariable=combobox_var4, values=["Forward", "Backward", "Stop"])
    combobox4.set("Select an opticron")
    combobox4.grid(row=4, column=2, padx=10, pady=10)
    combobox4.bind("Dropdown4", lambda event: on_combobox_select(event, combobox_var4))'''




 

def open_configure_window():
    # initialize values for configure window
    configure_window = tk.Toplevel(root)
    configure_window.title("Configure Gizmo Decision Tree")
    configure_window.geometry('400x300')
    # call dropdown method to create labels and dropdowns
    createDropdowns(configure_window=configure_window)

  


   
    


       



    # Create labels and place them in the top row
    #label1 = tk.Label(configure_window, text="action")
    #label1.grid(row=0, column=0, padx=10, pady=10)

    #label2 = tk.Label(configure_window, text="face")
    #label2.grid(row=0, column=1, padx=10, pady=10)

    #label3 = tk.Label(configure_window, text="gizmo action")
    #label3.grid(row=0, column=2, padx=10, pady=10)

    #label4 = tk.Label(configure_window, text="0")
    #label4.grid(row=1, column=0, padx=10, pady=10)

    #label5= tk.Label(configure_window, text="0")
    #label5.grid(row=1, column=1, padx=10, pady=10)

    #label6= tk.Label(configure_window, text="0")
    #label6.grid(row=2, column=0, padx=10, pady=10)

    #label6= tk.Label(configure_window, text="1")
    #label6.grid(row=2, column=1, padx=10, pady=10)

    #label7= tk.Label(configure_window, text="1")
    #label7.grid(row=3, column=0, padx=10, pady=10)

    #label8= tk.Label(configure_window, text="1")
    #label8.grid(row=3, column=1, padx=10, pady=10)

    #label9= tk.Label(configure_window, text="1")
    #label9.grid(row=4, column=0, padx=10, pady=10)

    #label10= tk.Label(configure_window, text="0")
    #label10.grid(row=4, column=1, padx=10, pady=10)
    
  

   
 
   
   
if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    root.geometry('200x200')
    root.title("Gizmo UI")

    menu = Menu(root)
    item = Menu(menu)
    # the 
    item.add_command(label='Configure Gizmo Decision Tree', command= open_configure_window)
    menu.add_cascade(label='Settings', menu=item)

    root.config(menu=menu)
    root.mainloop()
    

    # Create a button to trigger the configure window
    #configure_button = tk.Button(root, text="Open Configure Window", command=open_configure_window)
    #configure_button.pack(pady=20)
    
    
    # Run the Tkinter event loop
   



    