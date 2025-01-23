import os
import yt_dlp
# https://ffmpeg.org/download.html#build-windows

def download_video(url, output_path=None):
    """
    Download Youtube video por URL usando yt-dlp.

    Args:
        url (str): URL do video do YouTube.
        output_path (str, opcional): Diretório para salvar o video. 
                                     Padrão é o diretório atual.
    """
    # Configurações do yt-dlp para download de video
    ydl_opts = {
        'format': 'best',  # Melhor formato de video disponível
        'outtmpl': os.path.join(output_path or '.', '%(title)s.%(ext)s'),
        'nooverwrites': True,  # Não sobrescrever videos existentes
        'no_warnings': True,  # Não exibir avisos
        'ignoreerrors': True,  # Ignorar erros
    }

    # Cria um objeto yt-dlp e faz o download do video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        # Tenta fazer o download do video e exibe o título
        try:
            info_dict = ydl.extract_info(url, download=True)
            print(f"[DEBUG] Downloaded: {info_dict['title']}")
       
       # Except para tratar erros de download
        except Exception as e:
            print(f"[ERROR] Erro ao fazer o downloading do video: {e}")

def download_playlist(url, output_path=None):
    """
    Download de uma playlist do YouTube usando yt-dlp.

    Args:
        url (str): URL da playlist do YouTube.
        output_path (str, opcional): Diretório para salvar a playlist. 
                                     Padrão é o diretório atual.
    """
    # Configurações do yt-dlp para download de playlist
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_path or '.', '%(playlist_title)s', '%(title)s.%(ext)s'),
        'nooverwrites': True,
        'no_warnings': True,
        'ignoreerrors': True,
    }

    # Criar objeto yt-dlp e fazer download da playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        # Tenta fazer o download do video e exibe o título
        try:
            ydl.download([url])
            print("[DEBUG] Playlist baixada com sucesso!")
        except Exception as e:
            print(f"[DEBUG] Erro ao fazer o downloading da playlist: {e}")

if __name__ == "__main__":
    # Example usage
    video_url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'
    playlist_url = 'https://www.youtube.com/watch?v=lrIwPL6JpeI&list=PLOIXCdhqXKsAnrVIKr9Y3M9B2TPNqawLm'

    # Uncomment and use as needed
    # download_video(video_url)
    download_playlist(playlist_url)
    # You can also specify a custom output path
    # download_video(video_url, output_path='./downloads')