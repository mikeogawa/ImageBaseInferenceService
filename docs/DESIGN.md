# Image Based Inference Service

This Repository is an sample respository for image based inference service (e.g. image based diagnosis).  
This doc explains a service where images are taken from an IOT device and sent to the cloud for AI analysis.  

# Assumptions

### Character
There are 4 types of character base on this repository:
- Clinical Doctor
- Patient
- IOT Device
- AI Service

### Dynamics
Based on the characters described above, we assume the following dynamics:
- The Clinical Doctor takes pictures of their patients, and thereafter uses AI to analyze the pictures
- The Paitent goes to the clinic (due to illness etc.)
- The Patient answers a questionnare
    - The Patient enters her account
    - If logined before, then we use that account
    - The Patient enters her account
- The Clinical Doctor checks the questionnare and simply diagnose the Patient
- The Clinical Doctor makes the record of the result
- The Clinical Doctor takes serveral pictures of the patient with an IOT device
- The IOT Device sends pictures to the server
- The AI analyze the pictures and scores each picture
- The Clinical Doctor examines the picture and furher diagnose the Patient
- The Clinical Doctor informs the result to the Patient

### Other Detail
We also assumed the following:
- Machine entites are not required
- Doctors can register data 
- Patients can use their own ID/Pasword info in other clinics
- Doctors can only access one clinic
- Doctors can view diagnosis of other patients based on other doctors
- Image analysis can take time

# Requirements
With the above assumption established, we can consider the following features as the requirement:

System that:
- Allows access from any clinic
- Register Patient information from the Patient side
- Access Patient information from the Clinical Doctor side
- Access infered image of Patients from the Clinical Doctor side
- Register image from the IOT Device
- Register inference score from and AI Service
- Register Patient diagnosis from the Clinical Doctor side

# System Implementation
We have considered the following implementation to achieve to above requirements: 

### ER Diagram
<img src="/docs/img/simple_er.png" width="500px" />

- Cartels have information regarding the patient, so we can merge the questionnare and information from doctors into 1 entity
- We wanted to easily access cartels written by other doctors, so we made a relationship between the clinic (multi-tenant)
- Comaparing images despite patient information (cartel) is highly unlikely to happen, thus we do not have to make a relationship between the cliniic and only depend on the cartel.


### Use Case Digram
<img src="/docs/img/usecase_diagram.png" width="500px" />

### System Archiecture
<img src="/docs/img/cloud_architecture.png" width="700px" />

- Authentication is done by third party service (thus only tokens are passed towards the backend)
- Images are sent to the backend directly
- Images are uploaded to a bucket service(e.g. S3)
- Bucket service triggers a message and sends it to a queue
- AI service recieves thhe queue and analyze the image data
- Results are sent to backend server

### Backend Architecture
<img src="/docs/img/backend_architecture.png" width="600px" />

Details:
- UI Layer
    - Clinic App
    - Patient App
    - IOT Device (machine)
    - AI Analysis (machine)
- View Layer
    - API Handler
    - directory: `/backend/v1/views`
- Use Case Layer
    - code description of the use case described previously
    - directory: `/backend/v1/use_cases`
- Service Layer
    - Facade class that handles request, response, getters, setters from repositories outside of usecase
    - directory: `/backend/v1/services`
- Domain Layer
    - Entites that exist within the usecase real
    - Domains that don't require RDS are inversely depend toward them (Rich Model)
    - Domain that require RDS are depend toward it
    - directory: `/backend/v1/domain`
- Repository Layer
    - Object that are responsible for communicating other service (e.g. upload to data bucket, send request to AI Service)
    - Ideally, RDS relaed service should be part of the repostiory, but considering the amount required to implement it, we chose not to do it and instead be depend on it.
    - directory: `/backend/v1/repositories`



