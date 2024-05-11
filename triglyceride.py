import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

# Load the datasets
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# Combine train and test data for preprocessing
combined_df = pd.concat([train_df, test_df])

# Handle missing values if any
combined_df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# Convert categorical variables to numerical using Label Encoding
le = LabelEncoder()
combined_df['gender'] = le.fit_transform(combined_df['gender'])
combined_df['smoking_habit'] = le.fit_transform(combined_df['smoking_habit'])
combined_df['drinking_habit'] = le.fit_transform(combined_df['drinking_habit'])
combined_df['residential_area'] = le.fit_transform(combined_df['residential_area'])

# Split the combined data back into train and test sets
train_processed = combined_df[:len(train_df)]
test_processed = combined_df[len(train_df):]

# Define features and target variable
features = ['gender', 'age', 'height_in_cm', 'weight_in_lbs', 'smoking_habit', 'glucose_lvl', 'creatinine_lvl']
target = 'triglyceride_lvl'

# Split train data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(train_processed[features], train_processed[target], 
                                                      test_size=0.2, random_state=42)

# Initialize XGBoost regressor model
model = XGBRegressor()

# Fit the model on training data
model.fit(X_train, y_train)

# Make predictions on validation data
valid_preds = model.predict(X_valid)

# Calculate Mean Absolute Error (MAE) on validation data
mae = mean_absolute_error(y_valid, valid_preds)
print(f'Mean Absolute Error on validation set: {mae}')

# Make predictions on test data
test_preds = model.predict(test_processed[features])

# Prepare submission file
submission_df = pd.DataFrame({'candidate_id': test_df['candidate_id'], 'triglyceride_lvl': test_preds})
submission_df.to_csv('sample_submission.csv', index=False)