[![HitCount](http://hits.dwyl.io/fanwangecon/pyfan.svg)](https://github.com/FanWangEcon/pyfan)  [![Star](https://img.shields.io/github/stars/fanwangecon/pyfan?style=social)](https://github.com/FanWangEcon/pyfan/stargazers) [![Fork](https://img.shields.io/github/forks/fanwangecon/pyfan?style=social)](https://github.com/FanWangEcon/pyfan/network/members) [![Star](https://img.shields.io/github/watchers/fanwangecon/pyfan?style=social)](https://github.com/FanWangEcon/pyfan/watchers)

This is a work-in-progress [website](https://fanwangecon.github.io/pyfan/) consisting of python tutorials and examples for various research tasks. Book version: [bookdown site](https://fanwangecon.github.io/pyfan/bookdown) and [bookdown pdf](https://fanwangecon.github.io/pyfan/bookdown/A-Collection-of-Python-Examples.pdf). The associated python package's functions are not documented here, but shown here [docs](https://pyfan.readthedocs.io/en/latest/autoapi/pyfan/index.html#module-pyfan).

Files are written with [RMD](https://rmarkdown.rstudio.com/). Materials are gathered from various [projects](https://fanwangecon.github.io/research) in which python code is used for research and paper-administrative tasks. Files are from [**Fan**](https://fanwangecon.github.io/)'s [pyfan](https://github.com/FanWangEcon/pyfan) repository which has an associated [package](https://pypi.org/project/pyfan/). The package functionalize various tasks tested out in the Rmd files. In addition, the [pyecon](https://github.com/FanWangEcon/pyecon) repository and the associated [package](https://pypi.org/project/pyecon/) contain functions and rmd files related explicitly to solving economic models. Bullet points show which python packages/functions are used to achieve various objectives.

From [Fan](https://fanwangecon.github.io/)'s other repositories: For dynamic borrowing and savings problems, see [Dynamic Asset Repository (Matlab)](https://fanwangecon.github.io/CodeDynaAsset/); For code examples, see also [Matlab Example Code](https://fanwangecon.github.io/M4Econ/),  [R Example Code](https://fanwangecon.github.io/R4Econ/), and [Stata Example Code](https://fanwangecon.github.io/Stata4Econ/); For intro econ with Matlab, see [Intro Mathematics for Economists](https://fanwangecon.github.io/Math4Econ/), and for intro stat with R, see [Intro Statistics for Undergraduates](https://fanwangecon.github.io/Stat4Econ/). See [here](https://github.com/FanWangEcon) for all of [Fan](https://fanwangecon.github.io/)'s public repositories.

Please contact [FanWangEcon](https://fanwangecon.github.io/) for issues or problems.

[![](https://img.shields.io/github/last-commit/fanwangecon/pyfan)](https://github.com/FanWangEcon/pyfan/commits/master) [![](https://img.shields.io/github/commit-activity/m/fanwangecon/pyfan)](https://github.com/FanWangEcon/pyfan/graphs/commit-activity) [![](https://img.shields.io/github/issues/fanwangecon/pyfan)](https://github.com/FanWangEcon/pyfan/issues) [![](https://img.shields.io/github/issues-pr/fanwangecon/pyfan)](https://github.com/FanWangEcon/pyfan/pulls)

# 1  Array, Matrix, Dataframe

## 1.1  Array

1. [Python String Manipulation Examples](https://fanwangecon.github.io/pyfan/vig/amto/array/htmlpdfr/fp_ary_string.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array//fp_ary_string.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array/htmlpdfr/fp_ary_string.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array/htmlpdfr/fp_ary_string.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/amto/array/htmlpdfr/fp_ary_string.html)
	+ Various string manipulations
	+ **py**: *zip()*

## 1.2  Dictionary

1. [Python Dictionary Exampls and Usages](https://fanwangecon.github.io/pyfan/vig/amto/dict/htmlpdfr/fp_dict.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict//fp_dict.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict/htmlpdfr/fp_dict.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict/htmlpdfr/fp_dict.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/amto/dict/htmlpdfr/fp_dict.html)
	+ List comprehension with dictionary
	+ **py**: *dc = {'key': "name", 'val': 1}*

# 2  Get Data

## 2.1  Environmental Data

1. [CDS ECMWF Global Enviornmental Data Download](https://fanwangecon.github.io/pyfan/vig/getdata/envir/htmlpdfr/fs_ecmwf.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/getdata/envir//fs_ecmwf.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/getdata/envir/htmlpdfr/fs_ecmwf.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/getdata/envir/htmlpdfr/fs_ecmwf.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/getdata/envir/htmlpdfr/fs_ecmwf.html)
	+ Using Python API get get ECMWF ERA5 data.

# 3  System and Support

## 3.1  Command Line

1. [Run Python from Command Line Examples](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_command.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system//fp_command.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_command.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_command.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_command.html)
	+ Run python functions from command line.
2. [Run Matlab Command Line Operations](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_matlab.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system//fp_matlab.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_matlab.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_matlab.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_matlab.html)
	+ Generate a matlab script and run the script with parameters.
	+ **subprocess**: *cmd = Popen(ls_str, stdin=PIPE, stdout=PIPE, stderr=PIPE) + cmd.communicate()*
	+ **decode**: *decode('utf-8')*
	+ **os**: *chdir() + getcdw()*

## 3.2  File In and Out

1. [Python Reading and Writing to File Examples](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_files.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout//fp_files.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_files.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/inout/htmlpdfr/fp_files.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/inout/htmlpdfr/fp_files.html)
	+ Reading from file and replace strings in file.
	+ Convert text file to latex using pandoc and clean.
	+ Search for files in several folders with file substring.
	+ Get path root, file name, file stem, etc from path.
	+ **py**: *open() + write() + replace() + [c for b in [[1,2],[2,3]] for c in b]*
	+ **subprocess**: *call()*
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

## 3.3  Install Python

1. [Basic Conda Setup Instructions](https://fanwangecon.github.io/pyfan/vig/support/install/htmlpdfr/fs_install_basics.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/install//fs_install_basics.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/install/htmlpdfr/fs_install_basics.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/install/htmlpdfr/fs_install_basics.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/install/htmlpdfr/fs_install_basics.html)
	+ Conda and git installations
	+ **bash**: *where*

----
Please contact [![](https://img.shields.io/github/followers/fanwangecon?label=FanWangEcon&style=social)](https://github.com/FanWangEcon) [![](https://img.shields.io/twitter/follow/fanwangecon?label=%20&style=social)](https://twitter.com/fanwangecon) for issues or problems.

![RepoSize](https://img.shields.io/github/repo-size/fanwangecon/R4Econ)
![CodeSize](https://img.shields.io/github/languages/code-size/fanwangecon/R4Econ)
![Language](https://img.shields.io/github/languages/top/fanwangecon/R4Econ)
![Release](https://img.shields.io/github/downloads/fanwangecon/R4Econ/total)
![License](https://img.shields.io/github/license/fanwangecon/R4Econ)

