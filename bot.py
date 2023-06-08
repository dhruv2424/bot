import time
from selenium import webdriver
import smtplib
import requests

# Function to send an email
def send_email(subject, body):
    # Update with your Gmail account details
    gmail_user = "your_email@gmail.com"
    gmail_password = "your_password"
    recipient = "recipient_email@gmail.com"

    # Create email message
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)

        # Send email
        server.sendmail(gmail_user, recipient, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
    finally:
        server.quit()

# Function to upload content to Cyclic server
def upload_to_cyclic(content):
    # Update with your Cyclic server URL
    cyclic_url = "https://your-cyclic-server.com/upload"

    try:
        # Send POST request to Cyclic server
        response = requests.post(cyclic_url, data=content)
        if response.status_code == 200:
            print("Content uploaded to Cyclic successfully!")
        else:
            print(f"An error occurred while uploading to Cyclic: {response.text}")
    except Exception as e:
        print(f"An error occurred while uploading to Cyclic: {str(e)}")

# Open the website using Selenium
driver = webdriver.Chrome()  # Make sure to have Chrome driver installed and in PATH
driver.get("https://www.example.com")

# Wait for 10 seconds
time.sleep(10)

# Get the website content
website_content = driver.page_source

# Close the Selenium driver
driver.quit()

# Send the website content to your Gmail
email_subject = "Website Content"
send_email(email_subject, website_content)

# Upload the website content to Cyclic
upload_to_cyclic(website_content)


