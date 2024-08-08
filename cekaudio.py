from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('song.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

# Memotong 10 detik pertama
clipped_audio = audio[:10000]  # 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

# Menggabungkan audio asli dengan potongan
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

# Menyimpan audio dalam format WAV
audio.export('result.wav', format='wav')

# Meningkatkan volume sebesar 10 dB
louder_audio = audio + 10  
louder_audio = audio.apply_gain(10)
louder_audio.export('louder_result.mp3', format='mp3')
