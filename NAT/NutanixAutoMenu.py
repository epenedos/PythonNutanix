import tkinter
from NutanixWindowFunctions import winClusterConnect


class MenuBar:
    def __init__(self, window):
        # Create and display the main menu bar
        self.parent=window
        
        menuBar = tkinter.Menu(window)
        #,command=winClusterConnect(window)
        # Create a pull-down menu for file operations
        fileMenu = tkinter.Menu(menuBar, tearoff = False)
        fileMenu.add_command(label = "Connect to Cluster",command = self.mnuConnect)
        fileMenu.add_command(label = "Exit", command = window.destroy)
        menuBar.add_cascade(menu = fileMenu, label = "Cluster")

        # Create a pull-down menu for editing operations
        editMenu = tkinter.Menu(menuBar, tearoff = False)
        editMenu.add_command(label = "Cut")
        editMenu.add_command(label = "Copy")
        editMenu.add_command(label = "Paste")
        editMenu.add_command(label = "Select All")
        editMenu.add_command(label = "Undo")
        editMenu.add_command(label = "Redo")
        menuBar.add_cascade(menu = editMenu, label = "Edit")

        # Create a pull-down menu for help operations
        helpMenu = tkinter.Menu(menuBar, tearoff = False)
        helpMenu.add_command(label = "About")
        menuBar.add_cascade(menu = helpMenu, label = "Help")
        window.config(menu=menuBar)

    def mnuConnect(self):

        dlg = winClusterConnect(self.parent, title = "connect...")
