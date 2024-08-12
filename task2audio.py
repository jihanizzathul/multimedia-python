from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        if len(audio) > 10000:
            clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
            clipped_audio.export('clipped2_' + output_path, format='mp3')
            print("✅ Pemotongan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        # Operasi Penggabungan dengan validasi durasi
        combined_audio = audio + clipped_audio
        combined_audio.export('combined2_' + output_path, format='mp3')
        print("✅ Penggabungan berhasil")

        # Operasi Konversi Format
        audio.export('hasil.wav', format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pengaturan Volume dengan validasi
        if audio.dBFS < -10:  
            louder_audio = audio + 10  
            louder_audio.export('louder2_' + output_path, format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            print("✅ Volume audio sudah memadai, tidak perlu penyesuaian")

        # Operasi Pemutaran Audio
        if 'louder_audio' in locals():
            print("🔊 Memutar audio hasil manipulasi...")
            play(louder_audio)
        else:
            print("🔊 Tidak ada audio yang diputar.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('song.mp3', 'hasil.mp3')
