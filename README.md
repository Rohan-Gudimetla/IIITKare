# IIITKare

This is an Android Application which I have developed to register and track complaints regarding any of the services of my College (IIIT Kottayam, Kerala)




## Features

This Application allows users to:

- Register themselves using the College Mail ID.
- Login into their Accounts.
- Register a new Complaint
- Check the status of their Complaint.


## Tech Stack used

- **Python Programming Language**

- **Firebase:** Firestore Database, Creating and Managing new Accounts, Pushing Notifications.

- **Gmail API:** Sending Complaints registered to corresponding Authorities mailbox, Reading the replies of the authorities to the complaints.

- **Kivy Framework of Python:** To develop the GUI of the Android Application.

- **Pyrebase Framework of Python:** To manage Firebase wherever Python support not available.

- **Webhooks:** To Trigger Scripts upon receiving Replies (from authorities) to the Complaint mails, which are then sent as a JSON POST.



## Workflow

- **Registering a Complaint:** When a User Registers a new Complaint by choosing the appropriate options from the Dashboard of the App, and describing the Complaint, the Complaint is registered and User is brought back to the Dashboard.

- **Receiving the Complaint:** These complaints are received in the Mail Box of the Corresponding authorities. All the Complaints would be sent from a single Mail ID: [services.iiitkare@gmail.com](services.iiitakare@gmail.com)

- **Complaint Redressal:** In order to redress a particular complaint, the Authority who received the complaint just need to **Reply** to the Complaint mail.

- **User Notification:** When an Authority replies to the Complaint mail, the mail is delivered to the App mail ID, which triggers a **Webhook** to invoke a Script hosted on [https://www.pythonanywhere.com](https://www.pythonanywhere.com/) which pushes a Notification to the **Concerned User** of the Complaint (Using some Parsing Techniques). 

- **Viewing the Complaint Status:** By choosing the Corresponding option on the Dashboard, a User shall be able to check the **Status** or the **Solution of his Complaint**.


## Screenshots

![Opening Screen]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://github.com/Rohan-Gudimetla/IIITKare/blob/main/app/screenshots/Screenshot_20230202_214015.png))
**Opening Screen**
<img width="337" alt="Screenshot_20230202_214015" src="https://user-images.githubusercontent.com/97049524/224529497-96aee3ca-7a30-444d-ac84-aa9a247d3bd2.png">
