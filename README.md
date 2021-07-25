<img src="https://i.imgur.com/AQDHTkR.jpg" align="right" width="180px"/>

# Daily-Chinese

## What is Daily Chinese?
Daily Chinese is a program that emails recipients a Mandarin Chinese word or phrase every day, including pinyin, English translation, and example sentences.

Developed by Evan Yang.

## Example Email
![Banner](https://i.imgur.com/scOIBkA.png)

## Usage
`grabchars.txt`: a list of words and phrases in Mandarin Chinese, separated line by line. \
`parser.py`: scrapes pinyin, English translations, and example sentences from [LINE Dict](https://dict.naver.com/linedict/enzhdict/#/cnen/home). \
`emailtemplates.txt`: a list of formatted daily messages to be sent to users. \
`receiverlist.txt`: a list of emails that messages from `emailtemplates.txt` will be sent to. \
`sendmail.py` sends an email to each address in `receiverlist.txt`.  

## Technology & Resources
Python \
Yagmail \
Selenium \
LINE Dict

**Not affiliated with LINE. The CN-EN dictionary is only used as a tool in this project.*

## Contributing
Contributions are welcomed and encouraged!

## License
[MIT](https://choosealicense.com/licenses/mit/)
