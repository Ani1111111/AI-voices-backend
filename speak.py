'''File that convert text to speech'''
import pyttsx3
import os
from loguru import logger

def Speak(speak_text, voice_id = 'english', gender = None, rate = 130, volume = 1.0):  
    '''Function to speak text'''
    engine = pyttsx3.init()
    path_to_file = f'/tmp/{voice_id}.mp3'
    logger.debug(voice_id)
    logger.debug(gender)
    logger.debug(rate)
    engine.setProperty('voice',voice_id)
    engine.setProperty('rate', int(rate))
    engine.setProperty('volume',volume)
    engine.save_to_file(speak_text, path_to_file)
    engine.runAndWait()
    engine.stop()
    
    return path_to_file


if __name__ == '__main__':
    Speak('Animesh is a good boy')