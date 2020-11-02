from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))

red = my_values.get('red', ['']) [0] or 0
green = my_values.get('green', ['']) [0] or 0
blue = my_values.get('blue', ['']) [0] or 0
opacity = my_values.get('opacity', ['']) [0] or 0

print('Red:    %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)

#other way of writing helper functions
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

#helper function if logic reapeatedly needed
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
#when expressions get complicated its time 
#to consider splitting them into smaller pieces and moving logic into helper functions
