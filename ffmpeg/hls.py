import subprocess
from dotenv import load_dotenv
import os

def download_m3u8():
    load_dotenv()
    output_default_path = os.getenv('OUTPUT_PATH', '.')

    while True:
        m3u8_url = input("Enter the M3U8 URL (or type 'exit' to quit): ")
        if m3u8_url.lower() == 'exit':
            print("Exiting the program.")
            break
        
        output_filename = input("Enter the output file name (e.g., 'output.mp4'): ")
        output_file = os.path.join(output_default_path, output_filename)

        confirmation = input(f"Confirm download of '{m3u8_url}' to '{output_file}'? (yes/no): ")
        if confirmation.lower() != 'yes':
            print("Download cancelled.")
            continue

        ffmpeg_command = [
            'ffmpeg',
            '-user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            '-headers', 'Referer: https://jable.tv/',
            '-i', m3u8_url,
            '-c', 'copy',
            output_file
        ]

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"Downloaded and saved to {output_file}.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_m3u8()
