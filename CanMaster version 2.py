from Tkinter import *
import math
import time
from threading import Thread
from ctypes import *
import ctypes
import sys

def Save():
    f = open("Config.ini", "w")
    for i in range (len(liste_entry_nom_ID)):
        f.write(liste_entry_nom_ID[i]+ " ") # frame name
        f.write(liste_entry_ID[i]+ " ") # frame ID
        f.write(str(liste_varCheckbutton1[i].get())+ " ") # event mode 
        f.write(str(liste_varCheckbutton2[i].get())+ " ") # periodic mode
        f.write(str(liste_entry_periode[i].get())+ " ") # period
        f.write(str(liste_data1[i].get())+ " ") # data
        f.write(str(liste_data2[i].get())+ " ") # data
        f.write(str(liste_data3[i].get())+ " ") # data
        f.write(str(liste_data4[i].get())+ " ") # data
        f.write(str(liste_data5[i].get())+ " ") # data
        f.write(str(liste_data6[i].get())+ " ") # data
        f.write(str(liste_data7[i].get())+ " ") # data
        f.write(str(liste_data8[i].get())+ " \n") # data
    f.close()

def load():
    f = open("Config.ini", "r")
    line = f.readline()
    while line: 
       msg = line.split(" ")
       if len(msg) >= 12:
           EnregistrementInfosLoad(msg[0], msg[1], msg[2] , msg[3], msg[4], msg[5],msg[6],msg[7],msg[8],msg[9],msg[10],msg[11],msg[12])
       line = f.readline()

    f.close()
    
def signal_handler():
    global Stop,root,mydll
    Stop = False
    time.sleep(0.1)
    print "closed"
    mydll.Exit()
    Save()
    interface.destroy()

def RemoveTrame(): #Commande RemoveTrame() permet de supprimer des trames de donnees
   
 global suppression_ID
    
 Removefenetre=Toplevel(interface) # Ssfenetre est une sous fenetre de interface
 Removefenetre.geometry("260x60+300+300") #Dimension de la sous fenetre
 Removefenetre.title("Suppression des Trames") #Titre de la sous fenetre
    
 label_nom_ID=Label(Removefenetre,text="ID (s) à supprimer (0x):").place(x=1,y=5)#Label qui donne le nom de L'ID
 suppression_ID=Entry(Removefenetre)# Un entry pour ecrire le nom de l'ID
    
 Button(Removefenetre,text="Supprimer" , command=Suppression).place(x=120,y=30)#Button pour supprission des informations dans labelframe
    
 suppression_ID.place(x=130,y=5)#L'emplacement de nom de L'ID

def Suppression():
     global suppression_ID, liste_entry_ID
    
     id_list =suppression_ID.get().split(',')
     for i in liste_entry_ID:
         if i in id_list:
             liste_entry_nom_ID.remove(liste_entry_nom_ID[liste_entry_ID.index(i)])
             liste_varCheckbutton1.remove(liste_varCheckbutton1[liste_entry_ID.index(i)])
             liste_varCheckbutton2.remove(liste_varCheckbutton2[liste_entry_ID.index(i)])
             liste_entry_periode.remove(liste_entry_periode[liste_entry_ID.index(i)])
             liste_data1.remove(liste_data1[liste_entry_ID.index(i)])
             liste_data2.remove(liste_data2[liste_entry_ID.index(i)])
             liste_data3.remove(liste_data3[liste_entry_ID.index(i)])
             liste_data4.remove(liste_data4[liste_entry_ID.index(i)])
             liste_data5.remove(liste_data5[liste_entry_ID.index(i)])
             liste_data6.remove(liste_data6[liste_entry_ID.index(i)])
             liste_data7.remove(liste_data7[liste_entry_ID.index(i)])
             liste_data8.remove(liste_data8[liste_entry_ID.index(i)])
             liste_entry_ID.remove(i)
     signal_handler()

def AjoutTrame(): #Commande AjoutTrame() permet d'ajouter des trames de donnees
    
 global ssfenetre,entry_nom_ID,entry_ID
     
 ssfenetre=Toplevel(interface) # Ssfenetre est une sous fenetre de interface
 ssfenetre.geometry("250x90+300+300") #Dimension de la sous fenetre
 ssfenetre.title("Insertion des Trames") #Titre de la sous fenetre
     
 label_nom_ID=Label(ssfenetre,text="Nom de l'ID:").place(x=1,y=5)#Label qui donne le nom de L'ID
 entry_nom_ID=Entry(ssfenetre)# Un entry pour ecrire le nom de l'ID
     
 label_ID=Label(ssfenetre,text=" l'ID (0x):").place(x=1,y=30)#Label qui donne l'ID
 entry_ID=Entry(ssfenetre)#Un entry pour ecrire l'ID
     
 Button(ssfenetre,text="Enregistrer les informations" , command=EnregistrementInfos).place(x=75,y=55)#Button pour enregistrer les informations dans labelframe
     
 entry_nom_ID.place(x=90,y=5)#L'emplacement de nom de L'ID 
 entry_ID.place(x=90,y=30)#L'emplacement de L'ID


     
def EnregistrementInfos(): #Commande EnregistrementInfos() permet d'afficher l'ID , son nom ,le mode d'envoi et la data
    
 global ssfentre,PositionVerticaleDulabelframe,Indice,liste_entry_nom_ID,liste_entry_periode,liste_varCheckbutton1,liste_varCheckbutton2

 liste_entry_nom_ID.append(entry_nom_ID.get()) #Sauvegarder le nom de l'ID et l'ajouter dans une liste contenantles noms des ID
 liste_entry_ID.append(entry_ID.get()) #Sauvegarder l'ID et l'ajouter dans une liste contenant les ID
      
 labelframe=LabelFrame(interface,text="  "+liste_entry_nom_ID[Indice]+"("+liste_entry_ID[Indice]+")"+":"+"  ",width=440,height=100,relief='ridge',borderwidth=4)#Un labelframe a titre de nom del'ID plus L'ID et enregistre la data de trame et le mode d'envoi
 labelframe.place(x=2,y=PositionVerticaleDulabelframe)#L'emplacement de labelframe dans interface et l'incrementation par PositionVerticaleDulabelframe a chaque fois qu'on veut ajouter une labelframe 
      
 label=Label(labelframe, text="Mode d'envoi:").place(x=0,y=2)#Label qui donne le Mode d'envoi
      
 liste_varCheckbutton1.append(IntVar())#Creation d'une liste pour ajouter les variables de checkbutton1
 liste_varCheckbutton2.append(IntVar())#Creation d'une liste pour ajouter les variables de checkbutton2
 liste_varCheckbutton2[Indice].set(1)#Cochage par defaut le checkbutton2

 label_periode=Label(labelframe, text="Période(ms):").place(x=270,y=2)#Label qui donne le Mode d'envoi
      
 liste_entry_periode.append(Entry(labelframe, width=10))#Creation d'une liste pour ajouter la periode d'envoi
 liste_entry_periode[Indice].insert(END,'1000')#Donner par defaut la valeur 1000 ms pour la periode d'envoi
 liste_entry_periode[Indice].place(x=350, y=0)#L'emplacement de l'entry periode dans labelframe
   
 Checkbutton1=Checkbutton(labelframe, variable=liste_varCheckbutton1[Indice])#Checkbutton1 de variable liste_varCheckbutton1[Indice]
 Checkbutton1.place(x=180,y=0)#L'emplacement de Checkbutton1 dans labelframe
 Checkbutton1.config(text='periodique')#Checkbutton1 de text periodique
      
 Checkbutton2=Checkbutton(labelframe, variable=liste_varCheckbutton2[Indice])#Checkbutton2 de variable liste_varCheckbutton2[Indice]
 Checkbutton2.place(x=80,y=0)#L'emplacement de Checkbutton2 dans labelframe
 Checkbutton2.config(text='evenementiel')#Checkbutton2 de text evenementiel
              
 Button(labelframe,text='Send',command=lambda  i=Indice:EnvoiEvenementiel(i)).place(x=380,y=40)#Button de command EcritureDeDonnees d'indice Indice
      
 label_DATA=Label(labelframe,text ="DATA(0x):").place(x=0,y=40)#Un label qui donne la DATA
 liste_data1.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data1
 liste_data2.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data2
 liste_data3.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data3
 liste_data4.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data4
 liste_data5.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data5
 liste_data6.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data6
 liste_data7.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data7
 liste_data8.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data8
 liste_data1[Indice].insert(END,'00')#Insertion par defaut 00 dans la data1
 liste_data2[Indice].insert(END,'00')#Insertion par defaut 00 dans la data2
 liste_data3[Indice].insert(END,'00')#Insertion par defaut 00 dans la data3
 liste_data4[Indice].insert(END,'00')#Insertion par defaut 00 dans la data4
 liste_data5[Indice].insert(END,'00')#Insertion par defaut 00 dans la data5
 liste_data6[Indice].insert(END,'00')#Insertion par defaut 00 dans la data6
 liste_data7[Indice].insert(END,'00')#Insertion par defaut 00 dans la data7
 liste_data8[Indice].insert(END,'00')#Insertion par defaut 00 dans la data8
 liste_data1[Indice].place(x=60,y=40)#L'emplacement de la data1 dans labelframe
 liste_data2[Indice].place(x=100,y=40)#L'emplacement de la data2 dans labelframe
 liste_data3[Indice].place(x=140,y=40)#L'emplacement de la data3 dans labelframe
 liste_data4[Indice].place(x=180,y=40)#L'emplacement de la data4 dans labelframe
 liste_data5[Indice].place(x=220,y=40)#L'emplacement de la data5 dans labelframe
 liste_data6[Indice].place(x=260,y=40)#L'emplacement de la data6 dans labelframe
 liste_data7[Indice].place(x=300,y=40)#L'emplacement de la data7 dans labelframe
 liste_data8[Indice].place(x=340,y=40)#L'emplacement de la data8 dans labelframe

 PositionVerticaleDulabelframe +=100#Incrementation de la position verticale de labelframe par 100
 Indice += 1#Incrementation de l'indice par 1
 ssfenetre.destroy()#Fermeture de la sous fenetre

def EnregistrementInfosLoad(Nom_ID, ID, IntVar_P , IntVar_F, Period, Data1,Data2,Data3,Data4,Data5,Data6,Data7,Data8): #Commande EnregistrementInfos() permet d'afficher l'ID , son nom ,le mode d'envoi et la data
    
 global PositionVerticaleDulabelframe,Indice,liste_entry_nom_ID,liste_entry_periode,liste_varCheckbutton1,liste_varCheckbutton2

 liste_entry_nom_ID.append(Nom_ID) #Sauvegarder le nom de l'ID et l'ajouter dans une liste contenantles noms des ID
 liste_entry_ID.append(ID) #Sauvegarder l'ID et l'ajouter dans une liste contenant les ID
      
 labelframe=LabelFrame(interface,text="  "+Nom_ID+"("+ID+")"+":"+"  ",width=440,height=100,relief='ridge',borderwidth=4)#Un labelframe a titre de nom del'ID plus L'ID et enregistre la data de trame et le mode d'envoi
 labelframe.place(x=2,y=PositionVerticaleDulabelframe)#L'emplacement de labelframe dans interface et l'incrementation par PositionVerticaleDulabelframe a chaque fois qu'on veut ajouter une labelframe 
      
 label=Label(labelframe, text="Mode d'envoi:").place(x=0,y=2)#Label qui donne le Mode d'envoi
      
 liste_varCheckbutton1.append(IntVar())#Creation d'une liste pour ajouter les variables de checkbutton1
 liste_varCheckbutton1[Indice].set(int(IntVar_P))#Cochage par defaut le checkbutton1
 liste_varCheckbutton2.append(IntVar())#Creation d'une liste pour ajouter les variables de checkbutton2
 liste_varCheckbutton2[Indice].set(int(IntVar_F))#Cochage par defaut le checkbutton2

 label_periode=Label(labelframe, text="Période(ms):").place(x=270,y=2)#Label qui donne le Mode d'envoi
      
 liste_entry_periode.append(Entry(labelframe, width=10))#Creation d'une liste pour ajouter la periode d'envoi
 liste_entry_periode[Indice].insert(END,Period)#Donner par defaut la valeur 1000 ms pour la periode d'envoi
 liste_entry_periode[Indice].place(x=350, y=0)#L'emplacement de l'entry periode dans labelframe
   
 Checkbutton1=Checkbutton(labelframe, variable=liste_varCheckbutton1[Indice])#Checkbutton1 de variable liste_varCheckbutton1[Indice]
 Checkbutton1.place(x=180,y=0)#L'emplacement de Checkbutton1 dans labelframe
 Checkbutton1.config(text='periodique')#Checkbutton1 de text periodique
      
 Checkbutton2=Checkbutton(labelframe, variable=liste_varCheckbutton2[Indice])#Checkbutton2 de variable liste_varCheckbutton2[Indice]
 Checkbutton2.place(x=80,y=0)#L'emplacement de Checkbutton2 dans labelframe
 Checkbutton2.config(text='evenementiel')#Checkbutton2 de text evenementiel
              
 Button(labelframe,text='Send',command=lambda  i=Indice:EnvoiEvenementiel(i)).place(x=380,y=40)#Button de command EcritureDeDonnees d'indice Indice
      
 label_DATA=Label(labelframe,text ="DATA(0x):").place(x=0,y=40)#Un label qui donne la DATA
 liste_data1.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data1
 liste_data2.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data2
 liste_data3.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data3
 liste_data4.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data4
 liste_data5.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data5
 liste_data6.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data6
 liste_data7.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data7
 liste_data8.append(Entry(labelframe,width=5))#Creation une liste pour ajouter la data8
 liste_data1[Indice].insert(END,Data1)#Insertion par defaut 00 dans la data1
 liste_data2[Indice].insert(END,Data2)#Insertion par defaut 00 dans la data2
 liste_data3[Indice].insert(END,Data3)#Insertion par defaut 00 dans la data3
 liste_data4[Indice].insert(END,Data4)#Insertion par defaut 00 dans la data4
 liste_data5[Indice].insert(END,Data5)#Insertion par defaut 00 dans la data5
 liste_data6[Indice].insert(END,Data6)#Insertion par defaut 00 dans la data6
 liste_data7[Indice].insert(END,Data7)#Insertion par defaut 00 dans la data7
 liste_data8[Indice].insert(END,Data8)#Insertion par defaut 00 dans la data8
 liste_data1[Indice].place(x=60,y=40)#L'emplacement de la data1 dans labelframe
 liste_data2[Indice].place(x=100,y=40)#L'emplacement de la data2 dans labelframe
 liste_data3[Indice].place(x=140,y=40)#L'emplacement de la data3 dans labelframe
 liste_data4[Indice].place(x=180,y=40)#L'emplacement de la data4 dans labelframe
 liste_data5[Indice].place(x=220,y=40)#L'emplacement de la data5 dans labelframe
 liste_data6[Indice].place(x=260,y=40)#L'emplacement de la data6 dans labelframe
 liste_data7[Indice].place(x=300,y=40)#L'emplacement de la data7 dans labelframe
 liste_data8[Indice].place(x=340,y=40)#L'emplacement de la data8 dans labelframe

 PositionVerticaleDulabelframe +=100#Incrementation de la position verticale de labelframe par 100
 Indice += 1#Incrementation de l'indice par 1
 

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def RepresentsHex(s):
    try: 
        int(s, 16)
        return True
    except ValueError:
        return False
def myHex(s):
        
    return int(s, 16)
 
def EnvoiPeriodique():#Commande pour ecrire l'ID et la data

    delai = 10 # 10ms
    compteur = 0
    periode = 1
    while (len(liste_entry_ID)==0):
           pass
    #print range(len(liste_entry_ID))
    time.sleep(1)
    while(Stop):

      for i in range(len(liste_entry_ID)):
        if liste_varCheckbutton1[i].get() == 1:
           #print liste_entry_ID[i] 
           periode=liste_entry_periode[i].get()
           if RepresentsInt(periode): 
               periode= int(liste_entry_periode[i].get())
           else:
                print "The period of frame ID: "+liste_entry_ID[i]+" is invalid"
                continue   
           if ((delai * compteur) % periode == 0):
             if RepresentsHex(liste_entry_ID[i]) and RepresentsHex(liste_data1[i].get()) and RepresentsHex(liste_data2[i].get()) and RepresentsHex(liste_data3[i].get()) and RepresentsHex(liste_data4[i].get()) and RepresentsHex(liste_data5[i].get()) and RepresentsHex(liste_data6[i].get()) and RepresentsHex(liste_data7[i].get()) and RepresentsHex(liste_data8[i].get()):
                 
                 #print "*"+liste_entry_ID[i]+":"+liste_data1[i].get()+liste_data2[i].get()+liste_data3[i].get()+liste_data4[i].get()+liste_data5[i].get()+liste_data6[i].get()+liste_data7[i].get()+liste_data8[i].get()+"#" 
                 
                 mydll.Send(myHex(liste_entry_ID[i]),myHex(liste_data1[i].get()),myHex(liste_data2[i].get()),myHex(liste_data3[i].get()),myHex(liste_data4[i].get()),myHex(liste_data5[i].get()),myHex(liste_data6[i].get()),myHex(liste_data7[i].get()),myHex(liste_data8[i].get()))
                 
             else:
                 print "The ID or Data of frame ID: "+liste_entry_ID[i]+" is invalid"
      time.sleep(0.01) # sleep for 10ms
      compteur += 1
      
      
      if (compteur == 100):
          compteur =0
          
def EnvoiEvenementiel(i):

    if liste_varCheckbutton2[i].get() == 1:
        #print "*"+liste_entry_ID[i]+":"+liste_data1[i].get()+liste_data2[i].get()+liste_data3[i].get()+liste_data4[i].get()+liste_data5[i].get()+liste_data6[i].get()+liste_data7[i].get()+liste_data8[i].get()+"#"
        mydll.Send(myHex(liste_entry_ID[i]),myHex(liste_data1[i].get()),myHex(liste_data2[i].get()),myHex(liste_data3[i].get()),myHex(liste_data4[i].get()),myHex(liste_data5[i].get()),myHex(liste_data6[i].get()),myHex(liste_data7[i].get()),myHex(liste_data8[i].get()))
                 
def Connect_App():
    global mydll, thread,Connection_Label,Connect_Button,baudrate_value,entry_Boudrate
    
    #setting
    Connect_Button['state'] = 'disabled'
    entry_Boudrate['state'] = 'disabled'
    entry_channel['state'] = 'disabled'
    channel = int(Channel_value.get())#Cancase channel
    BaudRate = int(baudrate_value.get())
    mydll.Start(channel,BaudRate)
    thread.start()    
    Connection_Label.configure(text="  ON  ", bg="green") 

    
#Main programme principale
        
global liste_entry_ID, liste_data1,liste_data2,liste_data3,liste_data4,liste_data5,liste_data6,liste_data7,liste_data8,i,Indice


PositionVerticaleDulabelframe=50 #Initialisation de la position verticale de labelframe
Indice= 0 #Initialisation de l'indice  
                    
liste_entry_nom_ID=[]#Initialisation de la liste de nom des ID
liste_entry_ID=[]#Initialisation de la liste des ID
liste_entry_periode=[]#Initialisation de la liste des periodes
liste_data1=[]#Initialisation de la liste de la data1
liste_data2=[]#Initialisation de la liste de la data2
liste_data3=[]#Initialisation de la liste de la data3
liste_data4=[]#Initialisation de la liste de la data4
liste_data5=[]#Initialisation de la liste de la data5
liste_data6=[]#Initialisation de la liste de la data6
liste_data7=[]#Initialisation de la liste de la data7
liste_data8=[]#Initialisation de la liste de la data8
liste_varCheckbutton1=[]#Initialisation de la liste des variables de Checkbutton1
liste_varCheckbutton2=[]#Initialisation de la liste des variables de Checkbutton2



Stop =  True

interface = Tk()
interface.title('CanMaster')#Le titre de l'interface
interface.geometry('446x655+0+0')#La dimension de l'interface

Setting_labelframe=LabelFrame(interface,text=" Setting ",borderwidth=4)#Un labelframe
Setting_labelframe.place(x=2,y=0,width=441,height=50)#L'emplacement de labelframe dans interface et l'incrementation par PositionVerticaleDulabelframe a chaque fois qu'on veut ajouter une labelframe 

baudrate_label=Label(Setting_labelframe, text="Baudrates:").place(x=2,y=0 )#Label qui donne le Mode d'envoi

baudrate_value = StringVar()
entry_Boudrate=Entry(Setting_labelframe, textvariable= baudrate_value )#Un entry pour ecrire l'ID
entry_Boudrate.place( x=65,y=0,width=50)#L'emplacement de L'ID
baudrate_value.set(125000)

Channel_label=Label(Setting_labelframe, text="Channel:").place(x=120,y=0 )#Label qui donne le Mode d'envoi

Channel_value = StringVar()
entry_channel=Entry(Setting_labelframe, textvariable= Channel_value )#Un entry pour ecrire l'ID
entry_channel.place( x=180,y=0,width=20)#L'emplacement de L'ID
Channel_value.set(1)

Connect_Button = Button(Setting_labelframe, text="Connect", command=Connect_App)
Connect_Button.place(x=210,y=0,width=60,height=21)#Boutton Start/Stop

Connection_Label = Label(Setting_labelframe, text="  OFF ", bg="red")
Connection_Label.place(x=270,y=0 ,width=38,height=21)#Label Status

Button(Setting_labelframe, text='ADD', command=AjoutTrame).place(x=314,y=0,width=53,height=21)#Boutton pour l'ajout des trames de donnes

Button(Setting_labelframe, text='REMOVE', command=RemoveTrame).place(x=370,y=0,width=55,height=21)#Boutton pour l'ajout des trames de donnes


# API
interface.protocol("WM_DELETE_WINDOW", signal_handler)
mydll = cdll.LoadLibrary('CanCaseXL_API.dll')
thread = Thread(target=EnvoiPeriodique)
load()
interface.mainloop()
     
