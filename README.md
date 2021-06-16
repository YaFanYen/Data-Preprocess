# Data-Preprocess

## ffmpeg.py

convert the file of .mp4 into .wav with sampling rate 8000

`python ffmpeg.py`

## split.py

split data into train / validation / test

`python split.py`


## split_2.py

For data type in

    sample1>mix     sample2>mix     ...     samplen>mix
            spk1            spk1                    spk1
            spk2            spk2                    spk2

split data into mix / spk1 / spk2

`python split_2.py`


## rm.py

Remove file for file_name>5000

`python rm.py`
