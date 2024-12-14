from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript(vid_id, output_file):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(vid_id)

        full_text = '\n'.join([entry['text'] for entry in transcript])

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(full_text)

        print(f'transcript saved to {output_file}')

    except Exception as e:
        print(f'Error fetching transcript: {e}')

video_id = '1JbfAr-BQjA'
output_file = 'mel robbins ep1.txt'
#save_transcript(video_id, output_file)

with open('m_robbins_ep1_extract.txt', 'r') as file:
    output = ' '.join(line.strip() for line in file)


print(output)

with open('m_robbins_ep1_extract.txt', 'w') as new_file:
    new_file.write(output)