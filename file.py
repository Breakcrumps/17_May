# Remove the encoding part if Linux defaults to UTF-8, as it should.
with open("txt-cities-russia.txt", encoding="utf-8") as source:
  with open("cities.txt", 'w', encoding="utf-8") as destination:
    cities = "".join(source.read().replace('\n', '  '))
    print(cities, file=destination)