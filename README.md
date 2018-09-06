# MLWGSGIS Texting Script

## What is this?
This is a Python script read contact information and send text messages using Twilio's SMS functionality. It runs as a command-line script, which prompts you to enter the CSV filename and whether this is a trial run. (Trial defaults to True, in which case the messages are printed out to command line for manual verifiation.)

![CLI preview](https://github.com/micaswyers/mlwgsgis/blob/master/img/screenshot_cli.png)

The output looks like this:

![Text message preview](https://github.com/micaswyers/mlwgsgis/blob/master/img/screenshot_text.png)

## Why is it useful?
Every year, I am tasked with contacting alumni from my graduating class, asking for donations to the school's foundation. I used to do this manually, but then I remembered that I am a software engineer and can automate away such tasks.

## Can I use it?
Sure, you can, but I wrote this as a one-off script that is specific to the contact information spreadsheed that I get every year from the Foundation. If you choose to adapt it for your own use, you will have to enter in your own credentials (and get yourself a Twilio number).

## How do I run it?
You must have a Twilio phone number with credentials set up. You also will need a CSV document with the people you want to text.

Run `pip install requirements.txt` to get necessary requirements. I recommend doing this in a [virtual environment](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html).

Run `python text_people.py` to start the CLI script.
