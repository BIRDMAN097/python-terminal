#!/usr/bin/env python3
import os
import shutil
print("-"*50)
print("-"*50)
print("WELCOME TO MY MINI TERMINAL! ")
print("ENTER 'exit' TO TERMINATE")
print("-"*50)
print("-"*50)

while True:

         a = input("ENTER A COMMAND : ").strip()

         if a == "ls":
                print(os.listdir())

         elif a == "cd":
                  b =input("ENTER A DIRECTORY : ").strip()
                    
                  try:
                      os.chdir(f'{b}')
                  
                      
                  except FileNotFoundError:
                          
                  
                           print("FILE NOT FOUND\n")
         elif a == "hard":
              
          try:
               b = input("ENTER A FILE NAME :").strip()
               c = input("ENTER THE HARD LINK NAME : ").strip()
               os.link(b,c)
   
          except FileNotFoundError:
                    print("\n FILE NOT FOUND \n")
         elif a == "mkdir":

                     b = input("CREATE A NAME : ").strip()
                     os.mkdir(f'{b}')

         elif a == "pwd":

                       print(os.getcwd())

         elif a == "rm":
             try:
                  b = input("ENTER THE NAME  : ").strip()
                  if os.path.isdir(b):   
                     os.rmdir(b)
                  else:
                      os.remove(b)
                      print(f"REMOVED : {b}")
             except FileNotFoundError:
                  print("\n FILE NOT FOUND \n")
             except OSError:
                  print("\n DIRECTORY NOT EMPTY\n")     

         elif a == "exit" :
                     print("\nGOODBYE!\n")
                     break
         elif a == "rename" :
            try:
                b = input("ENTER THE FILE NAME :").strip()
                c = input("ENTER THE NEW NAME :").strip()
                os.rename(b,c)                       
            except FileNotFoundError:
                        print("\n FILE NOT FOUND \n")    
         elif a == "move":
                try:
                    b = input("ENTER THE FILE NAME :").strip()
                    c = input("ENTER THE TARGET DIRECTORY :").strip()
                    shutil.move(b,c)
                    print(f"MOVED: {b} -> {c}")
                except FileNotFoundError:
                       print("\n FILE NOT FOUND \n")
                      
         elif a == "symbolic" or a == "soft":
                   try:
                        b = input("ENTER THE FILE NAME :").strip()
                        c = input("ENTER THE SYMBOLIC LINK NAME:").strip()                       
                        os.symlink(b,c)
                        print(f"Symlink created {b} -> {c}")
                   except FileExistsError:
                                 print("\n FILE ALREADY EXISTS \n")
                   except PermissionError:
                                 print("\n PERMISSION DENIED \n")
 

         else :
               print("ENTER A VALID COMMAND!\n")
               continue     
