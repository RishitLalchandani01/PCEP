answer_a = input('Do you like travelling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')

# keep in mind how indentation is key


#rishit's example:
birthday_list=[]
try:
  month=int(input("What is your birthday month (1-12): "))
  if month == 1:
    birthday_list.append(month)
    print("Me too!")
    day=int(input("What is your birthday day (1-31): "))
    if day==14:
      birthday_list.append(day)
      print("Me too!")
      year=int(input("What is your birthday year (1800-2025): "))
      if year==2010:
        birthday_list.append(year)
        print("Me too!")
        print("Looks like we have the same birthday!")
        print(birthday_list)
      else:
        print("look's like we don't have the same birthday!")
    else:
      print("look's like we don't have the same birthday!")
  else:
    print("look's like we don't have the same birthday!")
  
  print("end of program!")
except ValueError:
  print("Provide a number next time, bye!")
