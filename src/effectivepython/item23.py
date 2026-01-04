"""
Accept Functions for simple interfaces instead of classes
"""

"""
Simplest example
- A hook is usually a callable passed in or registered and then invoked at the right moment
"""

def process(data, hook = None):
    if hook:
        hook("before", data)
    
    result = data * 2

    if hook:
        hook("after", result)
    
    return result
    

def my_hook(stage, value):
    print(f"[HOOK] {stage}: {value}")

process(data = 10, hook=my_hook)


names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key = lambda x: len(x))
print(names)


from collections import defaultdict
def log_missing():
    print("Key added")
    return 0 

current = {'green':12, 'blue':3}
increments = {
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
}

result = defaultdict(log_missing, current)
print("Before: ", result)
