import os
import subprocess

# brew install ffmpeg

input_txt = 'links.txt'

def convert_video(source, output):
    command = f'ffmpeg -i "{source}" -bsf:a aac_adtstoasc -c copy -vcodec libx264 -crf 24 {output}'
    return subprocess.run(command,shell=True)

def pop(file):
    with open(file, 'r+') as f:
        firstLine = f.readline()
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()
        return firstLine

counter = 1

while os.stat(input_txt).st_size != 0:
    link_to_m3u8 = pop(input_txt).rstrip()
    output_name = f'video{counter}.mp4'
    result = convert_video(link_to_m3u8, output_name)

    if result.returncode == 0:
        print(f'[{link_to_m3u8}] was processed successfully!')
    else:
        print(f'[{link_to_m3u8}] returned an error...!')

    counter += 1
else:
    print("File empty")