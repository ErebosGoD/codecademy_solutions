love_maybe_lines = ['Always    \n', '     in the middle   of our bloodiest battles ', 'you lay down your arms\t', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []


#for every line, append the line stripped of whitespace
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
#join each line
love_maybe_full = '#'.join(love_maybe_lines_stripped)

print(love_maybe_full)