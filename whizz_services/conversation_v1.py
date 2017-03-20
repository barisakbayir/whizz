import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import TextToSpeechV1
import record_voice
import pygame
import os

conversation = ConversationV1(
    username='09002e2b-e2bd-4dbc-9d99-1a95e44a222c',
    password='53I2zIAzGLSX',
    version='2016-09-20')

speech_to_text = SpeechToTextV1(
    username='9d046ae2-691b-4659-af0b-15d00445b839',
    password='w81ioYzUMEYE',
    x_watson_learning_opt_out=False
)

text_to_speech = TextToSpeechV1(
    username='54a0bff9-dedb-402a-bef7-769c9f2b1844',
    password='D7aNJcMKeZsW',
    x_watson_learning_opt_out=True)  # Optional flag

workspace_id = '4ca860d6-678a-4a76-bf7c-f81fb2c93d25'
##workspace_id = '2b54aad6-6ebf-4165-a15b-1346fa1ff848'

response = conversation.message(workspace_id=workspace_id, message_input={'text': ''})
print(json.dumps(response['output']['text'][0], indent = 2))

check_number = int(input("enter check number: "))

while check_number != 0:
    if check_number == 1:
        record_voice.record()
        with open(join(dirname(__file__), 'C:/Users/Barış\Desktop\whizz_scripts/microphone-results.wav'), 'rb') as audio_file:
            response_speech = speech_to_text.recognize(
                audio_file, content_type='audio/wav', timestamps=False, word_confidence=False)
            
        text_input = ""
        if len(response_speech['results']) != 0:
            text_input = response_speech['results'][0]['alternatives'][0]['transcript']
            print("user: " + text_input)

        response = conversation.message(workspace_id=workspace_id, message_input={'text': text_input}, context=response['context'])
        if len(response['entities']) != 0:
            print(json.dumps(response['entities'], indent = 2))
            print(json.dumps(response['entities'][0]['value'], indent = 2))
            print(json.dumps(response['entities'][0]['entity'], indent = 2))
        print(json.dumps(response['output']['text'][0], indent = 2))

    elif check_number == 2:
                                   
        with open(join(dirname(__file__), 'C:/Users/Barış\Desktop\whizz_scripts/output.wav'), 'wb') as audio_file:
            audio_file.write(text_to_speech.synthesize(response['output']['text'][0], accept='audio/wav', voice="en-US_AllisonVoice"))

        #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        os.system("start C:/Users/Barış\Desktop\whizz_scripts/output.wav")
##        pygame.init()
##
##        pygame.mixer.music.load('output.wav')
##
##        pygame.mixer.music.play()

    check_number = int(input("enter check number: "))


##i = 0
##while(i < 3):
##    #text_input = response_speech['results'][0]['alternatives'][0]['transcript']
##    #print(text_input)
##    #text_input = input()
##    print("user:  " + speech[i])
##    response = conversation.message(workspace_id=workspace_id, message_input={'text': speech[i]}, context=response['context'])
##    if len(response['entities']) != 0:
##        print(json.dumps(response['entities'][0]['value'], indent = 2))
##        print(json.dumps(response['entities'][0]['entity'], indent = 2))
##    print(json.dumps(response['output']['text'][0], indent = 2))
##    i += 1
    


# When you send multiple requests for the same conversation, include the context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))
