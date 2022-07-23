# License Plate Recognition

License plate recognition

**Install requirements**
```
pip install -r requirements.txt
```


**Detect**
The plates detected are located in datset/plates/

```
python detection/handcrafted/Detect.py
```

**Recognition**
*Training*

```
python recognition/character_based/train_plate_recognition.py
or
python recognition/segment_based/train_character_recognition.py
```

**Evaluate**

```
python recognition/character_based/evaluate.py
or
python recognition/segment_based/evaluate.py
```

**The all steps are shown in *visual.ipynb*. An end-to-end ALPR system: *end2end_recognition.ipynb* (Should put image file in test_img/). The streamlit demo**
```
https://thanhlam104-lpr-streamlit-app-ot6pyc.streamlitapp.com/
```

