free = {}
for _ in range(26):
    text = str(input()).split(", ")
    new_text = text[0].split()
    alpha = new_text[0]
    number = tuple(map(int, (new_text[1] + " " + " ".join(text[1:])).split()))
    free.update({alpha: str(number).replace(",", "") if len(number) > 1 else number[0]})
print(free)