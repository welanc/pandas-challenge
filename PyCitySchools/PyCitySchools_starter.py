#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[221]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete


# In[222]:


#test: confirm column names
school_data_complete.columns


# In[223]:


#test: confirm series data types
school_data_complete.dtypes


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[224]:


#test: group data by schools
schools_total = len(school_data_complete["school_name"].unique())
students_total = school_data_complete["student_name"].count()

s_d_group = school_data_complete.groupby(["school_name"]).mean()
budget_total = s_d_group["budget"].sum()

math_score_average = school_data_complete["math_score"].mean()

reading_score_average = school_data_complete["reading_score"].mean()

math_pass = school_data_complete.loc[school_data_complete["math_score"] >= 70, :]
math_pass_count = math_pass["student_name"].count()
math_pass_pc = float(math_pass_count/students_total) * 100

reading_pass = school_data_complete.loc[school_data_complete["reading_score"] >= 70, :]
reading_pass_count = reading_pass["student_name"].count()
reading_pass_pc = float(reading_pass_count/students_total) * 100

ovr_pass = school_data_complete.loc[(school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70), :]
ovr_pass_count = ovr_pass["student_name"].count()
ovr_pass_pc = float(ovr_pass_count/students_total) * 100


# In[225]:


school_district_summary = pd.DataFrame({
    "Total Schools": schools_total,
    "Total Students": students_total,
    "Total Budget": budget_total,
    "Average Math Score": math_score_average,
    "Average Reading Score": reading_score_average,
    "% Passing Math": math_pass_pc,
    "% Passing Reading": reading_pass_pc,
    "% Overall Passing": ovr_pass_pc
}, index=[0])
school_district_summary["Total Students"] = school_district_summary["Total Students"].map("{:,}".format)
school_district_summary["Total Budget"] = school_district_summary["Total Budget"].map("{:,.2f}".format)
school_district_summary


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[275]:


school_group = school_data_complete.groupby("school_name")
school_group.count().columns


# In[331]:


school_type = pd.Series(school_group["type"].unique())

school_type


# In[368]:


students_df = pd.Series(school_group["student_name"].count())
students_df.dtype


# In[310]:


school_budget_df = pd.DataFrame(school_group["budget"].unique().astype("int"))
school_budget_df


# In[238]:


student_budget = (school_budget_df["budget"])/(students_df["student_name"])
student_budget_df = pd.DataFrame({"Per Student Budget":student_budget})
student_budget_df.head()


# In[340]:


school_math_average = school_group["math_score"].mean()
school_math_average


# In[244]:


school_reading_average = pd.DataFrame(school_group["reading_score"].mean())


# In[376]:


# % of students passing maths = that school's no. of students scoring 70% and above, divided by that school's population

school_math_pass = (math_pass["math_score"]) / (students_df)


# In[348]:


merge_df = pd.DataFrame({
    "School Type":school_type,
    "Total Students":students_df,
    "Average Math Score":school_math_average,
})
merge_df


# In[9]:





# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[10]:





# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[11]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[12]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[13]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[22]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[24]:





# In[ ]:




