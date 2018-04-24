exports.handler = function(event, context, callback) {
   console.log("Received event: ", event);
   var data = {
       "greetings": "Response received "
   };
   var AWS = require("aws-sdk");
AWS.config.update({
accessKeyId: "AKIAJMK4AYSVSE36PIZQ",
secretAccessKey: "juVOnmMi1WVB+TEe/ILsObDy81JbkfJX/PRqrn4n",
region: "us-east-1"
});

var sns = new AWS.SNS();
sns.publish({
Message: 'Your parent responses that he does not fall',
PhoneNumber: '+16463277677'
}, function (err, data) {
if (err) {
console.log(err.stack);
return;
}

console.log("push sent");
});



   
   callback(null, data);
}