import random
from utils.TTS import speak


# Greeting 
def greet(result):
    
    responses = ["Hello,thanks for asking", "Good to see you again", "Hi there, how can I help?" , "hey! how can I help you?"]
    
    if result['Intent'] == 'Greeting':
        res = random.choice(responses)
    else:
        return None
        
    return speak(res)

# Goodbye
def goodbye(result):
    
    responses = ["See you!", "Have a nice day", "Bye! Come back again soon."]
    
    if result['Intent'] == 'Goodbye':
        res = random.choice(responses)
    else:
        return None
        
    return speak(res)

# Thanks
def thank(result):
    
    responses = ["Happy to help!", "Any time!", "My pleasure"]

    if result['Intent'] == 'Thanks':
        res = random.choice(responses)
    else:
        return None
        
    return speak(res)