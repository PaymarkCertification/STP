'''
Created on 6/01/2020

@author: Michael.Yu
'''
import win32com.client
Outlook = win32com.client.Dispatch("Outlook.Application")
 
# get the Namespace / Session object
namespace = Outlook.Session
 
# get Inbox Folders' name
inboxfolder = namespace.Folders.Folders('Inbox')
 
# get messages on Inbox folder
messages = inboxfolder.Items
 
# get message contents
for message in messages:
    sender = message.Sender
    receiver = message.To
    cc = message.Cc
    subject = message.Subject
    body = message.Body