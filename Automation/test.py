url = "https://drive.google.com/file/d/1YRa3M262PjWjK8CQZqgohmTGkzmtEs9r/view?usp=drive_link"

def extract_file_id(url):
  """Extracts the file ID from a Google Drive URL."""
  return url.split("/")[-2]



def main():
    file_id = extract_file_id(url)

    print(f" file id: {extract_file_id(url)}")
    print(f"download link: {generate_direct_download_link(file_id)}")
    
if __name__ == "__main__":
    main()