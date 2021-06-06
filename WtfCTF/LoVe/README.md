## Lov3

***Unfortunately my assistant deleted some of the files from my flash drive. Can you retrieve them and collect the flag?***


Hyperlink goes to googledrive where we can download a 3.2GB rar archive.

```unrar x  chall3 rar``` 

*extracts Challeng3.E01 file*

```file Challeng3.EO1```

*Challeng3.E01: EWF/Expert Witness/EnCase image file format*
	
```ewfmount Challeng3.E01 /mnt/E01/```


```cd /mnt/E01/ && file * ```

*ewf1: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS    ", sectors/cluster 8, Media descriptor 0xf8, sectors/track 63, heads 255, hidden sectors 2048, dos < 4.0 BootSector (0x0), FAT (1Y bit by descriptor); NTFS, sectors/track 63, physical drive 0x80, sectors 6637567, $MFT start cluster 786432, $MFTMirror start cluster 2, bytes/RecordSegment 2^(-1*246), clusters/index block 1, serial number 0e650706450703cfd; contains bootstrap BOOTMGR*

here we had some tries extracing files by foremost or binwalk. Results were unsatisfied so We have decided to use [RecuperaBit](https://github.com/Lazza/RecuperaBit), a software which attempts to reconstruct file system structures and recover files. Currently it supports only NTFS.

```python3 RecuperaBit/main.py /mnt/E01/ewf1 ```

*INFO:root:4 partitions found.*

files were easily recover in two folder called ```Imazess``` and ```Songzzz```, among them We have found two suspicious files 

```file Imazess/Incognito0.jpg```

*Imazesss/Incognit0.jpg: data*

```file Songzzz/Attention.wav``` 

*Songzzz/Attention.wav: data*

extension and directory name suggests formats so we should check file signature.

```xxd Incognit0.jpg | head -n 2```

*00000000: 4a46 ffe0 0010 6a66 3166 0001 0100 0001  JF....jf1f......
00000010: 0001 0000 ffdb 0043 0002 0101 0101 0102  .......C........* 

magic bytes were corrupted in two of these files. We have repaired it by using ```hexedit```

**Repaired jpg shows half of the flag!**

when it comes to .wav file - repaired file sounds like ```beep beep beep``` my friend suggested that this is DMTF code which can be restored by online tool. After conversion it returns a numer value which can be converted to ASCII and thats the second part of the flag. 










