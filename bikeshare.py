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

    city = input ("\nCan you please enter the name of your city - Chicago, New York City or Washington? ").lower()
    while city in ['chicago', 'new york city', 'washington']:
        print("\nThank you for selecting {}, that looks wonderful!".format(city))
        break
    else:
        city = input("\nSorry, I didn't quite get that! Could you please select the name of the city you want to examine - \n'Chicago', New York City' or 'Washington'. Thank you! ").lower()
        
    

    # get user input for month (all, january, february, ... , june)
    month = input("\nCan you please enter a month between January and June? For all the months, please type 'All' ").lower()
    while month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print ("\nThank you for selecting your month! You have selected {}. That all looks great!".format(month))
        break
    else:
        month = input("\nSorry, I didn't quite get that! Could you please select a month out of - \n'January', 'February', 'March', 'April', 'May', 'June' or 'All'? Thank you! ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nCan you please enter a day of the week to examine? For all days, please type 'All' ").lower()
    while day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print ("\nThank you! You have selected {}. That looks great!".format(day))
        break
    else:
        day = input("\nSorry, I didn't quite get that! Could you please type in a day out of - \n'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' or 'All'? Thank you! ").lower()
        
    print("\nYou have selected - \nCity - {} \nMonth - {} \nDay - {}".format(city, month, day))
    
    quitprogram = input("\nIs this OK? Please select 'Yes' to continue or 'No' to quit the program.").lower()
    if quitprogram == "no":
        quit()
    else:
         print("\nThank you, let's continue!")

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
    df['hour'] = df['Start Time'].dt.hour
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

    # display the most common month
    common_month = (df['month'].value_counts().idxmax())
    
    print("\nThe most common month is month {}".format(common_month))

    # display the most common day of week
    common_day = (df['day_of_week'].value_counts().idxmax())

    print("\nThe most common day of the week is {}".format(common_day))
    
    # display the most common start hour
    common_hour = (df['hour'].value_counts().idxmax())
    
    print("\nThe most common start hour is hour {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_st_station = (df['Start Station'].value_counts().idxmax())

    print("\nThe most commonly used start station is {}".format(common_st_station))

    # display most commonly used end station
    common_end_station = (df['End Station'].value_counts().idxmax())

    print("\nThe most commonly used end station is {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    
    se_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    
    print("\nThe most common combination of start station and end station is {}".format(se_combination))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totaltime = df['Trip Duration'].sum()
    
    print("\nThe total travel time is {}".format(totaltime))

    # display mean travel time
    meantime = df['Trip Duration'].mean()

    print("\nThe mean travel time is {}".format(meantime))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    print("\nThe listings below show the breakdown of total users into Subscribers and Customers -")

    subscriber = df['User Type'].value_counts()['Subscriber']
    
    customers = df['User Type'].value_counts()['Customer']
    
    print("\nThe total count of Subscribers is {}".format(subscriber))
    
    print("\nThe total count of Customers is {}".format(customers))

    # Display counts of gender
    
    print("\nThe listings below show the data values broken down into Gender type - Male / Female / Null results -")
    
    try:
    
        malecount = df['Gender'].value_counts()['Male']
    
        femalecount = df['Gender'].value_counts()['Female']
    
        nullcount = df['Gender'].isnull().sum()
    
        print("\nThe total number of Male listings is {}".format(malecount))
    
        print("\nThe total number of Female listings is {}".format(femalecount))
    
        print("\nThe total number of Null listings is {}".format(nullcount))
        
    except:
        print("\nSorry, we don't have any data for this filter!")
  

    # Display earliest, most recent, and most common year of birth
    
    print("\nThe listings below show the breakdown of Birth Years into earliest / latest / most common year of birth -")
    
    try:
    
        earliestdate = df['Birth Year'].min()
    
        earliestdate = int(earliestdate)
    
        recentdate = df['Birth Year'].max()
    
        recentdate = int(recentdate)

        commondate = (df['Birth Year'].value_counts().idxmax())
    
        commondate = int(commondate)
    
        print("\nThe earliest birth year is {}".format(earliestdate))
    
        print("\nThe most recent birth year is {}".format(recentdate))
    
        print("\nThe most common year of birth is {}".format(commondate))
        
    except:
        
        print("\nSorry, we don't have any data for this filter!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rawdata(df):
    
    """Displays statistics on the raw data."""
    
    print('\nCalculating Raw Data Stats...\n')
    
    start_time = time.time()
    
    start_loc = 0
    
    while True:
        rawinput = input("\nWould you like to see the top 5 rows of data? Please select 'Yes' or 'No': ").lower()
        if rawinput == "no":
            break
        else:
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            

if __name__ == "__main__":
	main()