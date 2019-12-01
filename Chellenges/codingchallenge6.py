#By: Brennan Link (Six-S)

# This problem was asked by Stripe.
# Write a map implementation with a get function
# that lets you retrieve the value of a key at a particular time.
import sys

class Main():
    def __init__(self):
        print('[INFO] Starting main.')
        #Init our collection, with a special place to store old values.
        self.collection = {
            'history': {} 
        }
    
    #Function that sets values to our global collection for reference later
    #NOTE: We could have used key as time here, but the challenge explicitly
    #references using all args for the set.
    def set(self, key, value, time):
        print('[INFO] Setting values.')
        #Make sure we have everything we need.
        if self.empty(key) and self.empty(value) and self.empty(time):
            #Nothing special if we haven't seen this key before.
            if key not in self.collection:
                self.collection.update({
                    key: {
                        'value': value,
                        'time': time
                    }
                })
            #An extra step is needed if we are setting a new value to the same key.
            else:
                old_values = self.collection[key]
                history_key = str(key) + '-' + str(old_values['time'])

                #Move the old value into our history
                #The key becomes "[key]-[time]"
                self.collection['history'].update({
                    history_key: old_values['value']
                })
                #Set the new value here
                self.collection.update({
                    key: {
                        'value': value,
                        'time': time
                    }
                })
        else:
            print('[WARN] One or more values passed into set are empty.')
            raise Exception('[WARN] A call to "set" is missing one or more arguments.')
    
    #Function that retrieves values from our global collection
    def get(self, key, time):
        print('[INFO] Getting values.')
        #ensure we have everything we need.
        if self.empty(key) and self.empty(time):
            #If the request is for the most recent time set to our value, nothing special
            if time == self.collection[key]["time"]:
                print('[INFO] User requested most recent time.')
                return self.collection[key]['value']
            else:
                #If the user is requesting a previously set value,
                #we need to find it in our history.
                #Check our keys for a matching [key]-[time] pair and return that value.
                print('[INFO] User requested time in the past.')
                for entry in self.collection['history']:
                    split = entry.split('-')
                    if str(key) in split[0] and str(time) in split[1]:
                        value = self.collection['history'][entry]
                        return value
        else:
            print('[WARN] One or more values passed into get are empty.')
            raise Exception('[WARN] A call to "get" is missing one or more arguments.')

    #Utility function to test for empty variables
    def empty(self, value):
        try:
            value = float(value)
        except ValueError:
            pass
        return bool(value)

    def getCollection(self):
        return self.collection


if __name__ in '__main__':

    challenge = Main()

    challenge.set(1, 'test', 4)
    challenge.set(1, 'test2', 6)
    challenge.set(2, 'testing', 7)
    challenge.set(1, 'test3', 7)
    challenge.set(2, 'testing2', 9)
    print(challenge.getCollection())
    print(challenge.get(1, 4))
    print(challenge.get(1, 7))
    print(challenge.get(2, 7))
