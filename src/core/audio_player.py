"""
音频播放模块
"""

import pygame
import threading

# 初始化混音器
pygame.mixer.init()

_play_lock = threading.Lock()


def play(audio_path: str):
    """播放指定音频文件，支持MP3和WAV"""
    with _play_lock:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()


def pause():
    """暂停当前播放"""
    with _play_lock:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()


def resume():
    """恢复播放"""
    with _play_lock:
        pygame.mixer.music.unpause()


def stop():
    """停止播放"""
    with _play_lock:
        pygame.mixer.music.stop()
