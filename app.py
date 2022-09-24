# Import libraries
import csv
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np

import streamlit as st

def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv"
    )
    return data

def load_ph_data():
    ph_data = global_data[global_data['economy'] == 'Philippines']
    return ph_data

def title():
    st.title("Promoting Savings Through Formal Institutions: A Step Towards Financial Resiliency")

def study_context():
    st.title("Study Context")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("images/A.png")
        with col2:
            st.markdown("### Something bad happened and you need to come up with Php10,000!")
    st.empty()
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Do you think you can get this within 30 days?")
        with col2:
            st.image("images/B.png")
    st.empty()
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("images/C.png")
        with col2:
            st.markdown("### More than 50% of Filipinos can not get 10,000 php within 30 Days")
            st.markdown("### But is 10,000 php even enough for emergencies?")
    st.empty()
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### The Philippines ranked 9th in Disaster Risk")
            st.markdown("### Hospitalization cost for COVID: Php50,000 to Php200,000")
            st.markdown("### These costs are hard to cover without enough savings")
        with col2:
            st.image("images/D.png")
    
def problem_statement():
    st.title(
        "Problem Statement"
    )
    
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.image("images/E.png")

        with col2:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("### What steps can we take to empower Filipinos to save for the 'rainy days'?")

def fi_state_worldwide():
    # Write the title and the subheader
    st.title(
        "This is the current state of FI worldwide."
    )
    st.markdown(
        "**Here is a bubble map presenting the % of debit card ownership per country:**"
    )

    # Load data
    data = load_data()

    # Create another column for debit card ownership
    data['has_debit_card'] = data['fin2'].apply(
        lambda x: 1 if x == 1 else 0
    )

    # Group the data and apply aggregations
    grouped_data = data.groupby(['economy', 'economycode', 'regionwb']).agg(
        total_debit_card_owners=('has_debit_card', 'sum'),
        total_population=('wpid_random', 'count')
    ).reset_index()

    # Compute debit card ownership in %
    grouped_data['% of population with debit card'] = grouped_data['total_debit_card_owners'] * 100.0 / grouped_data[
        'total_population']

    # Build the bubble map
    fig = px.scatter_geo(
        grouped_data,
        locations="economycode",
        color="regionwb",
        hover_name="economy",
        size="% of population with debit card",
        projection="natural earth"
    )

    # Show the figure
    st.plotly_chart(fig)

def objectives():
    st.title(
        "Objectives"
    )
    
    st.markdown("- ### To identify the factors affecting financial resilience")
    st.markdown("- ### To identify financially vulnerable groups")
    st.markdown("- ### To recommend policies that would improve financial resilience")
    

def dataset():
    st.title(
        "Dataset"
    )

    ph_data = global_data[
        global_data['economy'] == 'Philippines'
    ]

    st.image("images/F.png")
    st.markdown("A global study on **144 countries**.")
    st.markdown("Sample size: **154,923**")
    st.markdown("Variables: **105**")

    # Display data
    st.dataframe(ph_data)
    st.markdown("Source: Global Findex 2017 from World Bank.")

def methodology():
    st.title(
        "Methodology"
    )
    
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Inspect & Extract")
            st.caption("Inspect how information is encoded in dataset.")
            st.caption("Extract information relevant to Philippines.")
            st.caption("Philippine data: sample size of 1,000")
        with col2:
            st.header("Explore")
            st.markdown("")
            st.markdown("")
            st.caption("Conduct exploratory data analysis and visualizations.")
        with col3:
            st.header("Cluster")
            st.markdown("")
            st.markdown("")
            st.caption("Perform K-Modes clustering to identify similar groups in the data.")
        with col4:
            st.header("Evaluate")
            st.markdown("")
            st.markdown("")
            st.caption("Evaluate results and provide conclusions and recommendations.")

def eda():
    st.title(
        "Exploratory Data Analysis"
    )
    
    with st.container():
        # 2 columns (1st column: image, 2nd column: metrics)
        col1, col2 = st.columns(2)

        with col1:
            st.image("images/passbook-1.jpg")

        with col2:
            st.subheader("Only 1 in every 3 Filipinos has a bank account")
            st.subheader("Of those who have  bank accounts: Only 1 in 3 saved in his/her account within the past year!")
    
    st.empty()
    st.empty()
    st.subheader("Owning an account improves financial resilience across all income and age groups.")
    plot_fi_resilience_in_age_income_groups()
    
    st.empty()
    st.empty()
    st.subheader("Not only do they have access to emergency funds, but they are more self-resilient.")
    st.image("images/I.png")
    
    st.empty()
    st.empty()
    st.subheader("But where does the Philippines stand in terms of Financial Account coverage?")
    plot_sea_fi_inclusion()
    st.markdown("In comparison with other  ASEAN nations,  The Philippines is in the middle in terms of Financial Inclusion with a **34.4%**.")
    
    st.empty()
    st.empty()
    st.subheader("What is hindering unbanked Filipinos from creating financial accounts?")
    st.image("reasons_why_filipinos_dont_own_a_bank_account.jpg")
    st.markdown("Poverty Problem: 51% of the respondents who gave this reason also answered that they do not have emergency funds; there is a group of people who don't have extra money to save")
    
def plot_sea_fi_inclusion():
    global_data['with bank account'] = global_data.apply(
        lambda x: 1 if x['account_fin'] == 1 else None,
        axis = 1
    )
    
    # philippine_data = global_data[
    #     global_data["economy"] == "Philippines" 
    # ]
    
    sea_data = global_data[
        (global_data["economy"] == "Philippines") |
        (global_data["economy"] == "Brunei") |
        (global_data["economy"] == "Cambodia") |
        (global_data["economy"] == "Indonesia") |
        (global_data["economy"] == "Lao PDR") |
        (global_data["economy"] == "Malaysia") |
        (global_data["economy"] == "Myanmar") |
        (global_data["economy"] == "Singapore") |
        (global_data["economy"] == "Thailand") |
        (global_data["economy"] == "Vietnam")
    ]
    
    grouped_sea_data = sea_data.groupby(['economy','economycode'])['wpid_random', 'with bank account'].count()
    grouped_sea_data = grouped_sea_data.reset_index()
    
    # Compute % population with account
    grouped_sea_data['% with bank account'] = grouped_sea_data['with bank account']*100.0/grouped_sea_data['wpid_random']
    data_viz_1 = grouped_sea_data[[
        'economy','economycode',
        '% with bank account'
    ]]
    data_viz_1 = data_viz_1.sort_values('% with bank account', ascending=False).reset_index(drop=True)

    # Rename columns
    data_viz_1 = data_viz_1.rename(
        columns = {
            'economy':'ASEAN Nation', 
            '% with bank account':'% with bank account'
            }
    )
    
    # Set figure size
    fig = plt.figure(figsize=(6,3)  , dpi=200)
    clrs = ['grey' if (x != "PHL") else '#07b1f0' for x in data_viz_1['economycode'] ]
    # Run bar plot
    sns.barplot(
        x=data_viz_1['economycode'],
        y= data_viz_1['% with bank account'],
        palette=clrs
    )

    # Set title
    plt.title('ASEAN Countries and Financial Inclusion')

    # Set labels
    plt.xlabel('Countries')
    plt.ylabel('% Population with Bank Account')

    # Rotate x labels
    plt.xticks(rotation=45)

    # Show figure
    # plt.show()
    st.pyplot(fig)
    
def plot_fi_resilience_in_age_income_groups():
    global_data['age_group'] = pd.cut(
        global_data.age,
        bins=[15,25,35,45,55,float("inf")],
        labels= ['15-24','25-34','35-44','45-54','55 and older']
    )

    ph_data = global_data[global_data.economy == "Philippines"].reset_index(drop = True)
    ph_data = ph_data[[
        "economy",
        "wpid_random",
        "female",
        "age_group",
        "educ",
        "inc_q",
        "account_fin", # has an account in a financial institution
        "fin17a", #who saves in a fin institution?
        "fin24", #who can come up with emergency funds?
    ]]
    
    ph_data = ph_data.rename(
        columns= {
            "female" : "gender",
            "educ" : "educational_attiainment",
            "inc_q" : "income_group",
            "account_fin" : "has_a_fin_account",
            "fin17a" : "saves_in_a_fin_account",
            "fin24" : "can_get_emergency_funds"
        }
    )
    
    educ_map = {
        1: "primary",
        2: "secondary",
        3: "tertiary"
    }

    inc_map = {
        1:'A - poorest 20%',
        2:'B - second 20%',
        3:'C - middle 20%',
        4:'D - fourth 20%',
        5:'E - richest 20%'
    }

    yes_no_map = {
        0: False,
        1: True,
        2: False,
        3: False,
        4: False,
    }

    column_list = [
        "educational_attiainment", 
        "income_group", 
        "has_a_fin_account",
        "saves_in_a_fin_account",
        "can_get_emergency_funds"
    ]
        
    value_maps = [
        educ_map, 
        inc_map, 
        yes_no_map,
        yes_no_map,
        yes_no_map
    ]
    
    for count in range(len(column_list)):
        ph_data = ph_data.replace({
            column_list[count] : value_maps[count]
        })
    emergency_funds = (ph_data['can_get_emergency_funds'].value_counts() / len(ph_data)).to_frame()
        
    savings_given_acct_owned = (
        ph_data.groupby([
            "has_a_fin_account","saves_in_a_fin_account"
            ])["wpid_random"].count() /   ph_data.groupby([
                "has_a_fin_account"
                ])["wpid_random"].count()
    ).to_frame()
    # (ph_data['has_a_fin_account'].value_counts() / len(ph_data)).to_frame()
    # (ph_data["saves_in_a_fin_account"].value_counts() / len(ph_data)).to_frame()    
    
    by_age_group_tab, by_income_group_tab = st.tabs(['By Age Group', 'By Income Group'])
    with by_age_group_tab:
        age_results = variable_tester("age_group", ph_data)
        # with savings account
        fig = plt.figure(figsize=(7,3)  , dpi=200)
        plt.ylim(0,1)
        plt.plot(
            # x axis
            age_results[
            (age_results["has_a_fin_account"] == True) & 
            (age_results["can_get_emergency_funds"] == True)
            ].iloc[:,0],
            
            # y axis
            age_results[
            (age_results["has_a_fin_account"] == True) & 
            (age_results["can_get_emergency_funds"] == True)
            ].iloc[:,-1],
            
            color = '#07b1f0',
            linewidth=3
            )

        # without savings accounts

        plt.plot(
            # x axis
            age_results[
            (age_results["has_a_fin_account"] == False) & 
            (age_results["can_get_emergency_funds"] == True)
            ].iloc[:,0],
            
            # y axis
            age_results[
            (age_results["has_a_fin_account"] == False) & 
            (age_results["can_get_emergency_funds"] == True)
            ].iloc[:,-1],
            color = 'grey',
            linewidth=3
            )

        plt.xlabel("Age Group")
        plt.ylabel("probability of possessing emergency funds")
        plt.legend(["With accounts", "Without accouunts"])
        plt.title("Age Group and Financial Resilience")
        
        st.pyplot(fig)
    with by_income_group_tab:
        inc_result = variable_tester("income_group", ph_data)
    
        # with savings account
        fig2 = plt.figure(figsize=(7,3)  , dpi=200)
        plt.ylim(0,1)
        plt.plot(
            # x axis
            inc_result[
            (inc_result["has_a_fin_account"] == True) & 
            (inc_result["can_get_emergency_funds"] == True)
            ].iloc[:,0],
            
            # y axis
            inc_result[
            (inc_result["has_a_fin_account"] == True) & 
            (inc_result["can_get_emergency_funds"] == True)
            ].iloc[:,-1],
            
            color = '#07b1f0',
            linewidth=3
            )

        # without savings accounts

        plt.plot(
            # x axis
            inc_result[
            (inc_result["has_a_fin_account"] == False) & 
            (inc_result["can_get_emergency_funds"] == True)
            ].iloc[:,0],
            
            # y axis
            inc_result[
            (inc_result["has_a_fin_account"] == False) & 
            (inc_result["can_get_emergency_funds"] == True)
            ].iloc[:,-1],
            color = 'grey',
            linewidth=3
            )

        plt.xlabel("Income Group")
        plt.ylabel("probability of possessing emergency funds")
        plt.legend(["With accounts", "Without accouunts"])
        plt.title("Income Group and Financial Resilience")
        st.pyplot(fig2)
    
    
def variable_tester(var, ph_data):
    test_group = ph_data.groupby([var, "has_a_fin_account", "can_get_emergency_funds"]).agg( 
    total_count=('wpid_random', 'count')).reset_index()

    conditions = []
    unique_values = ph_data[var].unique()

    for value in unique_values:
        condition = (test_group[var] == value)
        conditions.append(condition)

    results = []
    for value in unique_values:
        result = (test_group["total_count"] / test_group[test_group[var] == value]["total_count"].count())
        results.append(result)

    # Create the denominator for the frame
    group_test = ph_data.groupby([var,"has_a_fin_account","has_a_fin_account"])["wpid_random"].count().to_frame()
    new_group = pd.concat([group_test,group_test])
    denom = new_group.sort_index(ascending= True).wpid_random

    test_denom = denom.to_frame()
    test_denom = test_denom[test_denom.wpid_random != 0]
    final = test_denom.reset_index(drop=True).wpid_random

    test_group["total_in_percentage"] = test_group["total_count"] / final

    return test_group
# def plot_fi_resilience_in_income_groups():
    
    
    
def ml_modelling():
    st.title(
        "Clustering"
    )
    st.image('images/J.png')

def conclusion():
    st.title(
        "Conclusion"
    )
    st.markdown("- ### Access to bank account empowers Filipinos to save and be more self-resilient against unexpected emergencies.")
    st.markdown("- ### There is still a huge opportunity for bank account access to Filipinos, and most of it are for reasons that we can address.")

def recommendations():
    st.title(
        "What We Can Do"
    )
    st.markdown("- ### Simplify account opening processes and removing fees for no-frills accounts.")
    st.markdown("- ### Offer a range of products specifically designed to help people cope with emergencies.")
    st.markdown("- ### Redefine traditional financial literacy to include digital literacy.")


def the_team():
    # Write the title
    st.title(
        "The Team"
    )
    st.markdown(
    """
    **Group 3: The Boys**
    - Chavez
    - Chua
    - Didal
    - Dometita
    - Pantoja
    - Tiu
    """
    )


global_data = load_data()

list_of_pages = [
    "Title",
    "Study Context",
    "Problem Statement",
    "Objectives",
    "Dataset",
    "Methodology",
    "Exploratory Data Analysis",
    "Machine Learning / Modelling",
    "Conclusion",
    "Recommendations",
    "The Team"
]

selection = st.sidebar.radio("", list_of_pages)

if selection == "Title":
    title()
elif selection == "Study Context":
    study_context()
elif selection == "Problem Statement":
    problem_statement()
elif selection == "Objectives":
    objectives()
elif selection == "Dataset":
    dataset()
elif selection == "Methodology":
    methodology()
elif selection == "Exploratory Data Analysis":
    eda()
elif selection == "Machine Learning / Modelling":
    ml_modelling()
elif selection == "Conclusion":
    conclusion()
elif selection == "Recommendations":
    recommendations()
elif selection == "FI Status Worldwide":
    fi_state_worldwide()
elif selection == "What We Can Do":
    recommendations()
elif selection == "The Team":
    the_team()
