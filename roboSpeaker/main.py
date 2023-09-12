import os

if __name__ == '__main__':
    print("Welcome to robo speaker 1.1")
    x = input('What do you want me to say?')
    command = f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
    os.system(command)
