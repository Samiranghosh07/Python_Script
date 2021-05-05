# Python Package and scripts

#[ Docx file read ] 

>> pip3 install python-docx

# [ Google Translator ]

>> pip3 install gtts
 
>>from gtts import gTTS
#dir(gtts)
audio = gTTS('''Sherlock Holmes (/ˈʃɜːrlɒk ˈhoʊmz/ or /-ˈhoʊlmz/) is a fictional private detective created by British author Sir Arthur Conan Doyle. Referring to himself as a "consulting detective" in the stories, Holmes is known for his proficiency with observation, deduction, forensic science, and logical reasoning that borders on the fantastic, which he employs when investigating cases for a wide variety of clients, including Scotland Yard.''')
>> audio.save('story.mp3')


# [ Domain Availablity check ]

>> pip3 install whois 

>>import whois
#dir(whois)
>>url = "x2y2b2.ga"
>>find_domain = whois.whois(url)
>>find_domain
