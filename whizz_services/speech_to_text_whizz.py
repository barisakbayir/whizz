import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


speech_to_text = SpeechToTextV1(
    username='9d046ae2-691b-4659-af0b-15d00445b839',
    password='w81ioYzUMEYE',
    x_watson_learning_opt_out=False
)

#print(json.dumps(speech_to_text.models(), indent=2))

#print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), 'C:/Users/Barış\Desktop/CNG 491/speech-to-text-websockets-python-master/recordings/0001.wav'), 'rb') as audio_file:
    response = speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=False, word_confidence=False)
    print(json.dumps(response['results'][0]['alternatives'][0]['transcript'], indent = 2))
