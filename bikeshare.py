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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Would you like to see the data for Chicago, New York City or Washington?\n').lower()
    while city not in ['chicago','new york city','washington']:
        print('please input one of city in Chicago, New York City or Washington!')
        city=input('Would you like to see the data for Chicago, New York City or Washington?\n').lower()
        
    choice=input('would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n')
    while choice not in ['month','day','both','none']:
        print('please input the right command!')
        choice=input('would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n')
    if choice=='month':
        month=input('Which month? January, Febuary, March, April, May or June?\n').lower()
        day='all'
    elif choice=='day':
        month='all'
        day=input('Which day? Monday, Tuesday, Wednesday, Thuresday, Friday, Saterday or Sunday?\n').lower()
    elif choice=='both':
        month=input('Which month? January, Febuary, March, April, May or June?\n').lower()
        day=input('Which day? Monday, Tuesday, Wednesday, Thuresday, Friday, Saterday or Sunday?\n').lower()
    else:
        month='all'
        day='all'
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
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
        month = months.index(month)+1
        df = df[df['month']==month]
        # filter by month to create the new dataframe

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['start hour']=df['Start Time'].dt.hour
    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('The most common month: {}.'.format(common_month))
    # TO DO: display the most common day of week
    common_day_of_week=df['day_of_week'].mode()[0]
    print('The most common day of week: {}.'.format(common_day_of_week))
    # TO DO: display the most common start hour 
    common_start_hour=df['start hour'].mode()[0]
    print('The most common start hour: {}.'.format(common_start_hour))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station: {}.'.format(commonly_start_station))
    # TO DO: display most commonly used end station
    commonly_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station: {}.'.format(commonly_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    df['Start station & End station']='Start Station: '+df['Start Station']+' / '+'End Station: '+df['End Station']
    commonly_combination=df['Start station & End station'].mode()[0]
    print('The most frequent combination of start and end station trip:\n {}.'.format(commonly_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time: {}.'.format(total_travel_time))
   
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The average travel time: {}.'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('Counts of user types:\n{}.\n'.format(user_types))
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print('Counts of gender:\n{}.\n'.format(gender))
    else:
        print('No Gender information.')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:        
        earlist_birth_year=df['Birth Year'].min()
        recent_birth_year=df['Birth Year'].max()
        common_birth_year=df['Birth Year'].mode()[0]
        print('The most oldest birth year: {}.'.format(earlist_birth_year))
        print('The most youngest birth year: {}.'.format(recent_birth_year))
        print('The most common birth year: {}.'.format(common_birth_year))
    else:
        print('No Birth Year information.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data(df,i):
    index_name=df.index.values
    for n in index_name[5*i:5*(i+1)]:
        print('Index:{}'.format(n))
        print('Start Station:{}'.format(df.loc[n]['Start Station']))
        print('Start Time:{}'.format(df.loc[n]['Start Time']))
        print('End Station:{}'.format(df.loc[n]['End Station']))
        print('End Time:{}'.format(df.loc[n]['End Time']))
        print('Duration:{}'.format(df.loc[n]['Trip Duration']))
        print('User Type:{}'.format(df.loc[n]['User Type']))
        print('-'*10)
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        i=0
        while True:
             individual=input('\nWould you like to view individual data? Enter yes or no.\n')
             if individual.lower()=='yes':
                individual_data(df,i)
                i=i+1
             else:
               break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
