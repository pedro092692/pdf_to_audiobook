from boto3 import Session
from dotenv import load_dotenv
import os
load_dotenv()
# voice of speech
voice_id = 'Joanna'


class TextToAudio:

    def __init__(self):
        self.session = Session(
            aws_access_key_id=os.environ.get('aws_access_key_id'),
            aws_secret_access_key=os.environ.get('aws_secret_access_key'),
            region_name='us-east-1'
        )

        self.polly = self.session.client('polly')

    def create_mp3(self, text):
        response = self.polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId=voice_id)
        if 'AudioStream' in response:
            with open('text_mp3.mp3', mode='wb') as audio:
                audio.write(response['AudioStream'].read())
        else:
            print('Sorry There was and error!')
