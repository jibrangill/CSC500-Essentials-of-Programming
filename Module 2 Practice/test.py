import array as arr

guest_list = arr.array('u', ['R', 'A', 'R', 'A', 'o', 'G', 'e', 'C', 'k', 'l'])

add_guest = input('Would you like to add someone to the guest list? Y/N: ')

while add_guest == 'Y':

   new_guest = input('What is their name? ')

   guest_list.append(new_guest)

   add_guest = input('Add another guest? Y/N: ')

# We can also search for guests on the list

search_guest = input('Would you like to check if someone is on the guest list? Y/N: ')

while search_guest == 'Y':

   potential_guest = input('What is their name? ')

   try:

      guest_list.index(potential_guest)

      print('Guest is on list')

   except ValueError:

      print('Guest is not on the list')

   search_guest = input('Look for another person? Y/N: ')