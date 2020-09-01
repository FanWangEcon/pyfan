'''
Created on Oct 5, 2013

@author: fan
'''

import numpy as np
import os as os
# from numpy import genfromtxt

import pyfan.util.timer.timer as timerSup


class csvIO():

    # ===========================================================================
    # saveFileDirectory = 'C:/Users/fan/Documents/Dropbox/Programming/Sandbox/numpyCSVOut.csv'
    # dataOut1 = np.arange(0.0,5.0,1)
    # dataOut2 = np.arange(0,10,1)
    # data1, data2 = np.meshgrid(dataOut1, dataOut2)
    # #===========================================================================
    # # print data1
    # # print data2
    # #===========================================================================
    # dataToSave = np.concatenate((data1,data2))
    # #===========================================================================
    # # print 'printing data to be saved'
    # # print dataAll
    # #===========================================================================
    # np.savetxt(saveFileDirectory, dataToSave, delimiter=',')   # X is an array
    # 
    # dataOut = np.loadtxt(saveFileDirectory, delimiter=',')
    # #===========================================================================
    # # print 'printing from loadtxt'
    # # print dataOut
    # #===========================================================================
    # ===========================================================================

    def numerical_parmlist_stringify(self, trueParameters):
        out_str = ''
        for key in trueParameters.keys():
            val = trueParameters[key]
            if (val > 1):
                out_str += str(int(trueParameters[key]))
            else:
                out_str += str(int(trueParameters[key] * 100))
        return out_str

    def createDirectory(self, save_file_directory, addName=''):
        addName = addName.replace('0.', 'p')
        addName = addName.replace('.', 'p')
        addName = addName.replace('\'', '')
        addName = addName.replace(':', '')
        addName = addName.replace(' ', '')
        addName = addName.replace(',', '')
        addName = addName.replace('{', '')
        addName = addName.replace('}', '')
        addName = addName.replace('-', 'n')
        addName = addName.replace(']', '')
        addName = addName.replace('[', '')
        addName = addName.replace('array(p', '')
        addName = addName.replace(')', '')

        fullname = save_file_directory + addName[0:60] + '/'

        if not os.path.exists(fullname):
            try:
                os.makedirs(fullname)
            except FileExistsError:
                print("Tried to concurrently create folders")

        return fullname

    def saveCSV(self, saveFileDirectory, dataToSave, header=''):
        np.savetxt(saveFileDirectory, dataToSave, delimiter=',', header=header)  # X is an array

    def loadCSV(self, saveFileDirectory, unpack=True):
        return np.loadtxt(saveFileDirectory, delimiter=',', unpack=True)
        # return genfromtxt(saveFileDirectory, delimiter=",",unpack=True)

    def loadText(self, saveFileDirectory):
        f = open(saveFileDirectory, 'r')
        fileOut = f.read()
        f.close()
        return fileOut

    def print_data_summary(self, numpy_matrix, numpy_matrix_name, saveFileDirectory=None, \
                           printSummary=True, printFullMatrix=False, saveText=True, printConsole=True,
                           printFullArray=False, precision=None, linewidth=200):

        np.set_printoptions(linewidth=linewidth)

        if (precision != None):
            np.set_printoptions(precision=precision)
        else:
            np.set_printoptions(precision=2)

        np.set_printoptions(suppress=True)
        if (printFullArray == True):
            np.set_printoptions(threshold=np.nan)

        #         print ''
        # =======================================================================
        # try:
        #     print name+'.shape'
        #     print name.shape
        # except:
        #     pass
        # try:
        #     print 'len('+name+'), len('+name+'[0])'
        #     print len(name), len(name[0])
        # except:
        #     pass        
        # =======================================================================

        #         try:

        if (printSummary == True):
            try:
                summary_line = '\n\n' + numpy_matrix_name + '\n' + \
                               numpy_matrix_name + '.shape:' + str(
                    numpy_matrix.shape) + ', np.mean(' + numpy_matrix_name + '):' + str(
                    np.mean(numpy_matrix)) + ', np.sd(' + numpy_matrix_name + '):' + str(np.std(numpy_matrix)) + \
                               '\nmin(' + numpy_matrix_name + '):' + str(
                    min(numpy_matrix)) + ', max(' + numpy_matrix_name + '):' + str(max(numpy_matrix)) + '\n'
                if (saveText == True):
                    self.saveText(saveFileDirectory, str(summary_line), type='a', addTimer=False, lineBreak=False,
                                  doubleBreak=False, printConsole=False)

                if (printConsole == True):
                    print(summary_line)
            except:
                pass
        else:
            pass

        try:
            if (printFullMatrix == True):

                if (saveText == True):
                    np.set_printoptions(precision=precision)
                    self.saveText(saveFileDirectory, '\n\n' + numpy_matrix_name + '\n' + str(numpy_matrix) + '\n',
                                  type='a', addTimer=False, lineBreak=False, doubleBreak=False, printConsole=False)

                if (printConsole == True):
                    print(numpy_matrix_name)
                    np.set_printoptions(precision=precision)
                    print(numpy_matrix)
        except:
            pass

    #         except:
    #             print 'failed to print ', numpy_matrix_name

    def saveText(self, saveFileDirectory, dataToSave, type='w',
                 addTimer=False, lineBreak=True, doubleBreak=False, printConsole=True, precision=None, linewidth=200):

        # ===========================================================================
        # The first argument is a string containing the filename.
        # The second argument is another string containing a few
        # characters describing the way in which the file will be used.
        # mode can be
        # 'r' when the file will only be read,
        # 'w' for only writing (an existing file with the same name will be erased), and
        # 'a' opens the file for appending; any data written to the file is automatically added to the end.
        # 'r+' opens the file for both reading and writing.
        #
        # On Windows, 'b' appended to the mode opens the file in binary mode,
        # so there are also modes like 'rb', 'wb', and 'r+b'.
        # Python on Windows makes a distinction between text and binary files;
        # the end-of-line characters in text files are automatically altered slightly when data is read or written.
        # This behind-the-scenes modification to file data is fine for ASCII text files,
        # Be very careful to use binary mode when reading and writing such files.
        # On Unix, it doesnt hurt to append a 'b' to the mode,
        # so you can use it platform-independently for all binary files.
        # ===========================================================================

        np.set_printoptions(linewidth=linewidth)

        if (precision != None):
            np.set_printoptions(precision=precision)
        else:
            np.set_printoptions(precision=2)

        if (printConsole == True):
            print(dataToSave)

        f = open(saveFileDirectory, type)

        if (addTimer == True):
            current_time = timerSup.getDateTime(timeType=3)
            f.write(current_time + '\n')

        if (doubleBreak == True):
            f.write('\n\n' + str(dataToSave) + '\n')
        elif (lineBreak == True):
            f.write(str(dataToSave) + '\n')
        else:
            f.write(str(dataToSave))

        f.close()
