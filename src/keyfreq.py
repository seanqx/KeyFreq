import os, json, time, uuid
from threading import Thread

import pynput
from pynput.keyboard import Key, Listener
import psutil, win32process, win32gui 

import tkinter
from tkinter import ttk

import keyUtils as ku


# Time interval for updating the tree view
TREE_UPDATE_INTERVAL_MIL_SECONDS = 1000

# Stores all the key clicked data
keyDict = {}

keyListener = None

#tree root
root = None
treeFrame = None
treeView = None


def json_tree(tree, parent, dictionary):
    '''
    Show dict data on tree 
    '''
    for key in dictionary:
        uid = uuid.uuid4()
        if isinstance(dictionary[key], dict):
            tree.insert(parent, 'end', uid, text=key)
            json_tree(tree, uid, dictionary[key])
        else:
            value = dictionary[key]
            if value is None:
                value = 'None'
            tree.insert(parent, 'end', uid, text=key, value=value)


def buildTree(data):
    # Setup the root UI
    global root
    root = tkinter.Tk()
    root.title("Key Freq Viewer")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Setup the Frames
    # tree_frame = ttk.Frame(root, padding="3")
    global treeFrame
    treeFrame = ttk.Frame(root, padding="3")
    treeFrame.grid(row = 0, column = 0, sticky = tkinter.NSEW)

    # Setup the Tree
    # tree = ttk.Treeview(tree_frame, columns='Values')
    global treeView
    treeView = ttk.Treeview(treeFrame, columns = 'ClickCounter')
    treeView.column('ClickCounter', width=100, anchor='center')
    treeView.heading('ClickCounter', text = 'Click Counter')
    json_tree(treeView, '', data)
    treeView.pack(fill=tkinter.BOTH, expand=1)

    # Limit windows minimum dimensions
    root.update_idletasks()
    root.minsize(800, 800)

    # root.after(1500, startListeningKeys)
    root.after(TREE_UPDATE_INTERVAL_MIL_SECONDS, updateTree)

    root.protocol("WM_DELETE_WINDOW", onTreeClosing)
    root.mainloop()


def onTreeClosing():

    global keyListener
    keyListener.stop()
    # KeyLogThread.is_alive 
    root.destroy()


def updateTree():
    
    global keyDict
    global root
    global treeView

    if not treeView:
        return 
    
    # Delete the whole tree here.
    # TODO: Do it in a bette way.
    for row in treeView.get_children():
        treeView.delete(row)

    json_tree(treeView, '', sortedDict(keyDict))
    treeView.pack(fill = tkinter.BOTH, expand = 2)      

    # Expand all nodes
    # TODO: Only expand manually expanded nodes
    open_children(treeView.focus()) 

    root.after(TREE_UPDATE_INTERVAL_MIL_SECONDS, updateTree)


def open_children(parent):

    treeView.item(parent, open=True)
    for child in treeView.get_children(parent):
        open_children(child)



def ifKeyExist(dict, key): 
      
    if key in dict.keys(): 
        return True
    else: 
        return False


# Get the current actived window(app)'s name
def active_window_process_name():

    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    return (psutil.Process(pid[-1]).name()) 


def getCurrentActiveAppName():
    return active_window_process_name()


def on_press(key):

    global keyDict

    current_window_str = str(getCurrentActiveAppName())
    keyPressedStr = str(ku.translateKey(key))
 
    if ifKeyExist(keyDict, current_window_str):
        if ifKeyExist(keyDict[current_window_str], keyPressedStr):
            keyDict[current_window_str][keyPressedStr] = keyDict[current_window_str][keyPressedStr] + 1
        else:
            keyDict[current_window_str][keyPressedStr] = 1
    else:
        keyDict[current_window_str] = {}
        keyDict[current_window_str][keyPressedStr] = 1
    

def sortedJson(dic):
    keyDictSorted = {key : dict(sorted(val.items(), key = lambda ele: ele[1], reverse=True)) 
       for key, val in dic.items()} 
    keyDictSortedJson = json.dumps(keyDictSorted, indent = 4) 
    return keyDictSortedJson


def sortedDict(dic):
    keyDictSorted = {key : dict(sorted(val.items(), key = lambda ele: ele[1], reverse=True)) 
       for key, val in dic.items()} 
    return keyDictSorted


def startListeningKeys():
    global keyListener
    with Listener(on_press=on_press) as keyListener:
        keyListener.join()


if __name__ == "__main__":

    KeyLogThread = Thread(target = startListeningKeys, args = [] )
    KeyLogThread.start()
    # thread.join()

    buildTree(keyDict)

