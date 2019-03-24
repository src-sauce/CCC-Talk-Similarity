# CCC-Talk-Similarity
Find similarities in CCC Event Talks. 
Automatically downloading, and analysing the data.
Looking at some stats and see how far I cmoe with a simple model.

## Requirements
Also see requirements.txt

Lang | Version 
:---: | :---: 
Python | 3.6.x

Package name | Version | Stage
:--- | :--- | :---
bs4 | 0.0.1 | download
guess-language-spirit | 0.5.3 | parsing
pysrt | 1.1.1 | parsing
nltk | 1.1.0 | parsing
gensim | 3.5.0 | model
matplotlib | 2.2.3 | all
pandas | 0.23.3 | all
numpy | 1.14.5 | all
scipy | 1.1.0 |

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
Not that nltk.corpus might not include the dictionary.
Fetch it in python console: bashuser$ <code>python3</code>
~~~
import nltk
nltk.download('words')
~~~
Sometimes I get the following SSL cert error.
~~~
[nltk_data] Error loading words: <urlopen error [SSL:
False
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed
[nltk_data]     (_ssl.c:852)>
~~~
Use this fix at [nltk/issues/2158](https://github.com/nltk/nltk/issues/2158).
<code>Python 3.6</code> is you local python directory.
~~~
open ~./Python\ 3.6/Install Certificates.command
~~~ 

#### Parsing Process & Feature Creation
<code>TODO</code>

## Model Output

Feature distribution in three example topic

10|4|17|...
---|---|---|---
attack|certificate|file|...
memory|key|attack|...
address|law|key|...
cache|log|secure|...
social|memory|cache|...
surveillance|search|user|...
key|net|memory|...
instruction|certification|encryption|...
file|address|attacker|...
module|value|input|...

#### Using the model
<code>TODO</code>