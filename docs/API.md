# API
This doc is a step by step doc that will help you understand the API.

Prerequisite: Dummy Data Placed, Copy the clinic UUID and keep it some where

Setup
- First Insert all the tokens generated from `show_token` file on the auth corner (Refer to the top README.md)

Patient Insert
- Insert your questionnaire as patient `api/v1/fill_questionnare/`

Doctor Insert
- Get `api/v1/cartels/` and confirm your cartel
- Select your cartel by getting `api/v1/cartels/{cartel_id}/` and confirm your cartel
- Get `api/v1/cartels/{cartel_id}/patient/` and confirm your account
- Put `api/v1/cartels/{cartel_id}/` and enter your diagnosis

Image Check
- Get `api/v1/cartels/{cartel_id}/` on a pre-existing Account
- Get `api/v1/cartels/{cartel_id}/images/` and check for API
- Get `api/v1/cartels/{cartel_id}/imaeges/{image_id}/` and get detail of your image

Image Upload
- POST `api/v1/upload_image/`
- Get `api/v1/cartels/` and confirm your cartel

Upload Score
- POST `api/v1/upload_image/`
- Get `api/v1/cartels/` and confirm your cartel