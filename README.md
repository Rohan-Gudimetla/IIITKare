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


<img width="337" alt="Screenshot_20230202_214015" src="https://user-images.githubusercontent.com/97049524/224529497-96aee3ca-7a30-444d-ac84-aa9a247d3bd2.png">

<img width="318" alt="Screenshot_20230202_214421" src="https://user-images.githubusercontent.com/97049524/224529513-13fee4f9-4b42-4482-8b9f-f74d813eb378.png">
<img width="759" alt="Screenshot_20230202_214541" src="https://user-images.githubusercontent.com/97049524/224529521-96c2aa81-ce7e-47b3-8a57-4b19774513b9.png">
<img width="323" alt="Screenshot_20230202_214618" src="https://user-images.githubusercontent.com/97049524/224529543-88b5ff87-1fdc-4155-a44f-19733fded2ac.png">
<img width="691" alt="Screenshot_20230202_214734" src="https://user-images.githubusercontent.com/97049524/224529559-48294f4a-e75c-4b68-aebe-69ff30180b19.png">

<img width="323" alt="Screenshot_20230202_214837" src="https://user-images.githubusercontent.com/97049524/224529571-78e86dfb-ed2a-49a8-85cb-8c47f922e29e.png">
<img width="754" alt="Screenshot_20230202_214915" src="https://user-images.githubusercontent.com/97049524/224529600-b7644ec5-aaf2-49a2-a03b-7dd9fa6a69c8.png">
<img width="325" alt="Screenshot_20230202_214938" src="https://user-images.githubusercontent.com/97049524/224529601-0aca8af7-d271-430d-999c-15e98f86d7fb.png">


<img width="321" alt="Screenshot_20230202_215104" src="https://user-images.githubusercontent.com/97049524/224529609-bcd80e52-86c6-4266-a2a2-593dd3929e58.png">


<img width="325" alt="Screenshot_20230202_215140" src="https://user-images.githubusercontent.com/97049524/224529614-29a8f499-4b7f-4d49-9db1-56560da50130.png">

<img width="325" alt="Screenshot_20230202_215220" src="https://user-images.githubusercontent.com/97049524/224529616-7cc016a5-a038-4974-ac56-790f8ee08e04.png">

<img width="718" alt="Screenshot_20230202_215349" src="https://user-images.githubusercontent.com/97049524/224529625-48275cad-edd3-4369-b481-b8e3e395ea51.png">

<img width="323" alt="Screenshot_20230202_215456" src="https://user-images.githubusercontent.com/97049524/224529633-57d8b886-00ad-45de-806a-1b499833cdf9.png">

<img width="326" alt="Screenshot_20230202_215513" src="https://user-images.githubusercontent.com/97049524/224529637-3f9b4115-f208-4bb6-a340-213495cb4dc6.png">

## Developer

Rohan Gudimetla
[rohan.gudimetla07@gmail.com](rohan.gudimetla07@gmail.com)
