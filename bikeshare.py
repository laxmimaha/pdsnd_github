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
    city = ""
    day = ""
    month = ""
    while (city not in CITY_DATA.items()):
        city = input('Name of the city to analyze:\n').lower()
        if city  in ('chicago','new york city','washington'):
            break;
        else:
            print("Sorry you might entered a wrong city!!Enter city names as chicago,new york city, washington")
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while  (month not in ['january','february', 'march', 'april', 'may', 'june'] ):
        month = input('Name of the Month:\n').lower()
        if month in ['january','february', 'march', 'april', 'may', 'june'] and month != 'all':
            break;
        else:
            print("Enter single month upto January to June")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
        day = input('Enter the Day:\n').lower()
        if day in ['monday', 'tuesday'  , 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and day != 'all':
            break;
        else:
            print("Sorry  Enter Correct Day")
    

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
    filename = CITY_DATA[city]   # to load data
    df = pd.read_csv(filename) 
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])      #to convert time to data
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print("User entered month:")
    print(month)
    print("month column for raw data")
    print(df['month'][:5])
    print("user entered day:")
    print(day)
    print("day for raw data")
    print(df['day_of_week'][:5])
    #Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print("converted month")
        print(month)
        df =df[df['month'] == month]
       
            
   
       
                
                
    if day != 'all':
        print(day)
        df =df[df['day_of_week'] == day.title()]
        
            
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Common_Month:\n',popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Common_day:\n',popular_day)

    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Common_hour:\n',popular_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Common_Start_Station :\n',popular_startstation) 


    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('Common_Start_Station\n',popular_endstation) 

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station']+ ','+df['End Station']).mode()[0]
    print('Most frequent start and end station:\n',common_start_end)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total_Time:\n",total_time)
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Total_Mean_Time:\n",mean_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of each user_type:\n",user_types)
    
 

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Count of each Gender:\n",gender)
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print("Earliest year:\n",earliest_year)
        mostrecent_year = df['Birth Year'].max() 
        print("Most Recent Year:\n",mostrecent_year)
        common_year = df['Birth Year'].mode()[0]
        print("Most Common year:\n",mostrecent_year)
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def entries(df):
    entries = input('\nWould you like to see the first 5 rows of data? Answer yes or no:\n')
    i = 0
    while True:
         if entries.lower() == 'yes':
             print(df.iloc[i:i+5])
             i += 5
             entries = input('\nWould you like to see additional 5 rows of data? Answer yes or no.\n')
             entries.lower()
         else:
             break
 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        entries(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

