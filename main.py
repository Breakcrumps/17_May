from random import choice

# Remove the encoding part if Linux defaults to UTF-8, as it should.
file = open("cities.txt", encoding="utf-8")

cities = file.readline().split('  ')

used_cities = []

next = choice(cities)
print(next)

used_cities.append(next)

next = next.replace('ь', '')
next = next.replace('ы', '')

while True:
  reply = input().strip()

  if reply not in cities:
    print("Не город России!")
    continue

  if reply[0].lower() != next[-1]:
    print("Неверный ответ!")
    continue

  if reply in used_cities:
    print("Было!")
    continue

  print("Верно!")

  used_cities.append(reply)

  reply = reply.replace('ь', '')
  reply = reply.replace('ы', '')

  good_next_cities = []

  for city in cities:
    if city in used_cities:
      continue

    if city[0].lower() == reply[-1]:
      good_next_cities.append(city)

  next = choice(good_next_cities)
  print(next)

  next = next.replace('ь', '').replace('ы', '')