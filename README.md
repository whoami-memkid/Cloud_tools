# Cloud_tools

These are my cloud tools that I have created for Cloud related enumeration / Recon.

Cloud Snake is a simple python tool that you feed a wordlist to and it will check AWS S3 buckets with the words in your list. This can be really useful when checking for S3 Buckets. 

This is by no means finished, but it's a start. I will continue to add more functionality to it.

Currently the way to run it is:

./Cloud_snake.py -r \<region\> -w \<wordlist\>

Currently US and EU are the only working regions.
