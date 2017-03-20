import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


speech_to_text = SpeechToTextV1(
    username='68bc7aa9-32da-4476-b5e6-0e1dc91e0b06',
    password='1cI2YMxbJnWX',
    x_watson_learning_opt_out=False
)

print(json.dumps(speech_to_text.models(), indent=2))

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), 'C:/Users/kadii\Desktop/Whizz/python-sdk-master/resources/my_speech_2.wav'), 'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=True, word_confidence=True), indent=2))
