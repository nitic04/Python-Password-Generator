import secrets
import string

def genPwd():
  password = ''
  upperLetters = string.ascii_uppercase
  lowerLetters = string.ascii_lowercase
  digits = string.digits
  specialChars = string.punctuation

  pwdLen = int(input('Enter desired password length: '))
  options = [upperLetters, lowerLetters, digits, specialChars]
  optionsPrint = ['uppercase letters', 'lowercase letters', 'digits', 'special characters']
  selection = []
  
  for i in optionsPrint:
    choice = str(input('Include %s' % i + ' (Y/N)? ')).upper()
    if choice == 'Y':
      selection.append(optionsPrint.index(i))

  if len(selection) == 0:
    return ''
  alphabet = ''
  for x in selection:
    alphabet += options[x]

  for i in range(pwdLen):
    password += ''.join(secrets.choice(alphabet))
  print('Generated password:', password)
  return password

def check_pwd_strength(pwd):
  '''
  Criteria:
  - at least 6 characters long, at most 20-characters long
  - at least one lowercase letter, at least one uppercase letter, at least one symbol
  - not have three repeating characters in a row
  '''
  points = 0
  if 6 <= len(pwd) <= 20:
    points += len(pwd) - 6

  for i in pwd:
    if i.isupper():
      points += 1
    elif i.islower():
      points += 1
    elif i in string.digits:
      points += 1
    else:
      points += 1

  if 0 <= points <= 2:
    print('Password Strength: Weak')
  elif 3 <= points <= 4:
    print('Password Strength: Good')
  else:
    print('Password Strength: Strong')

if __name__ == '__main__':
  pwd = genPwd()
  check_pwd_strength(pwd)
