import secrets
import string

def genPwd():
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
      
  alphabet = ''
  for x in selection:
    alphabet += options[x]

  password = ''
  for i in range(pwdLen):
    password += ''.join(secrets.choice(alphabet))
  print('Generated password:', password)

if __name__ == '__main__':
  genPwd()
