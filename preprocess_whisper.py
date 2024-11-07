import argparse
import os
from pydub import AudioSegment 
from pydub.utils import make_chunks


def get_args():
    parser = argparse.ArgumentParser("Preprocess for Whisper")
    parser.add_argument('--path', default='./hy/hy', help='Path to directory containing audio documents to be preprocessed')
    return parser.parse_args()

def splitting(path , filename):
    audio = AudioSegment.from_file(f'{path[2:]}/{filename}', "wav")
    chunk_length_ms = 30000
    chunks = make_chunks(audio, chunk_length_ms)

    for i, chunk in enumerate(chunks): 
        chunk_name = f'{path}/chunked/' + filename[:-4] + "_{0}.wav".format(i) 
        print ("exporting", chunk_name) 
        chunk.export(chunk_name, format="wav") 


def main(args):
    path = args.path
    all_file_names = os.listdir(path)
    try:
        os.makedirs(f'{path}/chunked') # creating a folder named chunked
    except:
        pass
    for each_file in all_file_names:
        if ('.wav' in each_file):
            splitting(path, each_file)


if __name__ == '__main__':
    args = get_args()
    main(args)

