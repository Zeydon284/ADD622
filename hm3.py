from itertools import count


text = """Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели."""
print(text)


b = [word for word in text.split() if word.startswith("е") or word.startswith("Е")]

print()
print("Количество слов:",len(b))






