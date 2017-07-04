# Anti-Duplicator

duplicates.py finds duplicate files (names and sizes are equal) in folder

the program is written in Python 3.6

# Use example
```
python duplicates.py valid_folder_path
```
# Output sample:
```
file='test\bb_test_0002.png' (58788 bytes)
file='test\bb_test_0001\bb_test_0002.png' (58788 bytes)
file='test\bb_test_0002\bb_test_0002.png' (58788 bytes)
file='test\bb_test_0003\bb_test_0002.png' (58788 bytes)

file='test\bb_test_0001\bb_test_0003_copy\bb_test_0003.desktop' (146 bytes)
file='test\bb_test_0002\bb_test_0003.desktop' (146 bytes)
file='test\bb_test_0003\bb_test_0003.desktop' (146 bytes)

file='test\bb_test_0001\bb_test_0003_copy\bb_test_0003.png' (10463 bytes)
file='test\bb_test_0003\bb_test_0003.png' (10463 bytes)

file='test\bb_test_0001\bb_test_0003_copy\bb_test_0003.vcf' (698 bytes)
file='test\bb_test_0003\bb_test_0003.vcf' (698 bytes)

Process finished with exit code 0
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
