import pandas as pd

def add_survey_summary(df_data, df_dims):
    location_dates = df_dims[['location','date']].values
    for a_pair in location_dates:
        some_data = get_one_day_survey_details(location=a_pair[0], date=a_pair[1], data=df_data)
        df_dims.loc[(df_dims.location==a_pair[0]) & (df_dims.date==a_pair[1]), 'variety'] = some_data['variety']
        df_dims.loc[(df_dims.location==a_pair[0]) & (df_dims.date==a_pair[1]), 'pcs_m'] = some_data['pcs_m']
        df_dims.loc[(df_dims.location==a_pair[0]) & (df_dims.date==a_pair[1]), 'quantity'] = some_data['quantity']
def get_one_day_survey_details(location="", date="", data=""):
    """Returns the total quantity, pieces/meter and number of categories for
    for one survey. Uses a dataframe from the API endpoint:
    'https://mwshovel.pythonanywhere.com/api/surveys/daily-totals/code-totals/'.

    This functions assumes the following column names: 'location', 'date','code','pcs_m' and 'quantity'.
    """
    survey_data = data.loc[(data.location==location) & (data.date==date)]
    number_codes = len(survey_data)
    pcs_m = round(survey_data.pcs_m.sum(), 3)
    quantity = survey_data.quantity.sum()
    return dict({}, variety=number_codes, pcs_m=pcs_m, quantity=quantity)
def get_dims_data_for_one_survey(location="", date="", data=""):
    """Returns a dictionary of the dimensional data for one survey. Uses a dataframe from the endpoint:
    'https://mwshovel.pythonanywhere.com/api/surveys/dim-data/dim-data-list/'.
    """
    return data[(data.location==location) & (data.date==date)].to_dict('records')[0]
def add_data_to_report_summary(dims_df, summary_survey_index, summary_survey_columns, columns_of_interest):
    """Summarizes the specified columns from the combined dims_data datarame. Calls df.describe()
    and extracts the pertienent value to the column and row specified the row-column indexer.
    """
    a_new_df = pd.DataFrame(index=summary_survey_index, columns=summary_survey_columns)
    for column in columns_of_interest:
        a_summary = dims_df[column].describe()
        for metric in summary_survey_columns:
            if metric == 'average':
                a_new_df.loc[column, 'average'] = a_summary['mean']
            elif metric == 'median':
                a_new_df.loc[column, 'median'] = a_summary['50%']
            else:
                a_new_df.loc[column, metric] = a_summary[metric]
    return a_new_df
