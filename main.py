# coding: utf8
import os
import whisper
from playsound import playsound
import time


def transcription(filename_audio, directory, modelSize):
    model = whisper.load_model(modelSize)
    result = model.transcribe(directory+filename_audio, fp16=True, language='French')
    with open("resultats/" + filename_audio+'.txt', 'w') as f:
        f.write(result['text'])

inputUser = False
modelSize = False
while inputUser == False:
    inputUser = True
    print("X pour quitter")
    print("Choisissez le modèle :")
    print("1. Tiny - Relative speed ~32x")
    print("2. Base - Relative speed ~16x")
    print("3. Small - Relative speed ~6x")
    print("4. Medium - Relative speed ~2x")
    print("5. Large - Relative speed ~1x")
    inputUser = input("Choix : ")
    if inputUser == '1':
        modelSize = 'tiny'
        print('Modèle ['+modelSize+']')
    elif inputUser == '2':
        modelSize = 'base'
        print('Modèle [' + modelSize + ']')
    elif inputUser == '3':
        modelSize = 'small'
        print('Modèle [' + modelSize + ']')
    elif inputUser == '4':
        modelSize = 'medium'
        print('Modèle [' + modelSize + ']')
    elif inputUser == '5':
        modelSize = 'large'
        print('Modèle [' + modelSize + ']')
    elif inputUser == 'x':
        print("Bye !")
    else:
        inputUser == False

if modelSize != False:
    directory = 'audios/'
    audio_list = os.listdir(directory)
    timeStartGlobal = time.time()
    for file_name in audio_list:
        timeStart = time.time()
        print("Début transcription [" + file_name + "] ... ", end='')
        transcription(file_name, directory, modelSize)
        timeEnd = time.time()
        timeDone = timeEnd - timeStart
        if timeDone > 120:
            timeDone = round(timeDone / 60)
        else:
            timeDone = round(timeDone / 60, 2)
        print("Terminé en " + str(timeDone) + ' minutes.')

    timeEndGlobal = time.time()
    timeDoneGlobal = round((timeEndGlobal-timeStartGlobal)/60)
    print('Temps total de traitement : ' + str(timeDoneGlobal) + ' minutes.')
    print(">>> Transcription des fichiers terminée.")
    playsound('bin/pop.mp3')











