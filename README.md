JARVIS – VOICE CONTROLLED VIRTUAL DESKTOP ASSISTANT


1. About:
JARVIS is a Python-based Voice Controlled Virtual Desktop Assistant. It allows users to control their computer and access online information using simple voice commands instead of keyboard or mouse. The assistant listens through a microphone, understands the spoken command, performs the required task, and replies back using a human-like voice.

This project demonstrates real-world usage of:
• Speech Recognition
• Text-to-Speech
• System Automation
• API Integration
• Modular Python Programming


2. WHY THIS PROJECT?
Using keyboard and mouse for every small task can be slow and repetitive. This project aims to make interaction with a computer faster and hands-free.

The main goals are:
• Automate daily desktop tasks
• Learn voice-based automation in Python
• Understand API usage in real applications


3. HOW DOES JARVIS WORK? (HIGH LEVEL)

JARVIS follows a simple and clear pipeline:

1. The microphone captures the user's voice
2. Speech is converted into text
3. The text command is analyzed
4. The corresponding action is performed
5. The assistant responds using speech

This cycle continues until the user says "quit".


4. CORE FUNCTIONALITIES

VOICE INPUT & OUTPUT

• Uses SpeechRecognition library to convert speech into text
• Uses pyttsx3 library to convert text responses into speech
• Works offline for text-to-speech

WIKIPEDIA SEARCH

When the user asks something related to Wikipedia, JARVIS:
• Searches Wikipedia
• Fetches a short summary
• Reads the result aloud

WEB AUTOMATION

JARVIS can:
• Open Google, YouTube, Facebook, LinkedIn
• Search queries on Google
• Play videos directly on YouTube using voice commands

SYSTEM AUTOMATION

JARVIS can open system applications like:
• Google Chrome
• Calculator
• Notepad
• Command Prompt
These operations are performed using OS-level commands.

WEATHER REPORT

• Detects user's city using IP address
• Fetches live weather data from OpenWeatherMap API
• Speaks temperature, feels-like value, and weather condition

ENTERTAINMENT FEATURES

• Tells random jokes using public APIs
• Gives random motivational advice
• Plays local music files

UTILITY FEATURES

• Announces current system time
• Displays public IP address
• Responds politely to user commands


5. PROJECT STRUCTURE

main.py
→ The heart of the project  
→ Listens to voice commands and decides what action to perform

utils.py
→ Contains predefined assistant replies  
→ Makes interaction sound natural

online_ops.py
→ Handles internet-related tasks like:
   - Google search
   - YouTube playback
   - IP address
   - Jokes & advice APIs

os_ops.py
→ Handles system-level tasks like opening CMD and applications

weather_rep.py
→ Fetches and formats live weather information

wa.py
→ WhatsApp automation module (optional feature)

openaiTest.py
→ Experiment file for OpenAI API usage

tempCodeRunnerFile.py
→ Temporary testing file


6. EXAMPLE VOICE COMMANDS

• "Search Python on Wikipedia"
• "Open Chrome"
• "Play music"
• "Search AI on Google"
• "Weather report"
• "Tell me a joke"
• "Give me advice"
• "What is the time"
• "Open calculator"
• "Quit"


7. HOW TO RUN THE PROJECT

Step 1: Clone the repository  
Step 2: Install required Python libraries  
Step 3: Ensure microphone access is enabled  
Step 4: Run the main file  

Command:
python main.py


8. SYSTEM REQUIREMENTS

• Windows OS
• Python 3.x
• Microphone
• Internet connection (for APIs)


9. LIMITATIONS

• Works best in quiet environments
• Limited natural language understanding
• Internet required for some features
• Platform dependent (Windows)


10. FUTURE IMPROVEMENTS

• AI-powered conversation engine
• Wake word detection (Hey Jarvis)
• Graphical user interface (GUI)
• Email and WhatsApp automation
• Cross-platform support


11. WHO SHOULD USE THIS PROJECT?

• Students learning Python automation
• Beginners exploring voice assistants
• Anyone interested in desktop automation
• Recruiters reviewing practical projects


12. CONCLUSION

This project is a complete example of how Python can be used to build a real, useful, and interactive desktop application using voice commands. It focuses on clarity, modular design, and real-world APIs.


AUTHOR

Name : Abhishek Kumar  
Project Type : Python Automation / Virtual Assistant  

