# 1  Array, Matrix, Dataframe

## 1.1  Array

1. [Python String Manipulation Examples](https://fanwangecon.github.io/pyfan/vig/amto/array/htmlpdfr/fp_ary_string.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array//fp_ary_string.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array/htmlpdfr/fp_ary_string.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/array/htmlpdfr/fp_ary_string.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/amto/array/htmlpdfr/fp_ary_string.html)
	+ Search for substring, replace string, wrap string.
	+ **py**: *zip() + upper()*
	+ **textwrap**: *fill(st, width = 20)*

## 1.2  Dictionary

1. [Python Dictionary Exampls and Usages](https://fanwangecon.github.io/pyfan/vig/amto/dict/htmlpdfr/fp_dict.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict//fp_dict.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict/htmlpdfr/fp_dict.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/amto/dict/htmlpdfr/fp_dict.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/amto/dict/htmlpdfr/fp_dict.html)
	+ List comprehension with dictionary
	+ **py**: *dc = {'key': "name", 'val': 1}*

# 2  Tables and Graphs

## 2.1  Matplotlib Base Plots

1. [Mabplotlib Scatter and Line Plots](https://fanwangecon.github.io/pyfan/vig/tabgraph/baseplot/htmlpdfr/fp_plot_base.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/tabgraph/baseplot//fp_plot_base.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/tabgraph/baseplot/htmlpdfr/fp_plot_base.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/tabgraph/baseplot/htmlpdfr/fp_plot_base.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/tabgraph/baseplot/htmlpdfr/fp_plot_base.html)
	+ Plot several arrays of data, grid, figure title, and line and point patterns and colors.
	+ Plot out random walk and white noise first-order autoregressive processes.
	+ **matplotlib**: *subplots() + ax.plot() + ax.legend() + ylabel() + xlabel() + title() + grid() + show()*
	+ **numpy**: *random.normal() + random.seed() + cumsum() + arange()*
2. [Mabplotlib Text Plots](https://fanwangecon.github.io/pyfan/vig/tabgraph/baseplot/htmlpdfr/fp_plot_text.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/tabgraph/baseplot//fp_plot_text.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/tabgraph/baseplot/htmlpdfr/fp_plot_text.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/tabgraph/baseplot/htmlpdfr/fp_plot_text.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/tabgraph/baseplot/htmlpdfr/fp_plot_text.html)
	+ Print text as figure.
	+ **matplotlib**: *ax.text()*
	+ **textwrap**: *fill()*
	+ **json**: *dump()*

# 3  Get Data

## 3.1  Environmental Data

1. [CDS ECMWF Global Enviornmental Data Download](https://fanwangecon.github.io/pyfan/vig/getdata/envir/htmlpdfr/fs_ecmwf.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/getdata/envir//fs_ecmwf.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/getdata/envir/htmlpdfr/fs_ecmwf.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/getdata/envir/htmlpdfr/fs_ecmwf.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/getdata/envir/htmlpdfr/fs_ecmwf.html)
	+ Using Python API get get ECMWF ERA5 data.

# 4  System and Support

## 4.1  Command Line

1. [Run Python from Command Line Examples](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_command.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system//fp_command.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_command.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_command.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_command.html)
	+ Run python functions from command line.
2. [Run Matlab Command Line Operations](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_matlab.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system//fp_matlab.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_matlab.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/system/htmlpdfr/fp_matlab.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/system/htmlpdfr/fp_matlab.html)
	+ Generate a matlab script and run the script with parameters.
	+ **subprocess**: *cmd = Popen(ls_str, stdin=PIPE, stdout=PIPE, stderr=PIPE) + cmd.communicate()*
	+ **decode**: *decode('utf-8')*
	+ **os**: *chdir() + getcdw()*

## 4.2  File In and Out

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

## 4.3  Install Python

1. [Basic Conda Setup Instructions](https://fanwangecon.github.io/pyfan/vig/support/install/htmlpdfr/fs_install_basics.html): [**rmd**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/install//fs_install_basics.Rmd) \| [**r**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/install/htmlpdfr/fs_install_basics.R) \| [**pdf**](https://github.com/FanWangEcon/pyfan/blob/master/vig/support/install/htmlpdfr/fs_install_basics.pdf) \| [**html**](https://fanwangecon.github.io/pyfan/vig/support/install/htmlpdfr/fs_install_basics.html)
	+ Conda and git installations
	+ **bash**: *where*
