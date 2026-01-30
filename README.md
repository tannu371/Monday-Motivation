# Monday Motivation

## Email SMTP setup

1. Use the correct SMTP address for your email provider::

| Provider | SMTP Server             |
| -------- | ----------------------- |
| Gmail    | `smtp.gmail.com`        |
| Hotmail  | `smtp.live.com`         |
| Outlook  | `outlook.office365.com` |
| Yahoo    | `smtp.mail.yahoo.com`   |

👉 If you’re using another provider, search online for:
<your email provider> SMTP server settings

2. Go to https://myaccount.google.com/

Select Security on the left and scroll down to How you sign in to Google.

3. Find the section on App Passwords by searching for it:

There you can add an App password.

Select give your app a name e.g., Python Mail and click create. 

COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.

Use this App password in your Python code instead of your normal password.

4. By default smtplib.SMTP uses port 25. This used to be the standard SMTP port, but because of abuse in the past most servers nowadays have blocked this port to external traffic. There are still some that do allow it; Hotmail, Live, etc. Port 25 is still used for traffic between servers, but many providers have switched to using port 587 for external traffic. If in doubt, search the internet for "smtp server settings" for your provider.

Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587)

---

## Running on local machine

### Set Environment variables
Create a .env file in the project root and add:

    EMAIL_SMTP_SERVER=smtp-server-address-of-your-email-provider
    EMAIL_PORT=587

    EMAIL_ID=your-mail-id
    EMAIL_PASSWORD=your-app-password

**Create Python virtual environment**

    python3 -m venv .venv

**Activate enironment**

    source .venv/bin/activate

**Intall required package**

    pip install -r ./requirements.txt

**Run python main file**

    python3 main.py

---
