from pytube import YouTube

# Ask the user for the YouTube video URL
url = input("Enter the YouTube video URL: ")
# Create a YouTube object
yt = YouTube(url)

# Print the video title and available formats
print("Title:", yt.title)
print("Available formats:")
for stream in yt.streams:
    print(stream)

# Ask the user to select a format to download
itag = int(input("Enter the itag of the format to download: "))

# Get the stream with the selected itag
stream = yt.streams.get_by_itag(itag)

# Download the stream
print("Downloading...")
stream.download()
print("Download complete!")
