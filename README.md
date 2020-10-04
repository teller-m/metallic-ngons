# Metallic Regular Polygons

<pre>
install required packages: pip install -r requirements.txt

usage: main.py [-h] [--dps DPS] [--buffer BUFFER] [-s] n mean_id

positional arguments:
  n                   # of sides for regular polygon
  mean_id             metallic mean to test for

optional arguments:
  -h, --help          show this help message and exit
  --dps DPS           decimal precision [default: 50]
  --buffer BUFFER     decimal precision buffer [default: 5]
  -s, --show_matches  show matches

examples: py main.py 5 1
          py main.py 8 2
          py main.py 13 3
</pre>
