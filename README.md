# elo-whisper
Transcription automatique de fichiers audios avec OpenAI Whisper.

Liens du GitHub Whisper : https://github.com/openai/whisper
<h2>Installation ffmpeg</h2>
Utilisation de chocolatey : https://github.com/openai/whisper

```
choco install ffmpeg-full
```
Puis place le `ffmpeg.exe` dans <i>C:\Windows\System32</i>

###Installation des modules :
```
pip install -r requirements.txt
```
## Utilisation
````commandline
python main.py
````

### Si erreur utilisation GPU
Commencer par désinstaller torch puis installer cuda-python
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
### Si pas de GPU dédié 
Forcer l'utilisation du CPU dans le main.py en ajoutant ``device='cpu'`` dans les paramètres ``model = whisper.load_model(modelSize, device='cpu')``.
Si utilisation en ligne de commande : 
````commandline
whisper AUDIO.mp3 --model medium --device cpu [--language French]
````