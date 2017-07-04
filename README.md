# Anti-Duplicator

duplicates.py finds duplicate files (names and sizes are equal) in folder

the program is written in Python 3.6

# Use example
```
python duplicates.py valid_folder_path
```
# Output sample:
```
name='bb_test_0002.png' size=58788 path='test\bb_test_0002.png'
name='bb_test_0002.png' size=58788 path='test\bb_test_0001\bb_test_0002.png'
name='bb_test_0002.png' size=58788 path='test\bb_test_0002\bb_test_0002.png'
name='bb_test_0002.png' size=58788 path='test\bb_test_0003\bb_test_0002.png'

name='bb_test_0003.desktop' size=146 path='test\bb_test_0001\bb_test_0003_copy\bb_test_0003.desktop'
name='bb_test_0003.desktop' size=146 path='test\bb_test_0002\bb_test_0003.desktop'
name='bb_test_0003.desktop' size=146 path='test\bb_test_0003\bb_test_0003.desktop'

name='bb_test_0003.png' size=10463 path='test\bb_test_0001\bb_test_0003_copy\bb_test_0003.png'
name='bb_test_0003.png' size=10463 path='test\bb_test_0003\bb_test_0003.png'

name='bb_test_0003.vcf' size=698 path='test\bb_test_0001\bb_test_0003_copy\bb_test_0003.vcf'
name='bb_test_0003.vcf' size=698 path='test\bb_test_0003\bb_test_0003.vcf'

Process finished with exit code 0
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
