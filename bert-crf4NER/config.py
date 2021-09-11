class Config(object):	
  apr_dir = '../model/'
  data_dir = '../corpus/'
  model_name = 'model_0.pt'
  epoch = 1
  bert_model = 'allenai/scibert_scivocab_uncased'
  lr = 5e-5
  eps = 1e-8
  batch_size = 10
  mode = 'prediction' # for prediction mode = "prediction"
  training_data = 'trainbio.txt'
  val_data = 'trainbio.txt'
  test_data = 'testbiov2.txt'
  test_out = 'test_prediction.csv'
  raw_prediction_output = 'raw_prediction.csv'
  hidden_dropout_prob = 0.5