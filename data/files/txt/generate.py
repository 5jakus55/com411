def search(file_name):
  print("Searching...")
  data={}
  with open(file_name) as file:
    section_name= ""
    for line in file:
      if (line.startswith("Section")):
        section_name=(line.split(":")[1].strip())
      else:
        if (section_name in data):
          data[section_name].append(line.strip())
        else:
          data[section_name]=[line.strip()]
  print("...Done!")
  return data

def run():
  data = search("data/files/txt/books.txt")
  with open( "data/files/txt/generated.csv", "w") as file:
    for section,books in data.items():
      file.write(f"{section}, {books}\n")

run()

