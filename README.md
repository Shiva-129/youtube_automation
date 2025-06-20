📁 YouTube Shorts Downloader & Uploader Automation
This project helps automate downloading YouTube Shorts from a list of URLs stored in an Excel file and then uploading them to a specified YouTube account using OAuth authentication.

📌 Features
📥 Download YouTube Shorts from a list of short URLs in an Excel file using download_youtube.py.

📤 Upload Shorts to YouTube using upload_shorts.py after OAuth setup.

📄 Simple configuration using an Excel file(videos.xlsx) and Google OAuth credentials.

🛠️ How to Use
1. Clone this Repository

git clone 
cd shorts-automation
2. Prepare the Excel File

Place your Excel file (videos.xlsx) in the root folder. It should contain a list of YouTube Shorts URLs.

3. Download Shorts

Run the following command to download all shorts to the downloads/ folder:

                    python download_youtube.py

🔐 Setting up OAuth for YouTube API
Before uploading, you need to create OAuth 2.0 credentials:

    Step-by-step:
    Go to Google Cloud Console.

    Create a new project (or select an existing one).

    Navigate to APIs & Services > Credentials.

    Click Create Credentials > OAuth Client ID.

    Choose Desktop App as the application type.

    After creation, click Download JSON and rename it to: client_secrets.json

    Important:
        Go to APIs & Services > Library

        Enable the following API:
            ✅ YouTube Data API v3

🚀 Upload Shorts
    Open the browser that has the YouTube account you want to upload to.

    Log into that account beforehand.

    Run:
        python upload_shorts.py

    The script will open a browser window for authentication. Approve access using the logged-in account.

📂 Folder Structure
shorts-automation/
│
├── downloads/             # Downloaded shorts saved here
├── download_youtube.py    # Script to download shorts from Excel
├── upload_shorts.py       # Script to upload shorts to YouTube
├── client_secrets.json    # Your OAuth 2.0 client credentials
└── videos.xlsx            # Excel file with YouTube short URLs
