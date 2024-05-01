from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.1",
    author="JunaidARahat",
    author_email="mjunaidrahat1990@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)