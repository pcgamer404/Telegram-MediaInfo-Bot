# 📦 Telegram MediaInfo Bot

A simple and lightweight Telegram bot to extract and display detailed media information from audio, video, or document files.  
Built using **Pyrogram** and **pymediainfo**, with zero external image or FFmpeg dependencies.

## ✨ Features

- Shows media **duration**, **format**, **file size**
- Extracts **video info**: codec, resolution, framerate, bitrate
- Extracts **audio info**: codec, channels, bitrate, language
- Detects **multiple audio tracks**
- Counts and lists **subtitle tracks and their languages**
- Clean and readable output
- Lightweight, fast, and easy to deploy

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/telegram-mediainfo-bot.git
cd telegram-mediainfo-bot
```

### 2. Install System Dependencies

#### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip mediainfo -y
```

#### Windows

- Install [Python 3.10+](https://www.python.org/)
- Install [MediaInfo CLI](https://mediaarea.net/en/MediaInfo/Download/Windows)

### 3. Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure Bot

Open `bot.py` and replace the following with your actual values:

```python
API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
```

### 5. Run the Bot

```bash
python bot.py
```

## 📝 Example Output

```
📁 File: movie_sample.mkv
⏱️ Duration: 128.04 sec
💾 Size: 9.36 MB
📦 Format: Matroska
📶 Overall Bitrate: 612 kbps

🎞️ Video Track
   • Codec: V_MPEG4/ISO/AVC
   • Resolution: 1280x720
   • Frame Rate: 24.0 fps
   • Bitrate: 500 kbps

🔊 Audio Tracks (1):
   • Codec: A_AAC, Channels: 2, Bitrate: 112 kbps, Language: eng

📜 Subtitles: 1 (Languages: eng)
```

## 📄 License

This project is licensed under the MIT License.

## 🤝 Credits

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [pymediainfo](https://github.com/sbraz/pymediainfo)
- [MediaInfo](https://mediaarea.net/en/MediaInfo)
