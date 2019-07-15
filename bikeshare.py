import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#Commit Test 1
# This is just for commit in github

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def city_input():
        while True:
            try:
                city = input('\n Enter one of these city Chicago,New York city or Washington:\n').lower()
                if city in CITY_DATA:
                    print('\ Good choice! Let\'s see data of {} City \n'.format(city.title()))
                    return city
            except:
                    print('\n Oops! There is no {} city in the list. \n'.format(city.title()))
    # TO DO: get user input for month (all, january, february, ... , june)
    def month_input():
        while True:
            try:
                month_input = int(float(input('\n If you would like to filter data by month, Please Enter the number of the following onths : 1- January,2- February,3-March, 4-April,5-May,6-June. or Enter "0" to apply no filter \n')))
                if(0 <= month_input <= 6 ):
                   return month_input
                   print('\n Great! Let\'s selecte the day !')
                   break
                else:
                   print('\n Oops! There is no {} Name of Month in the list, Make sure to enter month by number from 1-6 or 0 for no filter. \n'.format(month_input))
            except ValueError:
             print ('\n This is not a Month . Please Enter one of the these months  numbers: 1-January, 2-February,3-March, 4-April,5-May,6-June you would like to filter the data by it. \n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def day_input():
        while True:
            try:
                day_input = input('\n If you would like to filter data by day, Please Enter the days of the week of day or Enter "0" for no filter . \n').title()
                day_list=['Monday', 'Tuesday','Wednesday', 'Friday','Saturday','Sunday','0']
                if day_input in day_list:
                  return day_input
                  print('\n  In the folloing you will find data filltered by {} day  \n'.format(day_input.title()))
                  break
                else:
                   print('\n Oops! There is no {} Name of day in the list. \n'.format(day_input))
            except ValueError:
               print ('\n This is not a day name . Please Enter the day of the week that you want to filter your data by it. \n')

        print('-'*40)
    return city_input(), month_input(), day_input()

def raw():
    df = load_data(city,month,day )
    raw_data = input('\n if you you want to see the raw data ,enter "yes" if not enter  enter "no": \n').lower()
    if raw_data in ('yes','y'):
          i=0
          while True:
           print(df.iloc[i:i+5])
           i += 5
           further_data = input('\n For more data Enter "yes"  or "no":\n').lower()
           if further_data  not in  ('yes','y'):
               break


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   #Data file into datframe
    df= pd.read_csv(CITY_DATA[city])
   #covert column of the Start time into datatime
    df['Start Time']= pd.to_datetime(df['Start Time'])
   #Call month and day of the week from Start Time
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name

  #Data filter by month
    if month != 0:
     df=df[df['month']== month]
   #Data filter by day of the week
    if day != '0':
     df=df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('\n the Most common month:', most_common_month)

    # TO DO: display the most common day of week
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['day_of_week']= df['Start Time'].dt.weekday_name
    most_common_DOW =   df['day_of_week'].mode()[0]
    print('\n the Most common day of the week:',most_common_DOW )

    # TO DO: display the most common start hour
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['hour']= df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\n the Most common hour:',most_common_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_used_Sstation =  df['Start Station'].mode()[0]
    print('\n the Most commonly used start station',common_used_Sstation )

    # TO DO: display most commonly used end station
    common_used_Estation =  df['End Station'].mode()[0]
    print('\n the Most commonly used End station',common_used_Estation )

    # TO DO: display most frequent combination of start station and end station trip
    common_start_End_station =  df[['Start Station','End Station']].mode().loc[0]
    print('\n Most frequent combination of start station and end station trip \n',common_start_End_station  )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print('\nTotal travel time in minutes:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('\n Average travel time in minutes:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    print('\n User Type:',user_types)

    # TO DO: Display counts of gender
    if city in ('chicago','new york'):
      counts_gender= df['Gender'].value_counts()
      print('\n User counts of gender',counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
      youngest_user = df['Birth Year'].max()
      oldest_user = df['Birth Year'].min()
      common_user= df['Birth Year'].mode()[0]
      print('\n Youngest user was born in {}.\n'.format(int( youngest_user)))
      print('\n Oldest user was born in {}.\n'.format(int( oldest_user)))
      print('\n most common year of birth user was born in {}.\n'.format(int( common_user)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

city, month, day = get_filters()
df = load_data(city, month, day)

# git test 3
def main():
    while True:
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
#Git commit Test 2
if __name__ == "__main__":
	main()

# git test 4

# comment with one liner