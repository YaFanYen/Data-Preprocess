# Data-Preprocess

## ffmpeg

convert the file of .mp4 into .wav with sampling rate 8000

`python ffmpeg.py`

## split

split data into train / validation / test

`python split.py`


## split_2

For data type in 
    sample1>mix     sample2>mix     ...     samplen>mix
            spk1            spk1                    spk1
            spk2            spk2                    spk2

split data into mix / spk1 / spk2

`python split_2.py`
