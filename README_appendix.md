# (APPENDIX) Appendix {-}

# Index and Code Links

## Array, Matrix, Dataframe links

### [Section 1.1 Array][Array] links

1. [Python String Manipulation Examples](https://fanwangecon.github.io/pyfan/vig/amto/array/htmlpdfr/fp_ary_string.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array//fp_ary_string.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array/htmlpdfr/fp_ary_string.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array/htmlpdfr/fp_ary_string.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/amto/array/htmlpdfr/fp_ary_string.html)
	+ Various string manipulations
	+ **py**: *zip()*

### [Section 1.2 Dictionary][Dictionary] links

1. [Python Dictionary Exampls and Usages](https://fanwangecon.github.io/pyfan/vig/amto/dict/htmlpdfr/fp_dict.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict//fp_dict.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict/htmlpdfr/fp_dict.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict/htmlpdfr/fp_dict.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/amto/dict/htmlpdfr/fp_dict.html)
	+ List comprehension with dictionary
	+ **py**: *dc = {'key': "name", 'val': 1}*

## System and Support links

### [Section 2.1 File In and Out][File In and Out] links

1. [Python Reading and Writing to File Examples](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_files.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout//fp_files.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_files.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_files.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_files.html)
	+ Reading from file and replace strings in file.
	+ Convert text file to latex using pandoc and clean. 
	+ Search for files in several folders with file substring.
	+ Get path root, file name, file stem, etc from path.
	+ **py**: *open() + write() + replace() + [c for b in [[1,2],[2,3]] for c in b]*
	+ **subprocess**: *read()*
	+ **pathlib**: *Path().rglob() + Path().stem*
	+ **os**: *remove() + listdir() + path.isfile() + path.splitdrive() + os.path.splitext() + os.path.split()*
2. [Python Directory and Folder Operations](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_folders.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout//fp_folders.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_folders.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_folders.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_folders.html)
	+ Generate new folders and files.
	+ Generate subfolder recursively.
	+ Copying and moving files across folders. 
	+ Aggregate subfolders into a folder and move. 
	+ **py**: *open(srt, 'w') + write() + close()*
	+ **os**: *os.listdir()       + os.path.join('/', 'c:', 'fa', 'fb')*
	+ **pathlib**: *Path(srt).mkdir(parents=True, exist_ok=True) + [Path(spn).stem for spn in Path(srt).rglob(st)]*
	+ **shutil**: *shutil.copyfile('/fa/fl.txt', '/fb/fl.txt') + shutil.copy2('/fa/fl.txt', '/fb') + shutil.rmtree('/fb')*
	+ **distutils**: *dir_util.copy_tree('/fa', '/fb')*
3. [Python Yaml File Parsing](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_yaml.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout//fp_yaml.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_yaml.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_yaml.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_yaml.html)
	+ Parse and read yaml files.
	+ **yaml**: *load(fl_yaml, Loader=yaml.BaseLoader)       + dump()*
	+ **pprint**: *pprint.pprint(ls_dict_yml, width=1)*
