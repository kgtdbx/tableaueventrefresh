
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:55:42 2020

@author: Manish Chauhan +91-9774083186
"""



import tableauserverclient as TSC
import getpass

print("-------------------------------------------------------------------------")
print("Importing of modules completed")
print("-------------------------------------------------------------------------")
 

# Variable Declaration & Initialization
serv='http://laptop-r8gnfcla'
uname='Your Tableau Username'
pwd='Your Tableau Password'
site=''  # If site is Default then leave it blank else pass the site name AS ('https://mytableau.com/MYSITE')

print("-------------------------------------------------------------------------")
print("Variable Initialization Completed")
print("-------------------------------------------------------------------------")

print("-------------------------------------------------------------------------")
print("Welcome To The Goldstone's Tableau Embedded Credentials Update Application")
print("-------------------------------------------------------------------------")

#Getting username as input for which password has to be updated 
db_uname=input(prompt='Enter the current username for database connection:\n')
new_db_uname=input(prompt='Enter the new username for database connection:\n')
#Getting the new password from user
db_password= getpass.getpass(prompt='Enter new the Password: ')
#creating the Authentication Object:tableau_auth

tableau_auth = TSC.TableauAuth(uname,pwd, site)

# Creating the Server Object:server
server = TSC.Server(serv)

# This will ignore the SSL certificate check (Use this only if tableau server has SSL configured)
server.add_http_options({'verify': False}) 

# Setting Server API version i.e latest as of now
server.version = '3.1'
count=0 
with server.auth.sign_in(tableau_auth):
   print("-------------------------------------------------------------------------")
   print(" Signed In As " + uname)
   print("-------------------------------------------------------------------------")
# Getiing all data sources present on the Tableau server   
   all_datasources,pagination_item=server.datasources.get()

   update_function = server.datasources.update_connection
   
  
# Getting Id's of data sources from Tableau Server.   
   datasource_id=([datasource.id for datasource in all_datasources])
# Looping over all the id's and getting the data
   for i in range(len(datasource_id)):
       resource = server.datasources.get_by_id(datasource_id[i])
##       print(resource)
       server.datasources.populate_connections(resource)
       resource.connections[0].id
       resource.connections[0].username
       connection=resource.connections[0]
       connection.username=new_db_uname
       connection.password=db_password
       connection.embed_password = True
       if(resource.connections[0].username==db_uname):
           datasource_item = server.datasources.get_by_id(datasource_id[i]) 
##        print(datasource_item.id)
           server.datasources.update_connection(resource, connection)
           count=count+1
           
         
           
           
print("-------------------------------------------------------------------------")
print('There are '+ str(count)+' connections for which the credentials has been updated. ')
print("-------------------------------------------------------------------------")           

