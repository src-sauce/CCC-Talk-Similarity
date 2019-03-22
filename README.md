# CCC-Talk-Similarity
Find similarities in CCC Event Talks. 
Automatically downloading, and analysing the data.
Looking at some stats and see how far I cmoe with a simple model.

## Requirements
Also see requirements.txt

Package name | Version
:--- | :---
guess-language-spirit | 0.5.3
matplotlib | 2.2.3
pysrt | 1.1.1
gensim | 3.5.0
pandas | 0.23.3
numpy | 1.14.5
scipy | 1.1.0
bs4 | 0.0.1

## Download Data
The config notes url and directory, to get the data from and where to put it.
~~~
DownloadData
    subtitles
    config.json
    download.py
    path_structure.json
~~~
To get <code>subtitles</code> directory, do:
~~~
python3 download.py
~~~
In <code>subtitles</code>

~~~
subtitles
    30C3
    31C3
        31c3-6021-en-de-Why_is_GPG_damn_near_unusable.en.srt
        31c3-6112-en-de-Tor_Hidden_Services_and_Deanonymisation.en.srt
        31c3-6123-en-de-Freedom_in_your_computer_and_in_the_net.es.srt
        31c3-6196-en-Switches_Get_Stitches.en.srt
        31c3-6251-en-de-State_of_the_Onion.en.srt
        31c3-6258-en-Reconstructing_narratives.en.srt
        31c3-6264-de-en-Wir_beteiligen_uns_aktiv_an_den_Diskussionen.de.srt
        ...
~~~
Ok now there is some data. (~31.7MB)

## Parsing and Features
<code>TODO<code/>
