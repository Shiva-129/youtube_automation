import pandas as pd
import subprocess
import os
from pathvalidate import sanitize_filename
import logging
from datetime import datetime

# Set up directories and logging
DOWNLOADS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
ERROR_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_log.txt')

# Ensure downloads directory exists
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=ERROR_LOG,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def sanitize_title(title):
    """Sanitize video title to make it suitable for filename"""
    return sanitize_filename(title).replace(' ', '_')

def download_video(url):
    """Download YouTube video using yt-dlp"""
    try:
        # Get video title
        title_cmd = [
            r'C:\Users\shiva\AppData\Roaming\Python\Python313\Scripts\yt-dlp.exe',
            '--get-title',
            '--no-warnings',
            url
        ]
        result = subprocess.run(title_cmd, capture_output=True, text=True, check=True)
        title = result.stdout.strip()
        
        # Sanitize title for filename
        safe_title = sanitize_title(title)
        output_path = os.path.join(DOWNLOADS_DIR, f"{safe_title}.%(ext)s")
        
        # Download video
        download_cmd = [
            r'C:\Users\shiva\AppData\Roaming\Python\Python313\Scripts\yt-dlp.exe',
            '-f', 'bestvideo+bestaudio',
            '--merge-output-format', 'mp4',
            '--external-downloader', 'aria2c',
            '--retries', '10',
            '--fragment-retries', '10',
            '--socket-timeout', '30',
            '--console-title',
            '-o', output_path,
            '--no-warnings',
            url
        ]
        subprocess.run(download_cmd, check=True)
        
        return True, title
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to download {url}: {str(e)}")
        return False, str(e)
    except Exception as e:
        logging.error(f"Unexpected error with {url}: {str(e)}")
        return False, str(e)

def main():
    start_time = datetime.now()
    print("Starting YouTube downloader...")
    
    # Read Excel file
    df = pd.read_excel('videos.xlsx')
    
    if 'Link' not in df.columns:
        print("Error: Excel file must contain a 'Link' column")
        return
    
    total = len(df)
    success_count = 0
    fail_count = 0
    
    for _, row in df.iterrows():
        url = row['Link']
        if pd.notna(url) and isinstance(url, str) and url.startswith(('http://', 'https://')):
            print(f"\nProcessing: {url}")
            success, result = download_video(url)
            
            if success:
                print(f"Successfully downloaded: {result}")
                success_count += 1
            else:
                print(f"Failed to download: {result}")
                fail_count += 1
        else:
            print(f"Skipping invalid URL: {url}")
            fail_count += 1
    
    end_time = datetime.now()
    duration = end_time - start_time
    
    print("\n=== Download Summary ===")
    print(f"Total URLs processed: {total}")
    print(f"Successfully downloaded: {success_count}")
    print(f"Failed downloads: {fail_count}")
    print(f"Time taken: {duration}")
    print(f"Error log saved to: {ERROR_LOG}")
    print("Done.")

if __name__ == "__main__":
    main()