import gtts
from playsound import playsound
from moviepy.editor import *
# text = 'In this article we will see how we can add external audio to the video file clip in MoviePy. MoviePy is a Python module for video editing, which can be used for basic operations on videos and GIF’s. Video is formed by the frames, combination of frames creates a video each frame is an individual image. An audio file format is a file format for storing digital audio data on a computer system. The bit layout of the audio data is called the audio coding format and can be uncompressed, or compressed to reduce the file size, often using lossy compression. We can load the audio file with the help of AudioFileClip method.'
text = 'नमस्ते, मैं मयूख हूं। कृपया मुझे वोट दें, कृपया बैलेट मशीन पर बटन दबाएं. प्रिय छात्रों – भाषण सभा में आपका स्वागत है! आशा है अलग-अलग गतिविधियों के चलते आपकी पढाई प्रभावित नहीं हो रही है और जो आपके साप्ताहिक परीक्षण चल रहे हैं उनमें भी आप अच्छे नतीजे ला रहे हैं। आज के भाषण का विषय राजनीति है। राजनीति क्यों? क्योंकि यह हमेशा से एक चर्चित विषय रहा है चाहे आप किसी भी देश से संबंध रखते हो। राजनीति इतना आकर्षक विषय है कि हर किसी को कुछ न कुछ इस पर कहना है। इसके अलावा मुझे यह जरूरी लगता है कि मेरे छात्रों को थ्योरी पर ध्यान देने की बजाए प्रैक्टिकल विषयों पर ध्यान ज्यादा देना चाहिए और पूरे आत्मविश्वास से अपनी सोच और विचारों को रखने में सक्षम होना चाहिए। तो मेरे भाषण के माध्यम से मुझे आशा है कि आप बहुत कुछ सीख सकेंगे। '
language = 'hi'
title='output'

output = gtts.gTTS(text=text, lang=language, slow=False,tld='co.in')
audio_name = title+".mp3"
output.save(audio_name)
#playsound(audio_name)
video_path = "video.mp4"
audio_path = "output.mp3"
# Create instances of VideoFileClip and AudioFileClip
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)
video_clip_with_audio = video_clip.set_audio(audio_clip)
# Write the merged video file to a new file
video_clip_with_audio.write_videofile("output_video.mp4")
