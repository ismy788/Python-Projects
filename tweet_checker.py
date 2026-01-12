max_char = 140
tweet = input("Enter your tweet: ")
char_count = len(tweet)

if char_count < max_char:
    print(f"That {char_count} character tweet will work!")
else:
    print(f"Your {char_count} character is {char_count - max_char} too long")
