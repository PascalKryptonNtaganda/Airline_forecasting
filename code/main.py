
import os
import pandas as pd
from datetime import datetime
import math

## main function
 if __name__ == '__main__':
 training_df = pd.read_csv(training_data)
 validation_df = pd.read_csv(validation_data)
 training_df['departure_date'] = pd.to_datetime(training_df['departure_date'])
 training_df['booking_date'] = pd.to_datetime(training_df['booking_date'])
 pace = get_booking_pace(training_df)
 model = mult_model(validation_df, pace)
 print(model)