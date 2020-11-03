def search(file_name):
  print("Searching...")
  with open(file_name) as file:
    lines = file.read().split("\n")
    for line in lines:
      print(f"Looked in {line}.")
    print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()


