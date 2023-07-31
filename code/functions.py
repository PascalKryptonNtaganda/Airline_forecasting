
def get_booking_pace(df):
 fmt = '%Y-%m-%d'
 #booking pace for days prior
 #key: days prior
 #value: rate. percentage of final/total booking already booked before days prior
 booking_pace = {}
 final_booking = df.loc[df['booking_date'] == df['departure_date']]

 #loop finds all the on-the-book bookings for any days prior
 for index, row in df.iterrows():
 departure = row['departure_date']
 booking = row['booking_date']
 total_booking = final_booking.loc[final_booking['departure_date'] ==
departure]
 total_booking = total_booking['cum_bookings']
 days_prior = departure - booking
 days_prior = days_prior.days

 if days_prior in booking_pace and booking_pace[days_prior]:
 val = booking_pace[days_prior]
 booking_pace[days_prior] =
val.append(row['cum_bookings']/total_booking)
 else:
 booking_pace[days_prior] = [row['cum_bookings']/total_booking]

 #finds average booking pace for any days prior
 for key, value in booking_pace.items():
 booking_pace[key] = float(sum(value))/len(value)
 return booking_pace

def mult_model(df, booking_pace):
 #for each departure date finds a forecast
 #using mulitplicative model
 df = validation_df.dropna(how='any',axis=0)
 df['multiplicative'] = 0
 fmt = '%Y-%m-%d'
 df['departure_date'] = df['departure_date'].astype('datetime64[ns]')
 df['booking_date'] = df['booking_date'].astype('datetime64[ns]')

 for index, row in df.iterrows():
 days_prior = row['departure_date'] - row['booking_date']
 days_prior = days_prior.days
 if math.isclose(booking_pace[days_prior], 0, rel_tol=1e-2):
 df.loc[index, 'multiplicative'] = 0
 else:
 
 #formula from slides
 df.loc[index, 'multiplicative'] =
row['cum_bookings']/booking_pace[days_prior]
 for index, row in df.iterrows():
 
 #finds the absolute error for our forecast to naive forecast and shows sum
difference
 df.loc[index, 'Our Forecast Absolute Error'] = abs(row['multiplicative'] -
row['cum_bookings'])
 df.loc[index, 'Naive Forecast Absolute Error'] = abs(row['naive_fcst'] -
row['cum_bookings'])
 MASE = df['Our Forecast Absolute Error'].sum() / df['Naive Forecast Absolute
Error'].sum()
 print("Our model reduced errors by " + str(round(MASE,2)) + " percent or by " +
str(round(MASE/100*9154)) + " tickets.")
 return df