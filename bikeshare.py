import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city? chicago, new york city, or washington\n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry, that entry is not valid.")
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = input("\nWhich month ? January, February, March, April, May, June or type 'all'\n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Sorry, that entry is not valid.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Are you looking for a specific day? enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'\n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Sorry, that entry is not valid.")
    print('-'*40)
    return city, month, day


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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Common Month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Common day:', common_day)


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Common Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nCommonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    start_end_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nfrequent combination of start station and end station:', start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " days")


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender:\n', gender_types)
    except KeyError:
      print("\nGender:\nNo data available.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available .")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1
    
    print('\nWould you like to view 5 rows of individual trip data?\n')
    while True:
        raw_data = input('yes or no:').lower()
        if raw_data == 'yes':
           
            print('\n Displaying rows {} to {}:\n'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

           
            print('\n Would you like to see the next 5 rows?')
            continue
        else:
            break
  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()