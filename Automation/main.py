import requests
from bs4 import BeautifulSoup

def extract_file_id(url):
  """Extracts the file ID from a Google Drive URL."""
  return url.split("/")[-2]

def generate_direct_download_link(file_id):
  """Generates a direct download link for a Google Drive file ID using gdocs2direct."""
  base_url = "https://drive.google.com/uc?export=download&id="
  download_url = f"{base_url}{file_id}"
  return download_url

def process_file(url, output_file):
  """Processes a single Google Drive URL, extracts ID, generates direct download link and writes to output."""
  file_id = extract_file_id(url)
  download_link = generate_direct_download_link(file_id)
  output_file.write(f"{download_link}\n")

def main():
  """Reads URLs from a file, processes them and writes direct download links to another file."""
  input_file = "input.txt"  # Replace with your input file name
  output_file = "output.txt"  # Replace with your output file name
  
  with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
      url = line.strip()
      process_file(url, f_out)

if __name__ == "__main__":
  main()
