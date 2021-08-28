import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/NJ_prject/Pandas/County_municipality.csv')
county_to_municipality = {}
county_list= df.keys().tolist()


# 'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Population_2012_clean.csv',
# 'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Election_Results_2012_clean.csv',

csv_list = ['https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Voters&turnout_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Crime_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Employment_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Fiscal_Resources_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Gov_Expenditures_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Housing_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Poverty_2012_clean.csv',
'https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/2012_data/NJ_Property_Tax_Burden_2012_clean.csv',
]

indicator_list = ['Violent Crimes','Non-Violent Crimes','% Unemployed','Per Capita Taxable Property Value','Income Per Taxpayer',
                  'Municipal Budget per Capita ($)','Average Residential Property Value ($)','% Owner Occupied Units','TANF %','% SNAP Beneficiaries',
                  'School Tax Rate (%)','Property Tax as % Income','Registered Voters as % Population','% Democrats','Voter Turnout (%)']
final_dict={}
pair_list = ['Voters&turnout_2012','Crime_2012','Employment_2012','Fiscal_Resources_2012','Gov_Expenditures_2012',
'Housing_2012','Poverty_2012','Property_Tax_Burden_2012']

for csv_name in csv_list:
    df_crime = pd.read_csv(csv_name)
    df_crime['County_Municipality'] = df_crime['County']+' '+df_crime['Municipality']
    df_crime = df_crime.replace(to_replace ="Township",value ="Twp")
    df_crime = df_crime.replace(to_replace ="-",value ="0")


    for county_name in county_list:
        df_clean = df.dropna(how='any', subset=[county_name])
        df_clean = df_clean.replace(to_replace ="Township",value ="Twp")
        municipality_name = df_clean[county_name].tolist()
        df_curr=(df_crime[df_crime['County'] == county_name]).set_index('Municipality')
        for indicator in indicator_list:
            if indicator in df_curr.columns:
                municipality_value = {i : df_curr.loc[i,indicator] for i in municipality_name}
                county_to_municipality[county_name] = municipality_value
    #print(county_to_municipality.items())
    #print(county_to_municipality)   

    summary={}
    for names in pair_list:
        for county_name in county_to_municipality.keys():
            new_list = 0
            for values in county_to_municipality[county_name].values():
                new_list += float(values)
            summary.update({county_name:"%.2f" % new_list})
            final_dict.update({names:summary})
#print(final_dict.values())

