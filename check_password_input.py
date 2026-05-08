def CodelandUsernameValidation(strParam):

  length_of_username = len(strParam)
  if length_of_username < 4 or length_of_username > 25:
    return "false"

  # https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python
  if not strParam[0].isalpha():
    return "false"

  for ch in strParam:
    if not (ch == '_' or ch.isalnum()):
      return "false"

  if strParam[-1] == "_":
    return "false"

  return "true"

# keep this function call here
print(CodelandUsernameValidation(input()))