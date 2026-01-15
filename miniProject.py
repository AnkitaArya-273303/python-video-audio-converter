import moviepy.editor as mp
import speech_recognition as sr
video_path=r"C:\Users\ankita arya\OneDrive\Desktop\AI technology\project\border.mp4"
audio_path='audioSong.wav'
print("Extracting your audio please wait....")
video=mp.VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)
recognizer=sr.Recognizer()
with sr.AudioFile(audio_path) as source:
    print("Processing audio for text---")
    audio_data=recognizer.record(source)
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcript completed successfully---")

    text_file_path = "converted_text_file.txt"
    with open(text_file_path, "w") as text_file:
        text_file.write(text)

    print("Text file saved")

except sr.UnknownValueError:
    print("Speech recognition could not understand the audio---")

except sr.RequestError as e:
    print(f"Could not request from google speech recognition services; {e}")
