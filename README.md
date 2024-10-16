# SenseiCLI
SenseiCLI is a python script (Sensei.py) that can be used to revise kanji (Chinese characters used in Japanese), specifically the meaning of kanjis. It refers the [Kodansha Kanji Learner's Course](https://www.amazon.com/Kodansha-Kanji-Learners-Course-Step/dp/1568365268). To run the script, simply use:

```
$ python Sensei.py
```

Users can enter the start and end numbers for the range of kanji they want to revise from the book (Kodansha KLC). For example, to revise from Kanji 21 to 30, users can enter these kanji IDs when prompted by the script:

```
Kanji start: 21
Kanji end: 30
```

Then, the script will quiz the user on the specified range of kanjis, in a random order. Firstly, the kanji is displayed. The user recalls the meaning of the kanji (or fails to do so), then presses `Enter` to see the meaning. After that the script asks the user whether they recalled the meaning correctly, to which the user can press `4` or `f` and then press `Enter`, or any other key followed by `Enter` if they failed to recall the meaning correctly.

```
目              (1/10)
1. Eye    2. Item
Correct?: f


明              (2/10)
1. Bright    2. Clear
Correct?: d


土              (3/10)
Soil, land
Correct?: f
```

The keys `4` and `f` were chosen for going through the revision session faster. User can press `f` for correct and `d` for incorrect answer with left hand while pressing `Enter` key with right hand to proceed through the prompts. These key preferences can be changed in `Sensei.py` by editing the `GOTIT_CODES` list:

```Python
GOTIT_CODES = ['4','44','f']
```

The kanji marked as incorrectly recalled by the user will be asked till the user gets it right. Once all the kanji have been marked correct (user entered `f` for all the kanji asked), the script will ask whether a report should be generated or not.
```
Create report? (y/n): y
Date and time: 2024-10-16 10:49:34.204922

Kanji start: 21

Kanji end: 30


Number of Kanji: 10

Correct: 7

Wrong: 3

---------------------
Kanji you got wrong:


22      川 :    River

25      曜 :    Day of the week

26      火 :    Fire




~~~THE END~~~


Thank you for using Sensei CLI

Based on "The Kodansha Kanji Learner's Course" by Andrew Scott Conning, 2013


Created by Sheikh Bilal Ahmad

Date: 16-10-2024


~~~THE END~~~
```

The script will print a summary of the revision session. The report will be text file containing this summary. The name of the report will be the timestamp for the revision session. The report will be available in the same folder as the script.

Lastly, the script stores the info about the revision session in a json file `renshuu.json`.

I made this program because the current flashcard app options weren't doing it for me. I found some issue or the other in using them for kanji meaning revision. In the future, I may make a flashcard app for kanji meaning revision.

Enjoy!