
from trycourier import Courier
def sendEmail(emailAddress):
      client = Courier(auth_token="pk_prod_1XAN8A80K7498QH3GSTP6M711Y5T")
      resp = client.send_message(
        message={
          "to": {
            "email": emailAddress
          },
          "routing": {
            "method": "single",
            "channels": ["email"]
          },
          "channels" : {
            "email": {
              "providers": ["gmail"] 
            }
          },
          "content": {
            "title": "CSV upload Notification",
            "body": "Your csv file upload was successful"
          }
        }
      )  