# -*- coding: utf-8 -*-

"""
file_utils.py

与文件相关的IO函数库

@author: Jasper Gui
@email: jasper.gui@outlook.com
@date: 2017.12.11

---------------

FUNCTION LIST:
- validate_file(filepath)
"""

import os


def validate_file(filepath):
    if os.path.exists(filepath):
        return True
    else:
        raise ValueError("{} not found!".format(filepath))


def strip_suffix(fname, suffix):
    """
    移除文件名的后缀

    @fname (str): 文件名称
    @suffix (str): 后缀名称
    return (str)
    """

    return fname.replace(".{}".format(suffix), "")


def listdir_advanced(file_dir, suffix, strip=False):
    """
    获取在指定文件夹下所有文件的名称

    @file_dir (str): 文件夹路径
    @suffix (str): 文件类型
    @strip_suffix (bool): 是否去除后缀 默认为True表示去除后缀
    return (list) 文件名称列表
    """
    
    files = [f for f in os.listdir(file_dir) if f.endswith(suffix)]
    files.sort()
    if strip:
        files = [strip_suffix(f, suffix) for f in files]
    return files


class SevenZFileError(py7zlib.ArchiveError):
    pass

class SevenZFile(object):
	"""
	API for processing 7zip files
	"""
    @classmethod
    def is_7zfile(cls, filepath):
        """ Determine if filepath points to a valid 7z archive. """
        is7z = False
        fp = None
        try:
            fp = open(filepath, 'rb')
            archive = py7zlib.Archive7z(fp)
            _ = len(archive.getnames())
            is7z = True
        finally:
            if fp: fp.close()
        return is7z

    def __init__(self, filepath):
    	"""
    	@filepath <str>: path for 7zip file
    	"""
        fp = open(filepath, 'rb')
        self.filepath = filepath
        self.archive = py7zlib.Archive7z(fp)

    def __contains__(self, name):
        return name in self.archive.getnames()
    
    def read_csv(self):
    	"""
    	read csv files included in 7zip archive
    	"""
        lst_files = self.archive.getnames()
        lst_csv_files = [fname for fname in lst_files if fname.split('.')[-1] == 'csv']
        print(lst_csv_files)
        if len(lst_csv_files) == 0:
            print("no csv file to read!")
            return
        else:
            dic_csv_data = {}
            for csv_f in lst_csv_files:
                lines = []
                try:
                    for line in io.StringIO(self.archive.getmember(csv_f).read().decode("utf-8")):
                        line = line.replace("\n", "")
                        line = line.replace("\r", "")
                        lines.append(line)
                except Exception:
                        for line in io.StringIO(self.archive.getmember(csv_f).read().decode("gbk")):
                            line = line.replace("\n", "")
                            line = line.replace("\r", "")
                            lines.append(line)
                dic_csv_data[csv_f] = pd.DataFrame([line.split(',') for line in lines[1:]], columns=lines[0].split(","))
            return dic_csv_data
