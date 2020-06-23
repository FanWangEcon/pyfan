'''
Created on Sep 24, 2013

@author: fan
'''
"""
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2, 0))
ax5 = plt.subplot2grid((3,3), (2, 1))
"""

import logging

logger = logging.getLogger(__name__)

import matplotlib

# matplotlib.use('Agg')

# matplotlib.use('qt5agg')
# import matplotlib.pyplot as pylab
import pylab as pylab
# import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
# from matplotlib.mlab import griddata
import mpl_toolkits.mplot3d.axes3d as p3
import itertools
from matplotlib.patches import Polygon
from matplotlib import cm

import seaborn as sns


# ===============================================================================
# pylab.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# pylab.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
# ===============================================================================

def contourAnd3D(xData, yData, zData,
                 xLabStr, yLabStr, zLabStr,
                 graphTitleDisp, graphTitleSave,
                 savedpi=125, angleType=[1, [1, 2, 3]],
                 drawContour=False, draw3D=True,
                 draw3DSurf=False,
                 contourXres=100, contourYres=100,
                 s=20, alpha=0.6,
                 subplot=None, fig=None):
    if (fig == None):
        fig = pylab.figure()

    '''
    Contour
    '''
    if (drawContour == True):
        try:
            pylab.clf()
            if (subplot is not None):
                pylab.subplot(subplot['rows'], subplot['cols'], subplot['cur'])
            xN, yN, zN = grid(xData, yData, zData, resX=contourXres, resY=contourYres)
            pylab.contour(xN, yN, zN)
            pylab.xlabel(xLabStr)
            pylab.ylabel(yLabStr)
            pylab.title(graphTitleDisp)
            pylab.grid()
            # pylab.show()
            pylab.savefig(graphTitleSave + '_contour', dpi=savedpi, papertype='a1')
        except:
            pass

    '''
    3D
    '''
    if (draw3D == True):
        try:
            pylab.clf()
            if (subplot is not None):
                pylab.subplot(subplot['rows'], subplot['cols'], subplot['cur'])
            ax = p3.Axes3D(fig)
            ax.scatter3D(xData, yData, zData, marker='o', s=s, c=np.ravel(zData), alpha=alpha)
            tripleAngle3dSave(ax, graphTitleDisp, xLabStr, yLabStr, zLabStr, graphTitleSave + '_3D', savedpi=savedpi,
                              angleType=angleType)
        except:
            pass

    if (draw3DSurf == True):
        try:
            #             pylab.clf()
            if (subplot is not None):
                ax = fig.add_subplot(subplot['rows'], subplot['cols'], subplot['cur'], projection='3d')
            else:
                ax = p3.Axes3D(fig)
            ax.plot_surface(xData, yData, zData, cmap=cm.coolwarm, linewidth=0, antialiased=False)
            tripleAngle3dSave(ax, graphTitleDisp, xLabStr, yLabStr, zLabStr, graphTitleSave + '_3DS', savedpi=savedpi,
                              angleType=angleType)
        except:
            pass

    return fig


#     pylab.close(fig)

"""
angleType: [1, [1, 2, 3]]
    this menas
"""


def tripleAngle3dSave(ax, graphTitleDisp, xLabStr, yLabStr, zLabStr, graphTitleSave, savedpi=125,
                      angleType=[1, [1, 2, 3]]):
    ax.set_title(graphTitleDisp)
    # pylab.show()
    # for graphICur in [1, 2, 3]:
    for graphICur in angleType[1]:
        ax.set_xlabel(xLabStr)
        ax.set_ylabel(yLabStr)
        ax.set_zlabel(zLabStr)
        if (angleType[0] == 1):
            if (graphICur == 1):
                ax.view_init(elev=0, azim=-180)
                ax.set_xlabel('')
            if (graphICur == 2):
                ax.view_init(elev=0, azim=-90)
                ax.set_ylabel('')
            if (graphICur == 3):
                ax.view_init(elev=90, azim=-90)
                ax.set_zlabel('')
            if (graphICur == 4):
                ax.view_init(elev=-90, azim=0)
                ax.set_ylabel('')
            if (graphICur == 5):
                ax.view_init(elev=0, azim=-145)
                ax.set_ylabel('')
            if (graphICur == 6):
                ax.view_init(elev=22., azim=-115)
                ax.set_ylabel('')
        if (angleType[0] == 2):
            if (graphICur == 1):
                ax.view_init(elev=-90, azim=0)
            if (graphICur == 2):
                ax.view_init(elev=0, azim=-145)
        if (angleType[0] == 3):
            if (graphICur == 1):
                ax.view_init(elev=22., azim=-115)

        pylab.savefig(graphTitleSave + str(graphICur), dpi=savedpi, papertype='a1')

    # ===========================================================================
    #
    # angleColl_elevAndAzim_set1 = [[90,-90],[0,-180],[0,-90]]
    # angleColl_elevAndAzim_set2 = [[-90,0],[0,-145]]
    # angleColl_elevAndAzim = [angleColl_elevAndAzim_set1,angleColl_elevAndAzim_set2]
    #
    # if (angleColl_elevAndAzim[0] == 1):
    #     ax.set_title(graphTitleDisp)
    #     # pylab.show()
    #     #for graphICur in [1, 2, 3]:
    #     for graphICur in angleType[1]:
    #         ax.set_xlabel(xLabStr)
    #         ax.set_ylabel(yLabStr)
    #         ax.set_zlabel(zLabStr)
    #         (curElev,curAxzim) = angleColl_elevAndAzim[angleType[0]][graphICur]
    #         ax.view_init(elev=curElev, azim=curAxzim)
    #         if (graphICur == 1):
    #             ax.set_zlabel('')
    #         if (graphICur == 2):
    #             ax.set_xlabel('')
    #         if (graphICur == 3):
    #             ax.set_ylabel('')
    #
    #         pylab.savefig(graphTitleSave+str(graphICur), dpi=savedpi, papertype='a1')
    #
    # if (angleType[0] == 2):
    #     ax.view_init(elev=-90, azim=0)
    # ===========================================================================


'''
Essential function for turning scatter 3d plot into contour 3d plot
'''


def grid(x, y, z, resX=100, resY=100):
    "Convert 3 column data to matplotlib grid"
    xi = np.linspace(min(x), max(x), resX)
    yi = np.linspace(min(y), max(y), resY)
    Z = griddata(x, y, z, xi, yi)
    X, Y = np.meshgrid(xi, yi)
    return X, Y, Z


toGraphHere = False


def graph_emaxKCash_Value(soluSupObj, resources, k_vec, emaxValsCur, emaxChoicesCur, emaxChoiceOfMaxCollCur,
                          predictUtil):
    grapher = graphFunc()
    pylab.clf()

    toGraphHere = False
    if (toGraphHere == True):
        # fig=pylab.figure()
        xLabStr = 'Cash on Hand'
        yLabStr = 'Physical Capital'
        xData = resources
        yData = k_vec

        '''
        Resource and K State Space Ranges
        '''
        # ===================================================================
        # grapher = grpSup.graphFunc()
        # pylab.clf()
        # grapher.xyPlotMultiYOneX(yDataMat=resources, saveOrNot=True, showOrNot=False, graphType='hist',
        #                          saveDirectory=fobj.support_args['IO'],
        #                          saveFileName='ResStateHist'+str(fobj.support_args['cur_round']),
        #                          basicTitle='Resource Histogram', basicXLabel='Resource State Points', basicYLabel='Density')
        #
        # pylab.clf()
        # grapher.xyPlotMultiYOneX(yDataMat=k_vec, saveOrNot=True, showOrNot=False, graphType='hist',
        #                          saveDirectory=fobj.support_args['IO'],
        #                          saveFileName='KStateHist'+str(fobj.support_args['cur_round']),
        #                          basicTitle='K Histogram', basicXLabel='K State Points', basicYLabel='Density')
        # ===================================================================

        titleStrList = ['Utility', 'Consumption Choice', 'Kapital Choice', 'B Formal Choice', 'B Informal Choice']
        titleStringList = ['Informal Borrow', 'Informal Save/Lend', 'Formal Borrow', 'Formal Save',
                           'Formal and Informal Borrow', 'Formal Borrow and Informal Save/Lend', 'None']
        titleStringList = ['Inf Borr', 'Inf Save', 'For Borr', 'Form Save',
                           'FB+IB', 'FB+IS', 'None']

        drawHere2DGraph = True
        drawHere3DGraph = False

        """
        3D and Contour
        """
        curRound = str(soluSupObj.sa['cur_round'])
        if (int(curRound) % 1 == 0):

            """
            Look over Value and Choices
            """
            # for curCol in range(0,0):

            if (drawHere2DGraph == True):
                pylab.clf()
                fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = pylab.subplots(2, 3)
                axisList = [ax1, ax2, ax3, ax4, ax5, ax6]

            for curCol in range(0, 5):
                pylab.sca(axisList[curCol])

                titlStr = titleStrList[curCol]
                labelArray_coll = [titlStr]
                noLabel = True

                if (titlStr == 'Utility'):
                    zData = emaxValsCur[:, 0]
                    angleType = [1, [1, 2, 3]]
                else:
                    zData = emaxChoicesCur[:, curCol - 1]
                    angleType = [3, [1]]

                if (drawHere2DGraph == True):

                    """
                    Draw Prediction Line
                    """
                    if (curCol == 0):
                        xDataSortedIdx = np.argsort(xData)
                        xDataSorted = xData[xDataSortedIdx]
                        predictUtilSorted = predictUtil[xDataSortedIdx]

                        grapher.xyPlotMultiYOneX(yDataMat=predictUtilSorted, xData=xDataSorted,
                                                 labelArray=labelArray_coll, noLabel=noLabel,
                                                 saveOrNot=False, graphType='plot')

                    """
                    Draw Choices and Value along resources, scatter, color showing K value
                    """
                    line45Deg = False
                    if (curCol == 1):
                        line45Deg = True

                    grapher.xyPlotMultiYOneX(yDataMat=zData, xData=xData, colorVar=yData,
                                             labelArray=labelArray_coll, noLabel=noLabel,
                                             saveOrNot=False, graphType='scatter', scattersize=1,
                                             labelLoc1t0=4, basicTitle=titlStr,
                                             basicXLabel='Cash on Hand', basicYLabel='Consumption Unit',
                                             line45Deg=line45Deg)

                if (drawHere3DGraph == True and curCol <= 4):
                    graphTitleDisp = titlStr
                    saveTitleFull = soluSupObj.sa['IO'] + 'EmaxApprox_VCKnBn_t' + str(curCol) + 'iter' + curRound
                    graphTitleSave = saveTitleFull
                    zLabStr = 'Choices'

                    contourAnd3D(xData, yData, zData, xLabStr, yLabStr, zLabStr,
                                 graphTitleDisp, graphTitleSave, angleType=angleType, drawContour=True, draw3D=True)

            if (drawHere2DGraph == True):
                grapher.savingFig(saveDirectory=soluSupObj.sa['IO'],
                                  saveFileName='EmaxApprox_VCKnBn_iter' + str(curRound),
                                  saveDPI=200, pylabUse=fig)

            """
            Probability of Choices Graphs along 3D
            """
            # for curCol in range(4,4,1):
            if (drawHere2DGraph == True):
                pylab.clf()
                fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = pylab.subplots(2, 4)
                axisList = [ax1, ax2, ax3, ax4, ax5, ax6, ax7]

            maxProb = np.max(emaxChoiceOfMaxCollCur[:, 4:11])
            for curCol in range(4, 11, 1):
                pylab.sca(axisList[curCol - 4])

                xLabStr = 'Cash on Hand'
                yLabStr = 'Physical Capital'
                titlStr = 'Probability of ' + titleStringList[curCol - 4]

                zData = emaxChoiceOfMaxCollCur[:, curCol]

                if (drawHere3DGraph == True):
                    graphTitleDisp = titlStr
                    saveTitleFull = soluSupObj.sa['IO'] + 'EmaxApprox_Prob_t' + str(curCol) + 'iter' + curRound
                    graphTitleSave = saveTitleFull
                    zLabStr = 'Probability of Choice'

                    contourAnd3D(xData, yData, zData, xLabStr, yLabStr, zLabStr,
                                 graphTitleDisp, graphTitleSave, angleType=[3, [1]], drawContour=True, draw3D=True)

                if (drawHere2DGraph == True):
                    grapher.xyPlotMultiYOneX(yDataMat=zData, xData=xData, colorVar=yData,
                                             saveOrNot=False, graphType='scatter', scattersize=1,
                                             basicTitle=titleStringList[curCol - 4],
                                             basicXLabel='Cash on Hand', basicYLabel='Probability',
                                             ylim=[-0.05, maxProb], xlim=[0 - 5000, np.max(xData) + 5000])

            """
            sumProb Should be 1, but maybe not due to code issues, need to check here
            """
            pylab.sca(ax8)
            sumProb = np.sum((emaxChoiceOfMaxCollCur[:, 4:11]), axis=1)
            grapher.xyPlotMultiYOneX(yDataMat=sumProb, xData=xData,
                                     saveOrNot=False, graphType='scatter', scattersize=1, basicTitle='Sum Prob',
                                     basicXLabel='Cash on Hand', basicYLabel='Probability', ylim=[-0.05, 1.05],
                                     xlim=[0 - 5000, np.max(xData) + 5000])

            if (drawHere2DGraph == True):
                grapher.savingFig(saveDirectory=soluSupObj.sa['IO'],
                                  saveFileName='EmaxApprox_Prob_iter' + str(curRound),
                                  saveDPI=200, pylabUse=fig)


def OLSEmaxValAndChoicesGraphs(allDataY, allDataX,
                               saveFileSuffix='', yLabelNames=['Emax', 'Choice'],
                               xLabelNames=['Height', 'Weight', 'Income'],
                               saveDirectory='default', saveFileName='default'):
    # toGraphHere = False
    if (toGraphHere == True):

        loopCountY = len(yLabelNames)
        for graphI in range(0, loopCountY, 1):
            yData = allDataY[graphI]
            OLSEmaxGraphs(saveFileSuffix, yVal=yData, allDataX=allDataX,
                          yLabelName=yLabelNames[graphI], xLabelNames=xLabelNames,
                          saveDirectory=saveDirectory, saveFileName=saveFileName)


def OLSEmaxGraphs(saveFileSuffix,
                  yVal, allDataX,
                  saveDirectory='default', saveFileName='default', yLabelName='yLabelName',
                  xLabelNames=['Height', 'Weight', 'Income']):
    if (saveDirectory == 'default'):
        saveDirectory = 'C:\\Users\\fan\\Documents\\Dropbox\\Height_Production_Function\\Results--HD on HL WL--Linear--Protein and Calorie With Price Instruments\\ProduWithPref\\'

    saveFileName = saveFileName + '_' + str(yLabelName) + str(saveFileSuffix)
    if (saveFileName == 'default'):
        saveFileName = 'EmaxApprox'

    grapher = graphFunc()
    pylab.clf()

    loopCount = len(xLabelNames)
    for graphI in range(0, loopCount, 1):
        xData = allDataX[graphI]
        yDataMat = yVal
        pylab.subplot(2, loopCount, graphI + 1)
        basicTitle = xLabelNames[graphI] + ' and ' + yLabelName
        basicXLabel = xLabelNames[graphI]
        basicYLabel = yLabelName
        grapher.xyPlotMultiYOneX(yDataMat=yDataMat, xData=xData, saveOrNot=False, graphType='scatterregline',
                                 basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel, noLabel=True,
                                 scattersize=0.1)

        xData = allDataX[graphI]
        pylab.subplot(2, loopCount, graphI + 1 + loopCount)
        basicTitle = xLabelNames[graphI] + ' Histogram'
        basicXLabel = xLabelNames[graphI]
        basicYLabel = 'Frequency'
        grapher.xyPlotMultiYOneX(yDataMat=xData, saveOrNot=False, graphType='hist',
                                 basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel, noLabel=True,
                                 bins=30)

        pylab.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        pylab.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

    grapher.savingFig(saveDirectory=saveDirectory, saveFileName=saveFileName)


class graphFunc:
    points = 200
    xData = np.linspace(-1, 1, points)
    xData = np.random.normal(10, 2, points)
    xData = np.sort(xData)
    yData1 = np.random.normal(0, 1, points)
    yData2 = np.random.normal(0, 1, points) + 10
    yDataMat = np.column_stack((yData1, yData2))
    # ===============================================================================

    # Legend location
    # The location of the legend can be specified by the keyword argument loc, either by string or a integer number.
    # String    Number
    # upper right    1
    # upper left    2
    # lower left    3
    # lower right    4
    # right    5
    # center left    6
    # center right    7
    # lower center    8
    # upper center    9
    # center    10
    # ===============================================================================

    labelLoc1t0 = 'best'
    labelColCount = 1
    labelArray = ['line y1', 'line y2']
    basicTitle = 'Image  Name'
    basicXLabel = 'X Title Name'
    basicYLabel = 'Y Title Name'

    showOrNot = False

    # saveDirectory = 'C:/Users/fan/Documents/Dropbox/Programming/Sandbox/Graphs/'
    saveDirectory = 'C:/Users/fan/Pictures'
    saveFileName = 'temp.png'
    saveDPI = 125

    colorCounter = 0

    # yDataMat should be N by K, and xData is N by 1
    def __init__(self,
                 showOrNot=False,
                 saveDirectory=saveDirectory,
                 saveDPI=saveDPI
                 ):
        self.showOrNot = showOrNot
        self.saveDirectory = saveDirectory
        self.saveDPI = saveDPI
        self.colorCounter = 0

    def xyPlotMultiYOneX(self, xData=xData, yDataMat=yDataMat, colorVar=None,
                         labelArray=labelArray, noLabel=True,
                         basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel,
                         labelLoc1t0=labelLoc1t0, labelColCount=labelColCount,
                         line45Deg=False,
                         showOrNot=False, saveOrNot=True, graphType='plot',
                         saveDirectory=saveDirectory, saveFileName=saveFileName, saveDPI=1000, toScale=True,
                         pylabUse=None,
                         ylim=None, xlim=None,
                         sequential_color=False,
                         subplot=None,
                         clear_first=False,
                         **keywords):
        """Graph general

        yDataMat each column corresponds to x
        """
        # ===========================================================================
        #     import Support.GraphSupport as grhSup
        #     import pylab as pylab
        #     grapher = grhSup.graphFunc()
        #     pylab.clf()
        #
        #     xData = prot
        #     yDataMat = util_at_protrange
        #
        #     basicTitle = 'Utility at Choices Mean States'
        #     basicXLabel = 'Protein'
        #     basicYLabel = basicTitle
        #     grapher.xyPlotMultiYOneX(yDataMat=yDataMat,xData=xData,saveOrNot=False, graphType='plot',
        #                              basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel,noLabel=True)
        #
        #     grapher.savingFig(saveDirectory=self.support_args['IO'],saveFileName='graphMeanChoice_r'+str(self.support_args['cur_round']))
        # ===========================================================================

        # TESTER: grapher = graphFunc().xyPlotMultiYOneX()

        # ===============================================================================
        # TESTER 2:
        #
        # grapher = graphFunc()
        # pylab.subplot(2,1,1)
        # grapher.xyPlotMultiYOneX(saveOrNot=False)
        # pylab.subplot(2,1,2)
        # grapher.xyPlotMultiYOneX(saveOrNot=False)
        # grapher.savingFig()
        # pylab.clf()
        # grapher.xyPlotMultiYOneX(saveOrNot=True,saveFileName='temp2')
        # ===============================================================================

        if (subplot is not None):
            pylab.subplot(subplot['rows'], subplot['cols'], subplot['cur'])

        if (pylabUse == None):
            pylabUse = pylab

        try:
            pylab.setp(pylabUse.xaxis.get_majorticklabels(), rotation=70)
        except:
            pylab.xticks(rotation=45)

        if (clear_first is True):
            pylab.cla()
            pylab.clf()
            pylab.close()
            pylab.gcf().clear()

        if (graphType.lower() == "polygon"):
            colCnt = 1
        else:
            curDim = np.ndim(yDataMat)
            if (curDim > 1):
                rowCnt, colCnt = (yDataMat.shape)
            else:
                colCnt = 1

        colorSet = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        if (colCnt > 1 and sequential_color == True):
            colorSet = sns.color_palette("coolwarm", colCnt)
            # colorSet = sns.diverging_palette(255, 133, l=60, n=colCnt, center="dark")
            sns.set_style("whitegrid")

        colors = itertools.cycle(colorSet)

        """
        For Single Array Graph one at a time but for which I also want to keep track of color, change individual draw by draw
        """
        self.colorCounter = self.colorCounter + 1
        for colorCntr in range(0, self.colorCounter, 1):
            colorUse = next(colors)

        """
        Special Types
        """
        if (graphType.lower() == "polygon"):
            self.graphingEachType(graphType, xData, yDataMat, keywords=keywords, color=colorUse, pylabUse=pylabUse)
        else:
            """
            Single Array Data Draw
            curDim = 0 if it is a single number
            """
            if (curDim <= 1):
                if (noLabel == True):
                    # pylabUse.plot(xData,yDataMat)
                    self.graphingEachType(graphType, xData, yDataMat, colorVar=colorVar, color=colorUse,
                                          keywords=keywords, pylabUse=pylabUse)
                if (noLabel == False):
                    # pylab.plot(xData,yDataMat,label=labelArray)
                    self.graphingEachType(graphType, xData, yDataMat, colorVar=colorVar, color=colorUse,
                                          keywords=keywords, label=labelArray, pylabUse=pylabUse)

            """
            Multiple Array Data Draw, with consistent color set
            """
            # colors = cm.rainbow(np.linspace(0, 1, len(ys)))
            if (curDim > 1):

                if (graphType.lower() == 'stackplot'):
                    # No Label here, Label in staplot legend specific section below
                    self.graphingEachType(graphType, xData, yDataMat, colorVar=colorVar,
                                          keywords=keywords, color=colorSet, pylabUse=pylabUse)
                else:
                    yColCount = yDataMat.shape[2 - 1]
                    colors = itertools.cycle(colorSet)
                    for curCol in range(0, yColCount):
                        color = next(colors)
                        if (noLabel == True):
                            # pylab.plot(xData,yDataMat[:,curCol])
                            self.graphingEachType(graphType, xData, yDataMat[:, curCol], colorVar=colorVar,
                                                  keywords=keywords, color=color, pylabUse=pylabUse)
                        if (noLabel == False):
                            # pylab.plot(xData,yDataMat[:,curCol],label=labelArray[curCol])
                            self.graphingEachType(graphType, xData, yDataMat[:, curCol], colorVar=colorVar,
                                                  keywords=keywords, label=labelArray[curCol], color=color,
                                                  pylabUse=pylabUse)

        """
        Labeling
        """
        if (noLabel == True):
            pass
        else:
            if (graphType.lower() == 'stackplot'):
                legendArtistList = []
                labelArrayUpdate = []
                rows, cols = yDataMat.shape
                for curStack in range(0, cols):
                    pCur = pylabUse.Rectangle((0, 0), 1, 1, fc=colorSet[curStack])
                    newLabel = labelArray[curStack] + \
                               ', ' + "{0:.{1}f}".format(yDataMat[0, curStack] * 100, 1) + '%' \
                                                                                           ' to ' + "{0:.{1}f}".format(
                        yDataMat[rows - 1, curStack] * 100, 1) + '%'
                    legendArtistList.append(pCur)
                    labelArrayUpdate.append(newLabel)
                pylabUse.legend(legendArtistList[::-1], labelArrayUpdate[::-1],
                                loc=labelLoc1t0, ncol=labelColCount, prop={'size': 6})
                pylabUse.axis((np.min(xData), np.max(xData), 0, 1.3))
            else:
                pylabUse.legend(loc=labelLoc1t0, ncol=labelColCount, prop={'size': 6})

        try:
            pylabUse.set_title(basicTitle)
            pylabUse.set_xlabel(basicXLabel)
            pylabUse.set_xlabel(basicYLabel)
        except:
            pylab.title(basicTitle)
            pylab.xlabel(basicXLabel)
            pylab.ylabel(basicYLabel)

        # =======================================================================
        # pylabUse.xticks()
        # ax.set_xticks(numpy.arange(0,1,0.1))
        # =======================================================================
        # pylab.grid()
        pylab.gca().grid(color='k', linestyle=':', linewidth=1, alpha=0.5)

        if (line45Deg == True):
            ymin = np.min(yDataMat)
            ymax = np.max(yDataMat)
            xmin = np.min(xData)
            xmax = np.max(xData)
            xymin = np.minimum(ymin, xmin)
            xymax = np.minimum(ymax, xmax)
            pylabUse.plot([xymin, xymax], [xymin, xymax], 'k--', alpha=0.5)

        if (ylim != None):
            pylabUse.ylim(ylim)

        if (xlim != None):
            pylabUse.xlim(xlim)

        # =======================================================================
        # try:
        #     pylab.ylim([np.min(yDataMat),np.max(yDataMat)])
        #     pylab.xlim([np.min(xData),np.max(xData)])
        # except:
        #     pass
        # =======================================================================

        if (showOrNot == True):
            pylab.show()

        if (saveOrNot == True):
            self.savingFig(saveDirectory, saveFileName, saveDPI, pylabUse=pylabUse, toScale=toScale)

        return pylabUse

    def graphingEachType(self, graphType, xSingleArrayData, ySingleArrayata,
                         keywords, colorVar=None, label=False, color='b', pylabUse=None):
        """
        If do not use basic pylab, but have external axis
        """
        if (pylabUse == None):
            pylabUse = pylab

        keys = sorted(keywords.keys())
        alpha = 1
        bins = 30
        scattersize = 1
        cmapColor = 'coolwarm'
        for kw in keys:
            if (kw == 'bins'):
                bins = int(keywords[kw])
            if (kw == 'scattersize'):
                scattersize = int(keywords[kw])
            if (kw == 'alpha'):
                alpha = float(keywords[kw])
            if (kw == 'cmap'):
                cmapColor = str(keywords[kw])

        if (label == False):
            label = ''

        if (graphType.lower() == 'polygon'):

            # ===================================================================
            # pylab.axes()
            # #points = [[2, 1], [8, 1], [8, 4]]
            # polygon = pylab.Polygon(ySingleArrayata)
            # #pylabUse.Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,color=color,fill=True,label=label)
            # pylab.gca().add_patch(polygon)
            # pylab.axis('scaled')
            # pylabUse.show()
            # ===================================================================
            # points = [[2, 1], [8, 1], [8, 4]]
            polygon = pylabUse.Polygon(ySingleArrayata, ec='k', fc=color, linewidth=1.5, alpha=0.3, label=label)
            # pylabUse.Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,color=color,fill=True,label=label)
            pylabUse.gca().add_patch(polygon)
            try:
                pylabUse.axis('scaled')
            except:
                pass

            # ===================================================================
            # try:
            #     pylabUse.add_patch(Polygon(ySingleArrayata,ec='k',fc=color, linewidth=1.5,alpha=0.3))
            # except:
            #     #points = [[2, 1], [8, 1], [8, 4]]
            #     polygon = pylabUse.Polygon(ySingleArrayata,ec='k',fc=color, linewidth=1.5,alpha=0.3)
            #     #pylabUse.Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,color=color,fill=True,label=label)
            #     pylabUse.gca().add_patch(polygon)
            #     #===============================================================
            #     # pylabUse.axis('scaled')
            #     #===============================================================
            # ===================================================================

            # ===================================================================
            # pylab.axis('scaled')
            # ===================================================================

            # ===================================================================
            # self.savingFig('C:/Users/fan/DynammicProgrammingPython/src/ProjectDisertCredit/model1/HandTry',
            #                'testPolygon', 100, pylabUse = pylabUse)
            # ===================================================================

        # ==============================================================================
        #            circle = pylab.Circle((0, 0), 0.75, fc='y')
        #            pylab.gca().add_patch(circle)
        #
        #            rectangle = pylab.Rectangle((10, 10), 100, 100, fc='r')
        #            pylab.gca().add_patch(rectangle)
        # ==============================================================================

        # ===============================================================================
        #             points = [[2, 1], [8, 1], [8, 4]]
        #             polygon = pylab.Polygon(points)
        #             pylab.gca().add_patch(polygon)
        #
        #             pylab.axis('scaled')
        #             pylab.show()
        #
        #
        #             points = [[2, 1], [8, 1], [8, 4]]
        #             pylab.Polygon(points)
        #             pylab.axis('scaled')
        #
        #             pylabUse.show()
        #
        #             #===================================================================
        #             # curPoly = Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,
        #             #           fill=False, hatch='/')
        #             # pylabUse.show()
        #             #===================================================================
        #
        #             # pylab.gca().add_patch(Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,fill=False, hatch='/'))
        # ===============================================================================

        # ===============================================================================
        #
        #             try:
        #                 points = [[2, 1], [8, 1], [8, 4]]
        #                 polygon = pylab.Polygon(points)
        #                 pylabUse.Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,color=color,fill=True,label=label)
        #             except:
        #                 pylabUse.add_patch(Polygon([[0,0],[4,1.1],[6,2.5],[2,1.4]], closed=True,color=color,fill=True,label=label))
        #             pylabUse.show()
        # ===============================================================================

        # pylab.gca().add_patch(Polygon(ySingleArrayata, closed=True,color=color,fill=True,label=label))
        if (graphType.lower() == 'stackplot'):
            pylabUse.stackplot(xSingleArrayData, np.transpose(ySingleArrayata), colors=color, alpha=alpha)
        if (graphType.lower() == 'density'):
            guassian_kde_graph(ySingleArrayata, color=color, label=label)
        if (graphType.lower() == 'plot'):
            pylabUse.plot(xSingleArrayData, ySingleArrayata, c=color, label=label, alpha=alpha)
        if (graphType.lower() == 'plotscatter'):
            pylabUse.plot(xSingleArrayData, ySingleArrayata, c=color, label=label)
            pylabUse.scatter(xSingleArrayData, ySingleArrayata, color='k', s=scattersize)
        if (graphType.lower() == 'scatter'):
            logger.debug('graphType.lower():%s', graphType.lower())

            if (colorVar is not None):
                # ===============================================================
                # pylabUse.scatter(xSingleArrayData, ySingleArrayata,marker='+', s=scattersize,
                #                  linewidths=4,c=colorVar)
                # pylabUse.gray()
                # ===============================================================

                # ===============================================================
                # coolwarm
                # ===============================================================
                # http://matplotlib.org/examples/color/colormaps_reference.html
                # ===============================================================
                # ===============================================================

                pylabUse.scatter(xSingleArrayData, ySingleArrayata, marker='+', s=scattersize,
                                 linewidths=4, c=colorVar,
                                 cmap=pylab.get_cmap(cmapColor), alpha=0.5)
            else:
                #                 logger.debug('xSingleArrayData:%s',xSingleArrayData)
                #                 logger.debug('ySingleArrayata:%s',ySingleArrayata)
                logger.debug('color:%s', color)
                logger.debug('label:%s', label)
                logger.debug('scattersize:%s', scattersize)
                pylabUse.scatter(xSingleArrayData, ySingleArrayata,
                                 color=color, label=label, s=scattersize, alpha=0.5)

        if (graphType.lower() == 'scatterregline'):
            pylabUse.scatter(xSingleArrayData, ySingleArrayata, s=scattersize)
            x = xSingleArrayData
            y = ySingleArrayata
            fit = pylabUse.polyfit(x, y, 1)
            fit_fn = pylabUse.poly1d(fit)  # fit_fn is now a function which takes in x and returns an estimate for y
            pylabUse.plot(x, y, 'yo', x, fit_fn(x), '--k', label=label)
        if (graphType.lower() == 'hist'):
            pylabUse.hist(ySingleArrayata, bins=bins, label=label, alpha=0.4)
        if (graphType.lower() == 'regline'):
            x = xSingleArrayData
            y = ySingleArrayata
            fit = pylabUse.polyfit(x, y, 1)
            fit_fn = pylabUse.poly1d(fit)  # fit_fn is now a function which takes in x and returns an estimate for y
            pylabUse.plot(x, y, 'yo', x, fit_fn(x), '--k', label=label)

        # =======================================================================
        # if (label == False):
        #     if(graphType == 'stackplot'):
        #         pylabUse.stackplot(xSingleArrayData, np.transpose(ySingleArrayata), colors=color, alpha=alpha)
        #     if(graphType == 'density'):
        #         guassian_kde_graph(ySingleArrayata, color=color)
        #     if(graphType == 'plot'):
        #         pylabUse.plot(xSingleArrayData, ySingleArrayata)
        #     if(graphType == 'plotscatter'):
        #         pylabUse.plot(xSingleArrayData, ySingleArrayata, c=color, label=label)
        #         pylabUse.scatter(xSingleArrayData, ySingleArrayata, c=color, s=scattersize)
        #     if(graphType == 'scatter'):
        #         pylabUse.scatter(xSingleArrayData, ySingleArrayata, c=color, s=scattersize)
        #     if(graphType == 'scatterregline'):
        #         pylabUse.scatter(xSingleArrayData, ySingleArrayata, s=2)
        #         x = xSingleArrayData
        #         y = ySingleArrayata
        #         fit = pylabUse.polyfit(x, y, 1)
        #         fit_fn = pylabUse.poly1d(fit)  # fit_fn is now a function which takes in x and returns an estimate for y
        #         pylabUse.plot(x, y, 'yo', x, fit_fn(x), '--k')
        #     if(graphType == 'hist'):
        #         pylabUse.hist(ySingleArrayata, bins=bins, alpha=0.4)
        #     if(graphType == 'regline'):
        #         x = xSingleArrayData
        #         y = ySingleArrayata
        #         fit = pylabUse.polyfit(x, y, 1)
        #         fit_fn = pylabUse.poly1d(fit)  # fit_fn is now a function which takes in x and returns an estimate for y
        #         pylabUse.plot(x, y, 'yo', x, fit_fn(x), '--k')
        # else :
        #     if(graphType == 'stackplot'):
        #         pylabUse.stackplot(xSingleArrayData, np.transpose(ySingleArrayata), colors=color, alpha=alpha)
        #     if(graphType == 'density'):
        #         guassian_kde_graph(ySingleArrayata, color=color, label=label)
        #     if(graphType == 'plot'):
        #         pylabUse.plot(xSingleArrayData, ySingleArrayata, c=color, label=label)
        #     if(graphType == 'plotscatter'):
        #         pylabUse.plot(xSingleArrayData, ySingleArrayata, c=color, label=label)
        #         pylabUse.scatter(xSingleArrayData, ySingleArrayata, c='k', s=scattersize)
        #     if(graphType == 'scatter'):
        #         pylabUse.scatter(xSingleArrayData, ySingleArrayata, c=color, label=label, s=scattersize)
        #     if(graphType == 'scatterregline'):
        #         pylabUse.scatter(xSingleArrayData, ySingleArrayata, s=scattersize)
        #         x = xSingleArrayData
        #         y = ySingleArrayata
        #         fit = pylabUse.polyfit(x, y, 1)
        #         fit_fn = pylabUse.poly1d(fit)  # fit_fn is now a function which takes in x and returns an estimate for y
        #         pylabUse.plot(x, y, 'yo', x, fit_fn(x), '--k', label=label)
        #     if(graphType == 'hist'):
        #         pylabUse.hist(ySingleArrayata, bins=bins, label=label, alpha=0.4)
        #     if(graphType == 'regline'):
        #         x = xSingleArrayData
        #         y = ySingleArrayata
        #         fit = pylabUse.polyfit(x, y, 1)
        #         fit_fn = pylabUse.poly1d(fit)  # fit_fn is now a function which takes in x and returns an estimate for y
        #         pylabUse.plot(x, y, 'yo', x, fit_fn(x), '--k', label=label)
        # =======================================================================

    def savingFig(self, saveDirectory=saveDirectory, saveFileName=saveFileName, saveDPI=saveDPI, saveOrNot=True,
                  showOrNot=False,
                  pylabUse=None, toScale=True, subplots_adjust=True):

        if (pylabUse == None):
            pylabUse = pylab

        if (subplots_adjust == True):
            try:
                pylabUse.subplots_adjust(hspace=0)
            except:
                pass

        if (pylabUse == None):
            pylabUse = pylab

        if (toScale == True):
            try:
                pylabUse.axis('scaled')
            except:
                pass

        try:
            pylabUse.tight_layout()
        except:
            pass

        font = {'family': 'sans-serif',
                'weight': 'normal',
                'size': 7}
        pylab.rc('font', **font)
        if (showOrNot == True):
            pylab.show()

        if (saveOrNot == True):
            pylab.savefig(saveDirectory + saveFileName, dpi=saveDPI, papertype='a4')

    def sampleGraphs(self, graphSampleType, graphType='plot'):

        if (graphSampleType == 'OnePlot'):
            self.xyPlotMultiYOneX(saveOrNot=False, graphType=graphType, labelArray=self.labelArray, noLabel=False)

        if (graphSampleType == 'TwoPlot'):
            pylab.subplot(2, 1, 1)
            self.xyPlotMultiYOneX(saveOrNot=False)
            pylab.subplot(2, 1, 2)
            self.xyPlotMultiYOneX(saveOrNot=False)

        if (graphSampleType == 'ScatterHistPlotDifferSize'):
            pylab.subplot2grid((3, 2), (0, 0), colspan=2, rowspan=2)
            self.xyPlotMultiYOneX(saveOrNot=False, graphType='scatter', scattersize=50)
            pylab.subplot2grid((3, 2), (2, 0))
            self.xyPlotMultiYOneX(saveOrNot=False, graphType='hist', bins=50)
            pylab.subplot2grid((3, 2), (2, 1))
            self.xyPlotMultiYOneX(saveOrNot=False, graphType='plot')

        if (graphSampleType == 'ScatterHistPlotDifferSize'):
            pylab.subplot2grid((3, 2), (0, 0), colspan=2, rowspan=2)
            self.xyPlotMultiYOneX(saveOrNot=False, graphType='scatter')
            pylab.subplot2grid((3, 2), (2, 0))
            self.xyPlotMultiYOneX(saveOrNot=False, graphType='hist', bins=20)
            pylab.subplot2grid((3, 2), (2, 1))
            self.xyPlotMultiYOneX(saveOrNot=False, graphType='plot')

        self.savingFig(saveFileName=graphSampleType, saveOrNot=False, showOrNot=True)
        pylab.clf()


def guassian_kde_graph(data_fordensity, graph_xgrid=False, xgridpoints=1000, color='b', label=False,
                       showOnScreen=False):
    density = gaussian_kde(data_fordensity)
    density.covariance_factor = lambda: .25
    density._compute_covariance()

    if (graph_xgrid == False):
        data_min = np.min(data_fordensity)
        data_max = np.max(data_fordensity)
        graph_xgrid = np.linspace(data_min, data_max, xgridpoints)

    if (label == False):
        pylab.plot(graph_xgrid, density(graph_xgrid), c=color)
    else:
        pylab.plot(graph_xgrid, density(graph_xgrid), c=color, label=label)

    if (showOnScreen == True):
        pylab.show()


def subplot_square_counter(totalimages=15):
    # ===========================================================================
    # for i in np.arange(9,16,1):  subplot_square_counter(totalimages=i)
    # ===========================================================================

    sqrt_image = np.sqrt(totalimages)
    sqrt_image = np.ceil(sqrt_image)

    sqrt_image_remainder = np.remainder(totalimages, sqrt_image)
    sqrt_image_divide = np.floor(totalimages / sqrt_image)

    cols = sqrt_image
    rows = sqrt_image_divide

    if (sqrt_image_remainder > 0):
        rows += 1

    return rows, cols


def sampleDataGraphs():
    # ===========================================================================
    # import Support.GraphSupport as grhSup
    # import pylab as pylab
    # grapher = grhSup.graphFunc()
    # ===========================================================================

    grapher = graphFunc()

    # x = np.arange(0, 3*np.pi+np.pi/4, 2*np.pi/8)
    pointCount = 500
    x = np.linspace(0, 3 * np.pi + np.pi / 4, pointCount)

    y_sin = np.sin(x)
    y_cos = np.cos(x)
    yColl = np.column_stack((y_sin, y_cos))

    np.random.seed(111)
    error = np.random.normal(loc=0, scale=1, size=len(x))
    y_sin_err = y_sin + error
    y_cos_err = y_cos + error

    """
    Simple Graph 1
    """
    basicTitle = 'Graph Test'
    basicXLabel = 'X'
    basicYLabel = 'Y'
    saveDirectory = 'C:\\Users\\fan\\Documents\\Dropbox (UH-ECON)\\Programming\\PYTHON\\TestGraphs\\'

    pylab.clf()
    saveFileName = 'graphTest1_line'
    grapher.xyPlotMultiYOneX(graphType='plot',
                             yDataMat=y_sin, xData=x,
                             basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel, noLabel=True,
                             saveOrNot=True, saveDirectory=saveDirectory, saveFileName=saveFileName)

    pylab.clf()
    saveFileName = 'graphTest1_scatter'
    grapher.xyPlotMultiYOneX(graphType='scatter', scattersize=10,
                             yDataMat=y_sin_err, xData=x,
                             basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel, noLabel=True,
                             saveOrNot=True, saveDirectory=saveDirectory, saveFileName=saveFileName)

    """
    Simple Graph 2
    """
    basicTitle = 'Graph Test'
    basicXLabel = 'X'
    basicYLabel = 'Y'
    saveDirectory = 'C:\\Users\\fan\\Documents\\Dropbox (UH-ECON)\\Programming\\PYTHON\\TestGraphs\\'

    pylab.clf()
    saveFileName = 'graphTest2_line'
    grapher.xyPlotMultiYOneX(graphType='plot',
                             yDataMat=yColl, xData=x,
                             labelArray=['sin', 'cos'], noLabel=False, labelLoc1t0=2, labelColCount=2,
                             basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel,
                             saveOrNot=True, saveDirectory=saveDirectory, saveFileName=saveFileName)

    pylab.clf()
    saveFileName = 'graphTest2_scatter'
    grapher.xyPlotMultiYOneX(graphType='scatter', scattersize=10,
                             yDataMat=yColl, xData=x,
                             labelArray=['sin', 'cos'], noLabel=False, labelLoc1t0=1, labelColCount=1,
                             basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel,
                             saveOrNot=True, saveDirectory=saveDirectory, saveFileName=saveFileName)

    """
    Simple Graph 3
    """
    graphTitleDisp = 'Graph Test 3D'
    xLabStr = 'X'
    yLabStr = 'Y'
    zLabStr = 'Z'

    zData = y_cos_err
    xData = y_cos
    yData = error

    saveDirectory = 'C:\\Users\\fan\\Documents\\Dropbox (UH-ECON)\\Programming\\PYTHON\\TestGraphs\\'
    graphTitleSave = saveDirectory + 'graphTest3_3d'
    contourAnd3D(xData, yData, zData,
                 xLabStr, yLabStr, zLabStr,
                 graphTitleDisp, graphTitleSave,
                 savedpi=125, angleType=[1, [1, 2, 3, 4, 5, 6]],
                 drawContour=True, draw3D=True,
                 contourXres=100, contourYres=100)

    # ===========================================================================
    # basicTitle = 'Graph Test'
    # basicXLabel = 'X'
    # basicYLabel = 'Y'
    # saveDirectory = 'C:\\Users\\fan\\Documents\\Dropbox\\Programming\\PYTHON\\TestGraphs\\'
    # saveFileName = 'graphTest1'
    # grapher.xyPlotMultiYOneX(graphType='plot',yDataMat=y1,xData=x,
    #                          basicTitle=basicTitle, basicXLabel=basicXLabel, basicYLabel=basicYLabel,noLabel=True,
    #                          saveOrNot=True, saveDirectory=saveDirectory,saveFileName=saveFileName)
    # ===========================================================================

    # ===========================================================================
    # grapher.savingFig(saveDirectory=self.support_args['IO'],saveFileName='graphMeanChoice_r'+str(self.support_args['cur_round']))
    # ===========================================================================


if __name__ == '__main__':
    # ===========================================================================
    # data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8
    # density = gaussian_kde(data)
    # xs = np.linspace(0,8,200)
    # density.covariance_factor = lambda : .25
    # density._compute_covariance()
    # if (showOnScreen==True):
    #     pylab.plot(xs,density(xs))
    #     pylab.show()
    # ===========================================================================

    # ===============================================================================
    # guassian_kde_graph(showOnScreen=True)
    # ===============================================================================
    grapher = graphFunc()
    grapher.sampleGraphs(graphSampleType='OnePlot', graphType='scatter')
    grapher.sampleGraphs(graphSampleType = 'OnePlot',graphType='stackplot')
    grapher.sampleGraphs(graphSampleType = 'TwoPlot')
    grapher.sampleGraphs(graphSampleType = 'ScatterHistPlotDifferSize')

    # ===============================================================================
    # grapher = graphFunc()
    # grapher.sampleGraphs(graphSampleType = 'ScatterHistPlotDifferSize')
    # ===============================================================================
