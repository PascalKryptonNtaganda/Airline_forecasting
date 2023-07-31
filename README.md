Airline forecasting

The forecast model our project is based off is the multiplicative model. This model
forecasts the bookings by taking the on-the-book tickets and using a historical average to predict
the final booked tickets. The historical average is calculated by first finding the booking pace.
The booking pace takes the final booking date by finding when the booking date is equal to the
departure date. The final booking date is then used to find the total bookings under the
‘cum_bookings’ column. The days prior is then calculated for the booking to departure date for
each row. The booking pace can then be calculated by taking the cumulative booking and
dividing it by the total booking for each day prior. The forecast model can then be formed by
taking the cumulative bookings for each day and applying the booking pace to create the
‘multiplicative’, which is the predicated number of booked tickets. The data can then be
compared with the naïve forecast provided by subtracting the two columns for each row (day
prior) to the actual booked tickets to find the absolute error between the two predictions. The
absolute error and the sum of this absolute error show which forecast provides a more accurate
number of the final booked tickets. The pace from the training data set is then used to find the
predicted number of tickets for the validation set. Our model reduced the error from the naïve
forecast by 1.69% or 155 tickets. 
