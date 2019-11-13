def biggest_guy(num1, num2, num3):
  if num1 > num2 and num1>num3:
    return num1
  elif num2>num1 and num2>num3:
    return num2
  elif num3>num1 and num3>num2:
    return num3

#DO NOT remove lines below here, this is designed to test your code.
def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
  except (AssertionError) as e:
    print(e)
    print("WRONG!!")
    return
  print("SUCCESS!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()