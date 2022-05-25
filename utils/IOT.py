from utils.TTS import speak
import speech_recognition as sr
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('.\serviceAccount.json')
firebase_admin.initialize_app(cred ,{'databaseURL':'https://smart-home-2f967-default-rtdb.firebaseio.com/'}) 
ref = db.reference('/')
users_ref= ref.child('Smart Home')


"""
Actions => [On , Off , Down , Up , Dim , Open , Close , Medium , Low , High]
Modes   => [Increase , Decrease]
Rooms   => [Living room , Bedroom , Bathroom , Kitchen , Garage , Reception]
Devices => [Light , Heating , Curtain , Window , Door , Fan]
"""


# Ask about a room if the user doesn't mention it
def is_room(result):
    if 'room' not in result['Entities'] :
        speak('What is the room')    
        
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
            audio = recognizer.listen(source)
            ans = recognizer.recognize_google(audio)
            
        room = ans
    else:    
        room = result['Entities']['room']
        
    return room

# Take a result "Entities" and execute an action
# If an action is equal one of those [On , Open , Up]
def device_1(result):
    device = result['Entities']['device']
    room = is_room(result)
    action = result['Entities']['action']

    speak(f"ok,the {device} is {action}")

    return users_ref.update({'{}/{}'.format(room,device): True})

# If an action is equal one of those [Off , Dim , Down , Close]
def device_0(result):
    device = result['Entities']['device']
    room = is_room(result)
    action = result['Entities']['action']

    speak(f"ok,the {device} is {action}")
        
    return users_ref.update({'{}/{}'.format(room,device): False})

# Final function that identifies a device and an action     
def smartHome(result):   
    device = result['Entities']['device']
    action = result['Entities']['action']

    # Map every device to its action function 
    map_0 = {
        'light'   : device_0,
        'fan'     : device_0,
        'window'  : device_0,
        'heating' : device_0,
        'heater'  : device_0, 
        'curtain' : device_0,
        'door'    : users_ref.update({'door':False})
            }  

    map_1 = {
        'light'   : device_1,
        'fan'     : device_1,
        'window'  : device_1,
        'heating' : device_1,
        'heater'  : device_1,
        'curtain' : device_1,
        'door'    : users_ref.update({'door':True})
            } 
    
    
    if action in ['on','up','open']:
        if device in map_1.keys():
            res =  map_1[device](result)
            
    elif action in ['low','medium','high']:
        if 'light' in device:
            res = users_ref.update({f'bedroom/light/mode':{action}})

    elif action in ['off','dim','down','close']:
        if device in map_0.keys():
            res =  map_0[device](result)

    return res
    
    """
            # LIGHT
    if 'light' in device:
            # Light's Mode
        if 'mode' in result['Entities'].keys():
            mode = result['Entities']['mode']
            # Getting value of light's mode 
            value =  users_ref.child('bedroom').child('light').child('mode').get()
            if mode == 'increase':
                pass
            if mode == 'decrease':
                pass
        
        elif action in ['on','up']:
            device_1(result)
        
        elif action == 'medium':
            pass    
        
        elif action in ['off','down']:
            device_0(result)

            # FAN
    elif 'fan' in device:        
        if  action == 'off':
            device_0(result)
        else:
            device_1(result)
            # DOOR
    elif 'door' in device:
        if action == 'open':
            users_ref.update({device:True})
            speak("ok,the door is open")
        else:
            users_ref.update({device: False})
            speak("ok,the door is close")
            # WINDOW
    elif 'window' in device:
        if action == 'open':
            device_1(result)
        else:
            device_0(result)
            # CURTAIN
    elif 'curtain' in device:
        if action == 'open':
            device_1(result)
        else:
            device_0(result)
            # Heating
    elif device in ['heating','heater'] :
        if 'temperature' in result['Entities'].keys():
            return result['Entities']['temperature']
        elif action == 'on':
            device_1(result)
        else:
            device_0(result)
   """ 



