import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_image():
    # Prompt user for URL
    image_url = input("Enter the image URL: ").strip()

    # Validate URL
    if not image_url.startswith(("http://", "https://")):
        print("❌ Invalid URL. Must start with http:// or https://")
        return

    # Create directory
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Send HTTP GET request
        response = requests.get(image_url, timeout=10)

        # Check for HTTP errors
        response.raise_for_status()

        # Ensure it's an image
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print("❌ The URL does not point to an image.")
            return

        # Extract filename from URL or fallback to 'downloaded_image'
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image"

        # Add appropriate file extension if missing
        extension = content_type.split("/")[-1]
        if not filename.lower().endswith(f".{extension}"):
            filename += f".{extension}"

        # Full path
        filepath = os.path.join(folder, filename)

        # Save image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✅ Image successfully saved as: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download image. Error: {e}")

if __name__ == "__main__":
    fetch_image()
