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


#### Example results

[![sim matrix](https://github.com/src-sauce/CCC-Talk-Similarity/blob/master/examples/myplot.png])]

Number|File
---|---
1|Locked_up_science.en.srt
2|Mobile_Censorship_in_Iran.en.srt
3|Dude_you_broke_the_Future.en.srt
4|State_of_the_Onion.en.srt
5|WTFrance.en.srt
6|Tor_onion_services_more_useful_than_you_think.en.srt
7|Transmission_Control_Protocol.en.srt
8|31C3_Keynote.en.srt
9|Why_is_GPG_damn_near_unusable.en.srt
10|State_of_the_Onion.en.srt
11|PUFs_protection_privacy_PRNGs.en.srt
12|formal.en.srt
13|The_Social_Credit_System.en.srt
14|Algorithmic_science_evaluation_and_power_structure_the_...
15|A_look_into_the_Mobile_Messaging_Black_Box.en.srt
16|Organisational_Structures_for_Sustainable_Free_Software_...
17|The_Tor_Network.en.srt
18|Iridium_Update.en.srt
19|What_does_Big_Brother_see_while_he_is_watching.en.srt
20|Ein_Abgrund_von_Landesverrat.en.srt
21|Bootstraping_a_slightly_more_secure_laptop.en.srt
22|The_Rocky_Road_to_TLS_13_and_better_Internet_Encryption...
23|Collect_It_All_Open_Source_Intelligence_OSINT_for_...
24|Hellman_discrete_logs_the_NSA_and_you.en.srt
25|The_Universe_Is_Like_Seriously_Huge.en.srt
26|Internet_of_Fails.en.srt
27|International_exchange_of_tax_information.en.srt
28|Shut_Up_and_Take_My_Money.en.srt
29|Deep_Learning_Blindspots.en.srt
30|Defeating_Not_Petyas_Cryptography.en.srt
31|Switches_Get_Stitches.en.srt
32|Towards_reasonably_trustworthy_x86_laptops.en.srt
33|Beyond_your_cable_modem.en.srt
34|day_exploit_development_for_Cisco_IOS.en.srt
35|Sense_without_sight_a_crash_course_on_BlindNavi...
36|Gone_in_60_Milliseconds.en.srt

