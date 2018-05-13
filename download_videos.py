import requests

tfrecords_shared_links = "flyingshapes_videos.txt"


with open(tfrecords_shared_links, 'r') as link_file:
  url_list = link_file.read().splitlines()

  for i, link in enumerate(url_list):
    file_name = "videos_" + str(i+1) + ".zip"
    r = requests.get(link, stream=True)
    print("Downloading", file_name)
    with open(file_name, 'wb') as f:
      dl = 0
      for chunk in r.iter_content(chunk_size=1024):
        if chunk:
          dl += len(chunk)
          f.write(chunk)
          f.flush()
    print("Downloading", file_name, "completed")







