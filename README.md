# elo-whisper
Transcription automatique de fichiers audios avec OpenAI Whisper.

Liens du GitHub Whisper : https://github.com/openai/whisper
<h2>Installation ffmpeg</h2>
Utilisation de chocolatey : https://github.com/openai/whisper

```
choco install ffmpeg-full
```
Puis placer le fichier `ffmpeg.exe` dans <i>C:\Windows\System32</i>

###Installation des modules :
```
pip install -r requirements.txt
```
## Utilisation
Placez les fichiers audios � retranscrire dans le dossier ``audios``. Des fichiers audios d'exemple sont disponibles dans le dossier ``audio_samples``.

Lancez le programme via :
````commandline
python main.py
````
Choissisez le mod�le. Plus le mod�le est rapide, moins il est pr�cis dans sa transcription.

Une fois la transcription termin�e, les fichiers .txt de chaque fichiers audios se trouvent dans le dossier ```resultats```.
### Si erreur utilisation GPU
Commencer par d�sinstaller torch puis installer cuda-python
````commandline
pip uninstall torch torchvision torchaudio
pip cache purge
pip install cuda-python
````
Puis installer Pytorch en choisissant la version ici : https://pytorch.org/ (dans la section INSTALL PYTORCH)
Exemple : :
````commandline
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
````
### Si pas de GPU d�di� 
Forcer l'utilisation du CPU dans le main.py en ajoutant ``device='cpu'`` dans les param�tres ``model = whisper.load_model(modelSize, device='cpu')``.
Si utilisation en ligne de commande : 
````commandline
whisper AUDIO.mp3 --model medium --device cpu [--language French]
````