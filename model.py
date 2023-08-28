from pycaret.regression import *
from pycaret.datasets import get_data

data = get_data('insurance')
r2 = setup(data,target='charges', session_id= 123,
normalize = True, 
polynomial_features = True,
feature_selection=True,
bin_numeric_features = ['age','bmi'])

lr = create_model('lr')
plot_model(lr, plot='residuals')

save_model(lr, model_name= 'deployment-nummer-1')