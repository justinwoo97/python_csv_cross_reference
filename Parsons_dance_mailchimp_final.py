import pandas as pd 

# this chunk of code extracts all the names from the csv file 
# gets rid of the duplicates
# and make them into a list
final_list=[]
csv_list = ['01-Venue Contacts.csv','02-Summer Intensive.csv','03-Studio Showing Attendees | Nov 2018.csv','05-Past Parsons Dance Education Participants.csv',
            '06-Parsons Friends and Family.csv','07-Parsons Dance Workshops.csv','09-Opening Night Party.csv','10-Midterm Campaign Donors -4-14-17.csv',
           '11-Master Choreography.csv','12-Master Choreo LIght Family 2018.csv','13-Licensing.csv','14-Joyce Thank You Blast 2018.csv','15-Jan 30 2018 Studio Showing.csv',
           '16-Gala List as of 4-12-2016.csv','17-Gala 2106 Invitation Round 2.csv','18-Gala 2019 Guests.csv','20-Gala 2017 Attendees.csv','21-Former Interns.csv',
           '22-Former Gala Volunteers.csv','23-Former Emplyees.csv','24-Dube Campaign Donors Final.csv','25-Designers.csv','26-Campaign Master List 1.24.17.csv',
           '27-Board of directors.csv','28-Audition List | Nov 2018.csv','29-Audition List | Jun 23rd 2018.csv','30-Annual Appeal 16-17.csv','31-2019 Summer Intensive Discount Students.csv',
           '32-2019 Gala List.csv','33-2019 Education List.csv','34-2017 Full Education contacts.csv','35-2017 Chatham Interest.csv','36-2017 Campaign Donors.csv','37-2017 Audition List.csv',
           '38-2015 Studio Showing Invitation Internal.csv']
for file in csv_list:
    df = pd.read_csv(file)
    df['First-Last'] = df['Last Name']+' '+df['First Name']
    # get rid of all the NaN rows
    df_clean = df.dropna(how='any', subset=['First-Last'])
    # drop all the duplicate values
    df_clean = df_clean.drop_duplicates(subset=['First-Last'],keep='first')
    #change the dataframe into list
    df_final = df_clean['First-Last'].tolist()
    #df_1_final
    final_list.extend(df_final)    
#print(final_list)


#create two dataframes final_df
#make the final_list(list that contains all the names) 
# as a column in the dataframe final_df
final_df = pd.DataFrame({'Full-Name':final_list})


# create another dataframe new_frame
# incorporate the final_list as column w/ csv_file as row 
new_frame = pd.DataFrame({'Full-Name': final_df["Full-Name"].values})
for csv_file in csv_list:
    new_frame[csv_file] = ''  


# merege two list with column name First-Last' from df_clean 
# and column name "Full-Name" from the right list
df_clean.merge(final_df, how='left', left_on='First-Last', right_on="Full-Name")["First-Last"].values


#create a dict that stores csv file name as key
# and names in that file as value
csv_to_name_map = {}
for csv_file in csv_list:
    df = pd.read_csv(csv_file)
    df['First-Last'] = df['Last Name']+' '+df['First Name']
    df_clean = df.dropna(how='any', subset=['First-Last'])
    names_in_csv = list(df_clean['First-Last'].values)
    csv_to_name_map[csv_file] = names_in_csv
final_name_list = list(new_frame["Full-Name"].values)



#set the index for the Full-Name
new_frame.set_index('Full-Name', inplace=True)


for csv_file, names_list in csv_to_name_map.items():
    for csv_name in names_list:
        new_frame[csv_file][csv_name] = 1 if csv_name in final_name_list else 0


#display the dataframe new_frame
display(new_frame)

#export it into csv files
new_frame.to_csv("final_csv_file.csv", sep=',', encoding='utf-8')