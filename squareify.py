#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python

from PIL import Image
import sys

def main():
  filename = sys.argv[1]
  orig_image = Image.open(filename)
  
  new_size = (max(orig_image.size),) * 2
  new_image = Image.new("RGB", new_size)
  # (new.x-old.x, new.y-old.y)
  box = tuple((n - o) // 2 for n, o in zip(new_size, orig_image.size))
  new_image.paste(orig_image, box)

  new_image.show()

if __name__ == "__main__":
  main()
