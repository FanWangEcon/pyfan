# -*- coding: utf-8 -*-
"""
Generate Graphs using the Generic Graphing Tool
========================================================================

In this example, we generate a line plot, a density plot and a scatter plot.
"""

# Author: Fan Wang (fanwangecon.github.io)
import pyfan.graph.generic.allpurpose as pyfan_graph_allpurpose
import numpy as np

# %%
# Plot Time Series Lines of Temperatures in Two Cities
# --------------------------------------------------------------

# construct data inputs
np.random.seed(0)
it_days = 365
ar_x = np.linspace(1, 365, it_days)
ar_y1 = np.random.normal(25, 3, it_days)
ar_y2 = np.random.normal(15, 5, it_days)
mt_y = np.column_stack((ar_y1, ar_y2))

# graphing class object instance
co_grapher = pyfan_graph_allpurpose.graphFunc()
co_grapher.xyPlotMultiYOneX(xData=ar_x, yDataMat=mt_y,
                            basicTitle="Temperature Flucations Two Cities",
                            basicXLabel="days of the year",
                            basicYLabel="daily temperatures",
                            labelArray=["city 1, mean=25, sd=3",
                                        "city 2, mean=15, sd=5"], noLabel=False,
                            graphType='plot',
                            saveOrNot=False, showOrNot=False)

# %%
# Plot Three Densities of Test Score Distributions
# --------------------------------------------------------------

# construct data inputs
np.random.seed(0)
it_students_perclass = 100
ar_student_id = np.arange(it_students_perclass)
ar_class_a_tests = np.random.normal(80, 3, it_students_perclass)
ar_class_b_tests = np.random.normal(75, 10, it_students_perclass)
ar_class_c_tests = np.random.normal(50, 20, it_students_perclass)
mt_y = np.column_stack((ar_class_a_tests, ar_class_b_tests, ar_class_c_tests))

# graphing class object instance
co_grapher = pyfan_graph_allpurpose.graphFunc()
co_grapher.xyPlotMultiYOneX(xData=ar_x, yDataMat=mt_y,
                            basicTitle="Test Score Densities (100 students per class)",
                            basicXLabel="Test Scores",
                            basicYLabel="Densities",
                            labelArray=["Class 1", "Class 2", "Class 3"], noLabel=False,
                            graphType='density',
                            saveOrNot=False, showOrNot=False)

# %%
# Plot a Scatter Plot of the Relationship Between Wage and Education
# ------------------------------------------------------------------

# construct data inputs
np.random.seed(0)
it_worker_obs = 100
ar_worker_edu = np.random.choice(18, it_worker_obs);
ar_log_wage_shock = np.random.normal(0, 0.2, it_worker_obs)
ar_worker_wage = np.exp(2 + ar_worker_edu*0.05 + ar_log_wage_shock)

# graphing class object instance
co_grapher = pyfan_graph_allpurpose.graphFunc()
co_grapher.xyPlotMultiYOneX(xData=ar_worker_edu, yDataMat=ar_worker_wage,
                            basicTitle="Hourly Wage and Years of Education",
                            basicXLabel="Years of Schooling",
                            basicYLabel="Hourly Wage",
                            graphType='scatter', scattersize=10,
                            saveOrNot=False, showOrNot=False)

