import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pymediainfo import MediaInfo

API_ID = 123456     # Replace with your API ID
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("enhanced_mediainfo_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document | filters.video | filters.audio)
async def media_info_handler(client, message: Message):
    sent = await message.reply_text("📥 Downloading media...")

    file_path = await message.download()
    media_info = MediaInfo.parse(file_path)

    output = ""
    audio_count = 0
    subtitle_count = 0
    audio_tracks = []
    subtitle_languages = []

    for track in media_info.tracks:
        if track.track_type == "General":
            output += f"📁 **File:** {track.file_name}\n"
            if track.duration:
                output += f"⏱️ **Duration:** {track.duration / 1000:.2f} sec\n"
            if track.file_size:
                output += f"💾 **Size:** {int(track.file_size) / (1024 * 1024):.2f} MB\n"
            if track.format:
                output += f"📦 **Format:** {track.format}\n"
            if track.overall_bit_rate:
                output += f"📶 **Overall Bitrate:** {int(track.overall_bit_rate) / 1000} kbps\n"

        elif track.track_type == "Video":
            output += "\n🎞️ **Video Track**\n"
            if track.codec_id:
                output += f"   • Codec: {track.codec_id}\n"
            if track.width and track.height:
                output += f"   • Resolution: {track.width}x{track.height}\n"
            if track.frame_rate:
                output += f"   • Frame Rate: {track.frame_rate} fps\n"
            if track.bit_rate:
                output += f"   • Bitrate: {int(track.bit_rate) / 1000} kbps\n"

        elif track.track_type == "Audio":
            audio_count += 1
            track_info = []
            if track.codec_id:
                track_info.append(f"Codec: {track.codec_id}")
            if track.channel_s:
                track_info.append(f"Channels: {track.channel_s}")
            if track.bit_rate:
                track_info.append(f"Bitrate: {int(track.bit_rate) / 1000} kbps")
            if track.language:
                track_info.append(f"Language: {track.language}")
            audio_tracks.append("   • " + ", ".join(track_info))

        elif track.track_type == "Text":
            subtitle_count += 1
            if track.language:
                subtitle_languages.append(track.language)

    if audio_tracks:
        output += f"\n🔊 **Audio Tracks** ({audio_count}):\n" + "\n".join(audio_tracks)

    if subtitle_count:
        output += f"\n📜 **Subtitles:** {subtitle_count}"
        if subtitle_languages:
            output += " (Languages: " + ", ".join(subtitle_languages) + ")"

    await sent.edit_text(output or "❌ Could not extract media information.")
    os.remove(file_path)

@app.on_message(filters.command("start"))
async def start_message(client, message: Message):
    await message.reply_text("👋 Send me a media file and I’ll show you detailed info about it!")

if __name__ == "__main__":
    print("✅ Bot has started.")
    app.run()
