
// Code used is from awslab github with slight modifications

console.log("Loading event")
exports.handler = function(event, context) {
  var AWS = require('aws-sdk');
  var ml = new AWS.MachineLearning();
  var endpointUrl = 'https://realtime.machinelearning.us-east-1.amazonaws.com';
  var mlModelId = 'ml-8oKdxVJRc8R';
  var numMessagesToBeProcessed = event.Records.length;
  var sns = new AWS.SNS();
  var callPredict = function(mtaData){
    console.log('calling predict');
    var lat = mtaData['lat']
    var long = mtaData['lng']
    var bpm = mtaData['BPM']
    var phone1 = '+19293106827'
    var phone2 = '+16463277677'
    delete mtaData['lat']
    delete mtaData['lng']
    delete mtaData['phone_parent']
    delete mtaData['phone_children']
    delete mtaData['BPM']
    console.log(phone1)
        ml.predict(
            {
                Record : mtaData,
                PredictEndpoint : endpointUrl,
                MLModelId: mlModelId
                
            },function(err, data) {
      console.log("hi s")
                if (err) {
                    console.log(err);
                    context.done(null, 'Call to predict service failed.');
                    
                }
                else {
                    console.log('Predict call succeeded');
                    if(data.Prediction.predictedLabel === '1'){
                        console.log("Prediction 1")
                        sns.publish({
                          Message: 'Mr/Mrs XXX falls\n'  +'lat:' +lat+ '\nlong:'+long + '\nbpm:'+bpm,
                          PhoneNumber: phone1
                          }, function (err, data) {
                        if (err) {
                          console.log(err.stack);
                            return;
                              }

                  console.log("push sent");
                      });
                      sns.publish({
                          Message: 'Mr/Mrs XXX falls\n'  +'lat:' +lat+ '\nlong:'+long + '\nbpm:'+bpm,
                          PhoneNumber: phone2
                          }, function (err, data) {
                        if (err) {
                          console.log(err.stack);
                            return;
                              }

                  console.log("push sent");
                      });
                        
                    }
                    else if (data.Prediction.predictedLabel === '0'){
                        console.log("Prediction 0")
                        sns.publish({
                          Message: 'Your parent does not falls'+'\nlat:'+lat+'\nlong:'+long+ '\nbpm:'+bpm,
                          PhoneNumber: phone2
                          }, function (err, data) {
                        if (err) {
                          console.log(err.stack);
                            return;
                              }

                  console.log("push sent");
                      });
                        
                    }
                    else{
                        console.log("Prediction undefined")
                        
                    }
        }
                
            });
    }
  
         
  var processRecords = function(){
    for(var i = 0; i < numMessagesToBeProcessed; ++i) {
      var encodedPayload = event.Records[i].kinesis.data;
      // Amazon Kinesis data is base64 encoded so decode here
      var payload = new Buffer(encodedPayload, 'base64').toString('utf-8');
      try {
        var parsedPayload = JSON.parse(payload);
        //remove '' and 'first' labels
            delete parsedPayload['']
        
        callPredict(parsedPayload);
      }
      catch (err) {
        console.log(err, err.stack);
        context.done(null, "failed payload"+payload);
      }
    }
  }

    var checkRealtimeEndpoint = function(err, data){
    if (err){
      console.log(err);
      context.done(null, 'Failed to fetch endpoint status and url.');
    }
    else {
      var endpointInfo = data.EndpointInfo;
      console.log("end point info is : "+endpointInfo)    
      if (endpointInfo.EndpointStatus === 'READY') {
        endpointUrl = endpointInfo.EndpointUrl;
        console.log('Fetched endpoint url :'+endpointUrl);
        processRecords();
      } else {
        console.log('Endpoint status : ' + endpointInfo.EndpointStatus);
        context.done(null, 'End point is not Ready.');
      }
    }
  };

  ml.getMLModel({MLModelId:mlModelId,Verbose:true},checkRealtimeEndpoint);
  //context.succeed("Successfully processed " + event.Records.length + " record.");
};