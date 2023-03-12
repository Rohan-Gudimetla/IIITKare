from __future__  import print_function
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from login import login_window
from loginsignup import ls_window
from signup import signup_window
from reg_comp import complaint_window
from dashboard import dashboard_window
from choose_comp import choosecomp_window
from status import status_window
from kivy.core.window import Window
import pyrebase, os, re
from getpass import getpass
from logging import Logger
import requests, json
from kivy.storage.jsonstore import JsonStore
import firebase_admin
from firebase_admin import credentials, firestore
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import os
from email.mime.text import MIMEText
# import jwt #used for obtaining the UID from the IDtoken obtained on printing user.
firebaseConfig = {
  'apiKey': "AIzaSyAldG5tlW1XUKA4i1lN1w4aGlVpvfafkPc",
  'authDomain': "iiitkare.firebaseapp.com",
  'projectId': "iiitkare",
  'storageBucket': "iiitkare.appspot.com",
  'messagingSenderId': "969158176625",
  'appId': "1:969158176625:web:434af2cb546a29c81310d0",
  'measurementId': "G-D1SR81CSKD",
  'databaseURL' : "https://iiitkare.firebaseio.com"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#connections for firestore database established through db.
data = os.path.abspath(os.path.dirname(__file__)) + "\iiitkare-firebase-adminsdk-x9gan-e8549b7d44.json"
cred = credentials.Certificate(data)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
#kv = Builder.load_file('app.kv')

class WindowManager(ScreenManager):
    pass

class main(MDApp):

    def __init__(self, **kwargs):
        super(main, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)


    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(ls_window(name="ls"))
        self.sm.add_widget(login_window(name="login"))
        self.sm.add_widget(signup_window(name="signup"))
        self.sm.add_widget(dashboard_window(name="dashboard"))
        self.sm.add_widget(status_window(name="status"))
        self.sm.add_widget(choosecomp_window(name="choosecomp"))
        self.sm.add_widget(complaint_window(name="complaint"))


        store = JsonStore('data.json')
        if(store.keys()):
            with open('data.json', "r") as file:
                data = json.load(file)
            username = data['username']['uname']
            self.sm.get_screen('dashboard').ids.welcomename.text += username
            self.sm.get_screen('dashboard').ids.nocomp.text = data['comp']['no']
            self.sm.get_screen('dashboard').ids.nosol.text = data['comp']['sol']
            self.sm.current = "dashboard"
        else:
           
            self.sm.current = "ls"
        return self.sm


    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if self.sm.current == "ls" or self.sm.current == "dashboard":
                return False  # exit the app from this page
            elif self.sm.current == "login" or self.sm.current=="signup":
                self.sm.transition.direction = "right"
                self.sm.current = "ls"
                
                self.sm.get_screen("ls").ids.signup.md_bg_color = get_color_from_hex("133261")
                self.sm.get_screen("ls").ids.login.md_bg_color = get_color_from_hex("133261")
                return True  # do not exit the app
            elif self.sm.current == "choosecomp" or self.sm.current == "status":
                self.sm.transition.direction = "right"
                self.sm.current = "dashboard"
                return True
            
            elif self.sm.current == 'complaint':
                self.sm.transition.direction = 'right'
                self.sm.current = 'choosecomp'
                return True  # do not exit the app
    



    def newUser(self):

        email = self.sm.get_screen("signup").ids.mail.text
        # self.sm.get_screen("signup").ids.mail.opacity = 0
        password = (self.sm.get_screen("signup").ids.passw.text)
        
        # self.sm.get_screen("signup").ids.passw.opacity = 0
        try:
            
            user = auth.create_user_with_email_and_password(email, password)    #user is the web token
            uid = user['localId']
            print("Success...")
            auth.send_email_verification(user['idToken'])
            doc_ref = db.collection(u'users').document(email)
            doc_ref.set({
                'email': email, 
                 
                'name': self.sm.get_screen("signup").ids.uname.text
                #'complaint': {'threadId': "", 'status': ""}

                })
            # print(user['localId'])  #this prints the UID of the user.
            self.sm.transition.direction = "left"
            self.sm.current = "login"

    
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            print(error['message'])        


        # self.sm.current = "login"
        # print(email)

    def userLogin(self):
        email = self.sm.get_screen("login").ids.mail.text
        password = (self.sm.get_screen("login").ids.passw.text)
        
# #user login
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            email_verify = auth.get_account_info(login['idToken'])['users'][0]['emailVerified']
            if(email_verify):
                store = JsonStore('data.json')
                store.put('usermail', emailid=email)
                print("login successful!")
                store = JsonStore('data.json')
                store.put('details', email=email)
                #temporarily disabled
                doc_ref = db.collection(u'users').document(email)  
                doc_ref.update({'uid': login['localId']})
                doc = doc_ref.get()
                doc_dict = doc.to_dict()
                nameuser = doc_dict['name']
                store.put('username', uname = nameuser)
                store.put('comp', no='00', sol= '00')
                # store.put('comp', sol='00')
                self.sm.get_screen('dashboard').ids.welcomename.text += nameuser
                self.sm.transition.direction = "left"
                self.sm.current="dashboard"
            else:
                print("Please verify your email!!!")
    # print(login)
        except:
            print("error")        

    def signOut(self):
        store = JsonStore('data.json')
        store.clear()
        auth.current_user= None
        self.sm.current = "ls"

    def sendComp(self):
        subje = self.sm.get_screen("complaint").ids.subj.text
        messg = self.sm.get_screen("complaint").ids.msg.text
        SCOPES = ['https://mail.google.com/']
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'key.json', SCOPES)
                creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json()) 

        try:
            with open('data.json', "r") as file:
                data = json.load(file)
            emailidact = data['details']['email']
            subje = subje + ': ' + emailidact
            service = build('gmail', 'v1', credentials=creds)
            message = MIMEText(messg)
            message['To'] = 'rohan.gudimetla07@gmail.com'
            message['From'] = 'services.iiitkare@gmail.com'
            message['Subject'] = subje
        # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf8')

            print(encoded_message)
            create_message = {'raw': encoded_message}
        # pylint: disable=E1101
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["threadId"]}')

            doc_ref = db.collection(u'users').document(emailidact)
            doc_ref.update({'complaints': send_message["threadId"]})
            store = JsonStore('data.json')
            store.put('comp', no=str(int(data['comp']['no'])+1), sol= data['comp']['sol'])
            with open('data.json', "r") as file:
                data = json.load(file)
            self.sm.get_screen('dashboard').ids.nocomp.text = data['comp']['no']
            self.sm.get_screen('dashboard').ids.nosol.text = data['comp']['sol']
            #self.sm.get_screen('dashboard').ids.nocomp.text = str(int(self.sm.get_screen('dashboard').ids.nocomp.text)+1)


            self.sm.transition.direction = "right"
            self.sm.current = "dashboard"
        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None     


    def checkStatus(self):

        with open('data.json', "r") as file:
            data = json.load(file)
        emailidact = data['details']['email']
        doc_ref = db.collection(u'users').document(emailidact)
        doc = doc_ref.get()
        doc_dict = doc.to_dict()
        if 'complaints' in doc_dict:
            mid = doc_dict['complaints']

            SCOPES = ['https://mail.google.com/']
            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'key.json', SCOPES)
                    creds = flow.run_local_server(port=0)

            try:


                service = build("gmail", "v1", credentials=creds)
                thread = service.users().threads().get(userId="me", id=mid).execute()
        #print(thread)
                org_reply = (thread['messages'][1]['snippet'])
                match = re.search(', &lt;services.iiitkare@gmail.com', org_reply)
                org_mess = thread['messages'][0]['snippet']
                replist = []
                if match:
                    start_index = match.start()
                    for i in range(start_index):
                        replist.append(org_reply[i])
                reply = "".join(replist)
                print(f"original mail: {org_mess}")
                print(f"reply: {reply}")
                self.sm.get_screen("status").ids.compte.text = 'Complaint: '+ org_mess
                self.sm.get_screen("status").ids.replyte.text = 'Reply: '+reply
                store = JsonStore('data.json')
                store.put('comp', sol=str(int(data['comp']['sol'])+1), no = data['comp']['no'])
                
                with open('data.json', "r") as file:
                    data = json.load(file)
                self.sm.get_screen('dashboard').ids.nocomp.text = data['comp']['no']
                self.sm.get_screen('dashboard').ids.nosol.text = data['comp']['sol']
                #self.sm.get_screen('dashboard').ids.nosol.text = str(int(self.sm.get_screen('dashboard').ids.nosol.text)+1)


            except:
                message = service.users().messages().get(userId="me", id=mid).execute()
                #print(message)
                print(message['snippet'])
                self.sm.get_screen("status").ids.compte.text = 'Complaint: '+ message['snippet']
                self.sm.get_screen("status").ids.replyte.text = 'Reply: Complaint not yet Solved'






        else:
            self.sm.get_screen("status").ids.replycard.opacity = 0
            self.sm.get_screen("status").ids.compte.text = 'Complaint: No Complaints to Track'
        self.sm.transition.direction = "left"
        self.sm.current = 'status'

    def callback(self):
        self.sm.transition.direction = "right"
        self.sm.current="dashboard"
        

main().run()