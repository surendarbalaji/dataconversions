from pydub import AudioSegment
import os

AudioSegment.converter = "C:\\Program Files\\FFMPEG\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\Program Files\\FFMPEG\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\Program Files\\FFMPEG\\bin\\ffprobe.exe"

ffmpeg_path = "C:\\Program Files\\FFMPEG\\bin\\ffmpeg.exe"
ffprobe_path = "C:\\Program Files\\FFMPEG\\bin\\ffprobe.exe"

if os.path.isfile(ffmpeg_path) and os.path.isfile(ffprobe_path):
    AudioSegment.converter = ffmpeg_path
    AudioSegment.ffmpeg = ffmpeg_path
    AudioSegment.ffprobe = ffprobe_path
else:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ffmpeg or ffprobe not found.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

ffmpeg_dir = "C:\\Program Files\\FFMPEG\\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_dir

audio = AudioSegment.from_mp3("---")

data = []

with open("songs.txt", "r") as file:
    for line in file:
        data.append(line.split(" "))

for i in range(len(data) - 1):
    song = data[i]

    song_name = ' '.join(song[1:]).strip()

    timestamp = song[0].split(":")
    start = (int(timestamp[0]) * 3600 + int(timestamp[1]) * 60 + int(timestamp[2])) * 1000

    next_timestamp = data[i+1][0].split(":")
    end = (int(next_timestamp[0]) * 3600 + int(next_timestamp[1]) * 60 + int(next_timestamp[2])) * 1000

    clip = audio[start: end]
    clip.export(f"{song_name}.mp3", format="mp3")
    print(f"{start} to {end} cut and saved as {song_name}")