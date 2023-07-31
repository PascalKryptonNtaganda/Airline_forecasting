
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

