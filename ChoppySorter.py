import os
import shutil

# Define the source directory where downloaded files are stored
download_dir = os.path.expanduser("~/Downloads")  # Change this to your download directory

# Define destination directories for different file types
destination_dirs = {
    ".pdf": os.path.expanduser("~/Documents/PDFs"),
    ".jpg": os.path.expanduser("~/Documents/Pictures"),
    ".png": os.path.expanduser("~/Documents/Pictures"),
    ".txt": os.path.expanduser("~/Documents/TextFiles"),
    # Add more file extensions and destination directories as needed
}

def organize_downloads():
    # Get a list of all files in the download directory
    files = os.listdir(download_dir)

    for file in files:
        src_path = os.path.join(download_dir, file)

        if os.path.isfile(src_path):
            # Get the file extension
            _, ext = os.path.splitext(file)

            # Check if the extension exists in destination_dirs 
            if ext in destination_dirs:
                dest_dir = destination_dirs[ext]

                # Create the destination directory if not already created
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                # Construct the destination path
                dest_path = os.path.join(dest_dir, file)

                # Move the file to the destination
                shutil.move(src_path, dest_path)
                print(f"Moved '{file}' to '{dest_dir}'")

if __name__ == "__main__":
    organize_downloads()
