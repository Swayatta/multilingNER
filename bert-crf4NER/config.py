class Config(object):	
  apr_dir = '../model/'
  data_dir = '../corpus/'
  model_name = 'model_4.pt'
  epoch = 5
  bert_model = 'bert-base-uncased'
  lr = 5e-5
  eps = 1e-8
  batch_size = 10
  mode = 'prediction' # for prediction mode = "prediction"
  training_data = 'biotags_train.txt'
  val_data = 'biotags_valid.txt'
  test_data = 'biotags_valid.txt'
  test_out = 'test_prediction.csv'
  raw_prediction_output = 'raw_prediction.csv'
