## To run this code:
## Play full audio (default) with default interval (60 minutes)
# python stretchBreak.py
## Play short audio with default interval
# python stretchBreak.py -t short
## Play full audio with custom interval (e.g., 30 minutes)
# python stretchBreak.py -i 30
## Play full audio with custom interval
# python stretchBreak.py -t full -i 45

import time
import argparse
from datetime import datetime
import os
import platform
import subprocess

def play_audio_file(audio_path, system):
    """
    Plays an audio file using the appropriate command for the operating system
    
    Args:
        audio_path (str): Path to the audio file
        system (str): Operating system name
    """
    if system == 'Darwin':  # macOS
        subprocess.run(['afplay', audio_path])
    elif system == 'Windows':
        subprocess.run(f'start /wait "" "{audio_path}"', shell=True)
    else:  # Linux and others
        subprocess.run(['xdg-open', audio_path])

def play_audio_at_interval(interval_minutes, audio_type):
    """
    Plays a local audio file at specified intervals using the system's default player
    
    Args:
        interval_minutes (int): Time interval between plays in minutes
        audio_type (str): Either 'short' or 'full' to select which audio to play
    """
    # Define paths for both audio files
    audio_paths = {
        'short': "stretchBreak_clip.mp3",  # Replace with your short audio path
        'full': "stretchBreak_full.mp3"     # Replace with your full audio path
    }
    
    # Define durations in seconds
    audio_durations = {
        'short': 2,     # 2 seconds for short version
        'full': 120,    # 1:57 minutes = 117 seconds for full version
    }
    
    # Select the audio path based on the argument
    audio_path = os.path.abspath(audio_paths[audio_type])
    
    # Verify audio file exists
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found: {audio_path}")
        exit(1)
    
    # Get the operating system
    system = platform.system()
    
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] Waiting {interval_minutes} minutes until next play...")
            print(f"Selected audio: {audio_type} version ({audio_durations[audio_type]} seconds)")
            
            # Wait for specified interval
            time.sleep(interval_minutes * 60)
            
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] Playing {audio_type} audio...")
            
            # Play the audio using appropriate command
            play_audio_file(audio_path, system)
            
            # Wait for the exact duration of the audio
            time.sleep(audio_durations[audio_type])
            
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Play an audio file at specified intervals')
    parser.add_argument('-i', '--interval', 
                        type=int, 
                        default=60,
                        help='Time interval between plays in minutes (default: 60)')
    parser.add_argument('-t', '--type',
                        type=str,
                        choices=['short', 'full'],
                        default='full',
                        help='Type of audio to play: short (2 sec) or full (2:10 min) version (default: full)')
    
    # Parse arguments
    args = parser.parse_args()
    
    print(f"Starting audio player - will play {args.type} audio after {args.interval} minutes")
    print(f"Audio duration: {2 if args.type == 'short' else 130} seconds")
    print("Press Ctrl+C to stop the program")
    
    play_audio_at_interval(args.interval, args.type)