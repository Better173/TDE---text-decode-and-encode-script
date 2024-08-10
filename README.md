# TDE / text-decode-and-encode-script
Secure Text Encoder/Decoder

This script is a practical tool designed to enhance privacy in communication by allowing users to encode and decode messages using a custom seed phrase. It provides a way to securely transmit information over non-secure messaging platforms, ensuring that only individuals with the correct seed phrase can decrypt the encoded content.

Key Features:

    Custom Encoding/Decoding: Utilize a user-defined seed phrase to encode and decode messages. This adds a layer of security to text communications, making it accessible only to those who know the seed phrase.
    Anonymity for Non-Secure Platforms: Ideal for use with messaging services that lack robust encryption features, this script ensures that sensitive information remains private even when transmitted through less secure channels.
    Easy Integration: Seamlessly integrate with your preferred text-based communication methods to enhance privacy without altering your existing workflows.

Example Non-Secure Messengers:

    SMS (Short Message Service): Traditional text messaging that lacks encryption and can be intercepted.
    Basic Email Clients: Email services that do not offer end-to-end encryption, making them susceptible to unauthorized access.
    Generic Chat Applications: Older or non-encrypted versions of popular chat apps (e.g., earlier versions of WhatsApp or Telegram) that do not provide secure end-to-end encryption.

Usage:
To use this script, simply input your message and seed phrase to encode it. Share the encoded message via your chosen non-secure messenger. The recipient, who knows the seed phrase, can then decode the message to reveal the original content.

How to download:

1.Clone the repository:
  ```bash
git clone https://github.com/Better173/TDE---text-decode-and-encode-script.git
  ```
2.Navigate to the Project Directory:
  ```bash
cd TDE---text-decode-and-encode-script
  ```
3.Run the Script:
  ```bash
python3 text-decode-encode.py
  ```
