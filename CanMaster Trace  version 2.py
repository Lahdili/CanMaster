from Tkinter import *
from ctypes import *
import ctypes
import time
import signal
import sys
from threading import Thread

def Stop_Mode():
    global Pass_filter
    Pass_filter.set(0)

    
   
def Pass_Mode():
    global Stop_filter
    Stop_filter.set(0)


def Add_Frame_to_Filter():
   pass

def Remove_Frame_from_Filter():
    pass
   
def signal_handler():
    global Stop,root,mydll
    Stop = False
    time.sleep(0.1)
    print "closed"
    mydll.Exit()
    root.destroy()

def Update():
   global root, Stop, text, mydll,Connected, Can_filter, Pass_filter, Liste_frame,liste_id, liste_msg,text
   #Read
   mydll.check_reception_buffer.restype = ctypes.c_char_p
   while (Stop):
       if Connected:
          l = mydll.check_reception_buffer()
          if l[0] !='*':
              #print l
              Frame = l.split(',')
              ID = Frame[2].split(' ')
              Data = Frame[3].split(' ')
              Data = Data[1]
              ID = ID[1].split('=')[1]
              if Can_filter.get() == 1:
                 liste = Liste_frame.get()
                 liste = liste.split(',')
                 if Pass_filter.get() == 1:
                    
                    for i in range (len(liste)):
                       if ID == liste[i]:
                          msg = Frame[1] + " " + ID + " "
                          for i in range (len(Data)/2):
                              msg = msg + Data[2*i]+Data[2*i+1]+ " "
                          msg = msg+ '\n'
                          if OverWrite.get() == 1:
                                exist = False
                                for i in range(len(liste_id)):
                                    if ID == liste_id[i]:
                                       exist = True
                                       liste_msg[liste_id.index(ID)]=msg
                             
                                if exist == False:
                                   liste_id.append(ID)
                                   liste_msg.append(msg)
                         
                                else:
                                      pass
                                text.delete(1.0,END)
  
                                for i in range(len(liste_id)):
                                   if liste_id[i] in liste:
                                       try: 
                                           text.insert(INSERT,liste_msg[i])
                                       except ValueError:
                                           print  'Error'
                          else:
                              text.insert(INSERT,msg)
                                
                 else:
                     Filtred = False
                     for i in range (len(liste)):
                       if ID == liste[i]:
                          Filtred = True
                          if ID in liste_id:
                                liste_msg.remove(liste_msg[liste_id.index(ID)])
                                liste_id.remove(ID)
                     if Filtred == False:
                          msg = Frame[1] + " " + ID + " "
                          for i in range (len(Data)/2):
                              msg = msg + Data[2*i]+Data[2*i+1]+ " "
                          msg = msg+ '\n'
                          
                     if OverWrite.get() == 1 and Filtred == False:
                       exist = False
                       for i in range(len(liste_id)):
                           if ID == liste_id[i]:
                               exist = True
                               liste_msg[liste_id.index(ID)]=msg
                             
                       if exist == False:
                         liste_id.append(ID)
                         liste_msg.append(msg)
                         
                       else:
                          pass
                       text.delete(1.0,END)
  
                       for i in range(len(liste_id)):
                            try: 
                                text.insert(INSERT,liste_msg[i])
                            except ValueError:
                                print  'Error'
                     else:
                        if Filtred == False:
                            text.insert(INSERT,msg)
                                
              else:
                  msg = Frame[1] + " " + ID + " "
                  for i in range (len(Data)/2):
                       msg = msg + Data[2*i]+Data[2*i+1]+ " "
                  msg = msg+ '\n'
                  if OverWrite.get() == 1:
                     exist = False
                     for i in range(len(liste_id)):
                         if ID == liste_id[i]:
                             exist = True
                             liste_msg[liste_id.index(ID)]=msg
                             
                     if exist == False:
                         liste_id.append(ID)
                         liste_msg.append(msg)
                         
                     else:
                          pass
                     text.delete(1.0,END)
  
                     for i in range(len(liste_id)):
                            try: 
                                text.insert(INSERT,liste_msg[i])
                            except ValueError:
                                print  'Error'
                           
                           
                  else:         
                            try: 
                                text.insert(INSERT,msg)
                            except ValueError:
                                print  'Error'
                     

def Status_Control():
    global Connected
    
    if Start_Button['text'] == "Start":
        Start_Button.configure(text="Stop")
        Status_Label.configure(text="  ON  ", bg="green")
        Connected = True
    else:
        Start_Button.configure(text="Start")
        Status_Label.configure(text="  OFF ", bg="red")
        Connected = False

def Connect_App():
    global mydll, thread,Connection_Label,Connect_Button,baudrate_value,entry_Boudrate
    
    #setting
    Connect_Button['state'] = 'disabled'
    entry_Boudrate['state'] = 'disabled'
    channel = 1 #Cancase channel
    BaudRate = int(baudrate_value.get())
    mydll.Start(channel,BaudRate)
    thread.start()    
    Connection_Label.configure(text="  ON  ", bg="green") 

def disply_overwrite():
    pass  
    
#main
#var
Stop =  True
Connected = False

liste_id = []
liste_msg = []

#code
root = Tk()
root.title('CanMaster Trace')#Le titre de l'interface
root.geometry('468x700+0+0')#La dimension de l'interface

label_Frame=Label(root, text="Baudrates:").place(x=2,y=3 )#Label qui donne le Mode d'envoi

baudrate_value = StringVar()
entry_Boudrate=Entry(root, textvariable= baudrate_value )#Un entry pour ecrire l'ID
entry_Boudrate.place( x=65,y=3,width=50)#L'emplacement de L'ID
baudrate_value.set(125000)

Connect_Button = Button(root, text="Connect", command=Connect_App)
Connect_Button.place(x=125,y=3,width=60,height=21)#Boutton Start/Stop

Connection_Label = Label(root, text="  OFF ", bg="red")
Connection_Label.place(x=185,y=3 ,width=34,height=21)#Label Status

Start_Button = Button(root, text="Start", command=Status_Control)
Start_Button.place(x=230,y=3,width=40,height=21)#Boutton Start/Stop

Status_Label = Label(root, text="  OFF ", bg="red")
Status_Label.place(x=270,y=3,width=34,height=21)#Label Status

OverWrite = IntVar()
OverWrite_Activation=Checkbutton(root, variable= OverWrite )#Checkbutton de OverWrite_Activation
OverWrite_Activation.config(text='Overwrite')
OverWrite_Activation.place(x=315,y=3)#L'emplacement de Checkbutton
OverWrite.set(1)

Clear_Button = Button(root, text='Clear', command=lambda: text.delete(1.0,END))
Clear_Button.place(x=400,y=3,width=60,height=21)#Boutton Start/Stop
                
Can_filter = IntVar()
Filter_Activation=Checkbutton(root, variable= Can_filter )#Checkbutton de Filter_Activation
Filter_Activation.config(text='Apply filter')
Filter_Activation.place(x=0,y=30)#L'emplacement de Checkbutton dans labelframe

Pass_filter = IntVar()
Pass=Checkbutton(root, variable= Pass_filter, command=Pass_Mode )#Checkbutton de Pass
Pass.config(text='Pass')
Pass.place(x=90,y=30)#L'emplacement de Checkbutton dans labelframe

Stop_filter = IntVar()
Stop=Checkbutton(root, variable= Stop_filter, command=Stop_Mode )#Checkbutton de Pass
Stop.config(text='Stop')
Stop.place(x=140,y=30)#L'emplacement de Checkbutton dans labelframe


label_Frame=Label(root, text="Trames ID (0x):").place(x=200,y=32)#Label qui donne le Mode d'envoi

Liste_frame=StringVar()
entry_ID=Entry(root,textvariable = Liste_frame)#Un entry pour ecrire l'ID
entry_ID.place(x=282,y=33,width=176)#L'emplacement de L'ID
 
#Button(root, text='ADD', command=Add_Frame_to_Filter).place(x=343,y=33,width=60,height=21)#Boutton pour l'ajout des trames
#gButton(root, text='REMOVE', command=Remove_Frame_from_Filter).place(x=400,y=33,width=60,height=21)#Boutton pour la supprission des trames

scrollbar = Scrollbar(root)
scrollbar.place(x=443,y=58,height=642)

text = Text(root,yscrollcommand=scrollbar.set,width=54,height=40)
text.place(x=3,y=58)

scrollbar.config(command=text.yview)

#Read

# API
mydll = cdll.LoadLibrary('Trace\CanCaseXL_API.dll')
root.protocol("WM_DELETE_WINDOW", signal_handler)
thread = Thread(target=Update)

root.mainloop()

